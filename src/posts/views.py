from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)		
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

        

	# if request.method == "POST":
	# 	print "title" + request.POST.get("content")
	# 	print request.POST.get("title")
	# 	#Post.objects.create(title=title)

        
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None): #retrieve
    # instance =Post.objects.get(id=20)
    instance =get_object_or_404(Post, id=id)
    context = {
        "title" :instance.title,
        "instance": instance,
        
    }
    return render(request, "post_detail.html", context)

def post_list(request): #list items
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List"
        
    }
    return render(request, "post_list.html", context)
    #    if request.user.is_authenticated():
#        context = {
#            "title": "My User List"
#        }
#        return render(request, "index.html", context)
#    else:
#        context = {
#            "title": "List"
#        }
#        return render(request, "index.html", context)
        
	
def post_update(request, id=None):
    instance =get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)		
        instance.save()
        # message success
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    "title" :instance.title,
    "instance": instance,
    "form" : form,

    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")