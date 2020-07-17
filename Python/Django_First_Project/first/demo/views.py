from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#
# class Another(View):
#     books = Book.objects.get(id=1)
# # all - даст сет всех объектов
#     # filter - сет всех объектов, удовлетворяющих улсовию, например  (is_published = True)
#     # get - первый объект, удовлетворяющий условию.  Итерироваться по нему уже будет нельзя.
#     output = f'We have "{books.title}" with ID = {books.id}<br>'
#     # for book in books:
#     #     output += f'We have {book.title} book with id = {book.id} in DB<br>'
#     def get(self, request):
#         return HttpResponse(self.output)
# # можно удалить, низкоуровневый пробник
#
#
# def first(request):
#     books = Book.objects.all()
#     return render (request, 'first_temp.html', {'books': books})
# # можно удалить, низкоуровневый пробник


class BookViewSet (viewsets.ModelViewSet):      # Ctrl+ЛКМ - перешли в код ModelViewSet, взяли там код метода retrieve
    serializer_class = BookMiniSerializer       # по умолчанию стоит МИНИсериализатор
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):       # Для метода retrieve
        instance = self.get_object()
        serializer = BookSerializer(instance)
        # вместо self.get_serializer(instance) прописали другой сериализатор и можем отдельные книги просматривать подробно
        return Response(serializer.data)