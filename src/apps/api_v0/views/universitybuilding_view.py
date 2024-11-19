from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.api_v0.serializers.universitybuilding_serializers import UniversityBuildingSerializer
from apps.university.models import UniversityBuilding


class UniversityBuildingViewSet(viewsets.ModelViewSet):
    serializer_class = UniversityBuildingSerializer
    queryset = UniversityBuilding.objects.all()
    http_method_names = ['get', 'post', 'head', 'options', 'list']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)