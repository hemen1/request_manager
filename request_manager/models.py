from django.db import models
from django.conf import settings
from django.utils import timezone

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rate_limit = models.IntegerField()  # 1 request per rate_limit in crontab
    is_active = models.BooleanField(default=True)


class Request(models.Model):
    class ExecutionStatus(models.IntegerChoices):
        Pending = 0, 'Pending'
        Started = 1, 'Started'
        Success = 2, 'Success'
        Failed = 3, 'Failed'
        Timeout = 4, 'Timeout'

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(settings.MAX_PRIORITY)])
    execution_time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    executed_status = models.PositiveSmallIntegerField(default=ExecutionStatus.Pending,
                                                       choices=ExecutionStatus.choices)
    expiration_time = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()

    def __str__(self):
        return f"{self.provider} - {self.priority} - {self.created_at} - {self.executed_status}"
