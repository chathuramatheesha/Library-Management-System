from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', LogoutView.as_view(), name='user_logout'),

    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/search/', views.AuthorSearchView.as_view(), name='author_search'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author_add'),
    path('author/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]
