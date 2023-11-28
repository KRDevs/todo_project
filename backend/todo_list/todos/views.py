from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TodoSerializer
from .models import Todo


class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
