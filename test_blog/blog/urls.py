from django.urls import path
from blog import views

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostDetailView.as_view(), "post_detail"),
    path("post/new/", views.CreatePostView.as_view(), name="post_new"),
    path("post/<int:pk>/edit", views.PostUpdateView.as_view(), "post_edit"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), "post_delete"),
    path("drafts/<int:pk>", views.DraftListView.as_view(), "post_draft_list"),
    ]
