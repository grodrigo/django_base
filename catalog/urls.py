from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    # Stubs are URL-friendly word-based primary keys for data. You might use a stub
    #if you wanted your book URL to be more informative.
    #For example /catalog/book/the-secret-garden rather than /catalog/book/33.
    #url(r'^book/(?P<stub>[-\w]+)$', views.BookDetailView.as_view(), name='book-detail'),
    #r'^book/(\d+)$' for unnamed argument
]
