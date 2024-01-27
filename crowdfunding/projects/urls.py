from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    # path('comments/', views.CommentListAPI.as_view(), name="comments_list"),
    # path('comments/<int:pk>/', views.CommentDetailAPI.as_view(), name="comment_detail"),
    # path('projects/<int:pk>/total_pledges', views.ProjectDetail.as_view()),
]