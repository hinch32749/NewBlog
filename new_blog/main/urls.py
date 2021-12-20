from django.urls import path

from .views import HomePageView, ListBlogsView, GetAuthorView, GetBlogView, AllBloggersView, CreateBlogView, \
    CreateCommentView, RegisterView, RegisterDoneView, Login, Logout, ProfileView, ChangePasswordView, \
    ChangePasswordDoneView


urlpatterns = [
    path('blog/', HomePageView.as_view(), name='index'),
    path('blog/blogs/', ListBlogsView.as_view(), name='list_blogs'),
    path('blog/create_blog/', CreateBlogView.as_view(), name='create_blog'),
    path('blog/bloggers/', AllBloggersView.as_view(), name='all_bloggers'),
    path('blog/blogger/<int:author_id>/', GetAuthorView.as_view(), name='author'),
    path('blog/<int:blog_id>/', GetBlogView.as_view(), name='blog'),
    path('blog/<int:blog_id>/create_comment/', CreateCommentView.as_view(), name='create_comment'),
    path('account/register/', RegisterView.as_view(), name='register'),
    path('account/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('account/login/', Login.as_view(), name='login'),
    path('account/logout/', Logout.as_view(), name='logout'),
    path('account/profile/', ProfileView.as_view(), name='profile'),
    path('account/change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('account/change_password/done/', ChangePasswordDoneView.as_view(), name='change_password_done'),
]