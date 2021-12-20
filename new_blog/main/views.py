

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView, LogoutView

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView

from .models import Author, Blog, Comment
from .forms import CreateBlogForm, CreateCommentForm, \
    RegisterForm, ChangeProfileForm


class HomePageView(TemplateView):
    template_name = 'main/blog/index.html'


class ListBlogsView(ListView):
    queryset = Blog.objects.all()
    template_name = 'main/blog/all_blogs.html'

    def get_ordering(self):
        return self.ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


class GetAuthorView(TemplateView):
    template_name = 'main/blog/blogger.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['author_id'])
        blogs = Blog.objects.filter(author_id=self.kwargs['author_id'])
        context['author'] = author
        context['blogs'] = blogs
        return context


class GetBlogView(TemplateView):
    template_name = 'main/blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(blog_id=self.kwargs['blog_id'])
        blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        context['blog'] = blog
        context['comments'] = comments
        return context


class AllBloggersView(ListView):
    queryset = Author.objects.all()
    template_name = 'main/blog/all_bloggers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bloggers'] = Author.objects.all()
        return context


class CreateBlogView(CreateView):
    model = Blog
    form_class = CreateBlogForm
    template_name = 'main/blog/create_blog.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        request = self.request
        a = request.user
        form.instance.author = a
        print(a)
        return super().form_valid(form)


class CreateCommentView(CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = "main/blog/create_comment.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        request = self.request
        author = request.user
        blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        form.instance.blog = blog
        form.instance.author = author
        return super().form_valid(form)


class RegisterView(CreateView):
    model = Author
    form_class = RegisterForm
    template_name = 'main/account/register.html/'
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/account/register_done.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'main/blog/index.html'


class Login(LoginView):
    template_name = 'main/account/login.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return str(self.success_url)


class ProfileView(TemplateView):
    template_name = 'main/account/profile.html'


class ChangePasswordView(PasswordChangeView):
    template_name = 'main/account/change_password.html'
    success_url = reverse_lazy('change_password_done')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'main/account/change_password_done.html'