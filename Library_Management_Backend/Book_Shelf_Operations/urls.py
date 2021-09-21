from django.urls import path
from .views import BookShelfViewInsert, BookShelfUpdateDelete

urlpatterns = [
    path('bookshelf/listadd/api/V1', BookShelfViewInsert.as_view({'get' : 'list', 'post' : 'create'})),
    path('bookshelf/updatedelete/api/v1/<int:id>', BookShelfUpdateDelete.as_view({'get' : 'retrieve', 'put' : 'update',
                                                                         'delete' : 'destroy'}))
]