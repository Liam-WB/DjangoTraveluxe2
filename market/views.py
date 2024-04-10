from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Author
from django.urls import reverse_lazy
from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        is_post_owner = post.author == request.user

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "is_post_owner": is_post_owner,
                "comment_form": CommentForm()
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user
        comments = post.comments.filter(approved=True).order_by('created_on')
        owned_comments = comments.filter(author=user)
        context['comments'] = comments
        context['owned_comments'] = owned_comments
        return context

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = form.instance.title.lower().replace(' ', '-')
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'content', 'featured_image', 'excerpt', 'listing_currency', 'listing_timespan', 'listing_price', 'status')
    template_name = "post_update_form.html"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ["name"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name=self.request.user)

class CommentDelete(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.name == request.user.username:
            comment.delete()
        
        return redirect('post_detail', slug=comment.post.slug)