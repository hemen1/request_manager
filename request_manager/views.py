from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Provider, Request
from .serializers import ProviderSerializer, RequestSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def destroy(self, request, *args, **kwargs):
        instance:Provider = self.get_object()
        if not instance.is_active:
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_deleted:
            instance.is_deleted = True
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
