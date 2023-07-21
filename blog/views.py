from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Post
from .forms import NewPostForm


class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='Pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    form_class = NewPostForm
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')


# def posts_list_view(request):
#     posts = Post.objects.filter(status='Pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts': posts})
# ==========================================
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
# ==========================================
# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             form = NewPostForm()
#             return redirect(reverse('post_detail', args=[post.id]))
#     else:  # Get
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', {'form': form})
# ==========================================

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('post_detail', args=[post.id]))

#     return render(request, 'blog/post_create.html', {'form': form})

# ===================================
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', {'post': post})
