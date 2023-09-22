from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Provider
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


@receiver(post_save, sender=Provider)
def provider_post_save(sender, instance: Provider, created, **kwargs):
    if created and instance.is_active:
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=instance.rate_limit,
            period=IntervalSchedule.SECONDS,
        )
        expires, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            task='request_manager.tasks.process_request',
            name=instance.name,
            kwargs=json.dumps({'provider_id': instance.pk}),
            interval=schedule,
        )
    else:
        periodic_task = PeriodicTask.objects.filter(name__exact=instance.name).first()
        periodic_task.enabled = instance.is_active
        periodic_task.save()

@receiver(post_delete, sender=Provider)
def request_post_delete(sender, instance, using, **kwargs):
    periodic_task = PeriodicTask.objects.filter(name__exact=instance.name).first()
    periodic_task.delete()