from rest_framework import viewsets


class ViewCommon(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
