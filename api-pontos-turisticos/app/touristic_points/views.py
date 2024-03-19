from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from app.common.view import ViewCommon

from .serializers import TouristicPointSerializer


class ChangePontoTuristicoViewSet(ViewCommon):
    serializer_class = TouristicPointSerializer
    queryset = serializer_class.Meta.model.objects.get_queryset()


class ReadPontoTuristicoViewSet(ViewCommon):
    serializer_class = TouristicPointSerializer
    queryset = serializer_class.Meta.model.objects.get_queryset()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        if search:
            words = search.split(" ")
            q_filters = Q()

            for word in words:
                q_filters |= Q(name__unaccent__icontains=word)
                q_filters |= Q(description__unaccent__icontains=word)

            return self.queryset.filter(q_filters)

        return self.queryset
