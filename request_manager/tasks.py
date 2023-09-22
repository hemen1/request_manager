from celery import shared_task
from .models import Request
from datetime import datetime
import time
import random
from celery.utils.log import get_logger
from django.db.models import Q

logger = get_logger(__name__)


def call_server(provider_id, request):
    logger.info(f'Starting request {str(request)}')
    time.sleep(random.randint(0, 5))
    logger.info(f'Finish request {str(request)}')
    return random.randint(0, 1)

@shared_task
def process_request(provider_id):
    request = Request.objects.filter(provider_id__exact=provider_id,
                                     executed_status=Request.ExecutionStatus.Pending,
                                     execution_time__lte=datetime.now()).filter(
                                     Q(expiration_time__gte=datetime.now()) |
                                     Q(expiration_time__isnull=True)).order_by('-priority',
                                                                               'created_at').first()
    if not request:
        return
    request_result = call_server(provider_id, request)
    if request_result:
        request.executed_status = Request.ExecutionStatus.Success
    else:
        request.executed_status = Request.ExecutionStatus.Failed

    request.save()
    return f'executed {str(request.id)}'


@shared_task
def change_status_expired_request():
    affected_rows = Request.objects.filter(executed_status=Request.ExecutionStatus.Pending,
                                           expiration_time__lt=datetime.now()).update(
        executed_status=Request.ExecutionStatus.Timeout)
    return f'number of row expiration_time arived is {str(affected_rows)}'
