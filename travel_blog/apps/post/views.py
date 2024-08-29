from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import CommentForm, SearchForm
from .models import *
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts1'
    paginate_by = 2
    queryset = Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:6]
        context['posts'] = Post.objects.all()
        context['tags'] = Tag.objects.all()
        context['search_form'] = SearchForm(self.request.GET)
        # context['liked_posts'] = Post.objects.filter(like__gt=0).order_by('-like')[:3]
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.GET.get('query')
    #     if query:
    #         keywords = query.split()
    #         q_objects = Q()
    #         for keyword in keywords:
    #             q_objects |= Q(title__icontains=keyword) | Q(text__icontains=keyword)
    #
    #         queryset = queryset.filter(q_objects)
    #         return queryset

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains=search_text)
            | Q(text__icontains=search_text)

        )
        return q


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_details.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return redirect('post_details', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

from django.shortcuts import get_object_or_404
class LikePostView(View, LoginRequiredMixin):
    def post(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Post,pk=pk)
        like, created = Like.objects.get_or_create(user=request.user,post=post)
        if not created:
            like.delete()
            return redirect('post_details', pk=post.pk)