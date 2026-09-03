from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ["completed"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title", "completed"]

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        # filterset_fields = ["completed"]
        # search_fields = ["title", "description"]
        # ordering_fields = ["created_at", "title", "completed"]
        # completed = self.request.query_params.get("completed")

        # if completed == "true":
        #     queryset = queryset.filter(completed=True)

        # elif completed == "false":
        #     queryset = queryset.filter(completed=False)

        # search = self.request.query_params.get("search")

        # if search:
        #     queryset = queryset.filter(
        #         title__icontains=search
        #     ) | queryset.filter(
        #         description__icontains=search
        #     )


        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        task = self.get_object()

        task.completed = True
        task.save()

        serializer = self.get_serializer(task)

        return Response(serializer.data)