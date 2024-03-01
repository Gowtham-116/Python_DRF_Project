from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView,DetailView

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Gowtham",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Gowtham",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Gowtham",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Gowtham",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

all_posts=Post.objects.all().order_by("date")

def get_date(post):
    return post['date']

# Create your views here.
# def starting_page(request):
#     latest_posts=Post.objects.all().order_by("-date")[:3]
#     #sorted_posts=sorted(all_posts,key=get_date)
#     #all_posts.sort(key=get_date)
#     #latest_posts=all_posts[-3:]
#     return render(request, "blog/index.html",{
#         "posts":latest_posts
#     })  

#CLASS BASED STARTING_PAGE VIEW

class StartingpageView(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"

    def get_queryset(self):
        query_set= super().get_queryset()
        data=query_set[:3]
        return data

    

# def posts(request):
#     return render(request, "blog/all-posts.html",{
#         "all_posts":all_posts
#     })
    
class AllpostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=['-date']
    context_object_name='all_posts'


# def post_detail(request,slug):
#     #identified_post=Post.objects.get(slug=slug)
#     identified_post=get_object_or_404(Post,slug=slug)
#     return render(request, "blog/post-detail.html",{
#         "post":identified_post,
#         "post_tags":identified_post.tags.all()
#     })
    

class PostdetailView(DetailView):
    template_name="blog/post-detail.html"
    model=Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all() 
        context["comment_form"]=CommentForm()
        return context   