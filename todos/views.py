from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializers


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        return TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        return TodoSerializers
