from django.urls import path
from . import views


urlpatterns = [
    path('', views.article), # article list, create article
    path('<int:article_id>/', views.article_detail), # article detail
    path('<int:article_id>/like/', views.article_like), # like article
    path('<int:article_id>/comments/', views.comment), # create comment
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_detail), # update comment, delete
    path('<int:article_id>/comments/<int:comment_id>/like/', views.comment_like), # like comment
]