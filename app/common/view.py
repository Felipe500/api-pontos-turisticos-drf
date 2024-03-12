from rest_framework import viewsets


class ViewCommon(viewsets.ModelViewSet):

    def get_serializer_context(self):
        return {'request': self.request, 'user': self.request.user}

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
