from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='user_login'),
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/search/', views.AuthorSearchView.as_view(), name='author_search'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author_add'),
    path('author/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]
