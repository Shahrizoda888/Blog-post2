from django.contrib import  messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
#home

    
class home(ListView):
    model=Post
    template_name='home.html'
    
#register
def register(request):
    
    return render(request,'register.html')


#login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is None :
            return HttpResponse('Invalid login')
        else:
            if user:
                return redirect('all_post')
    return render(request,'login.html')



#add_post
def add_post(request):
     if request.method == 'POST':
       title=request.POST.get('title')


       try:
           messages.success(request, 'Successfully added Post')
           post_model=Post(title=title)
           post_model.save()
           return  redirect('all_post')
       except:
           messages.error(request, 'Invalid added Post')
           return  redirect('add_post')
     return render(request,'add_post.html')


#delete_post
def delete_post(request):
    post=Post.object.get(id=pk)
    post.delete()
    messages.success(request, 'Successfully deleted Post')
    return render(request,'all_post.html')


#update_post
def update_post(request):
     post=Post.object.get(id=pk)
     if request.method == 'POST':
        title=request.POST.get('title')
        try:
            post_model=Post(title=title)
            post_model.save()
            messages.success(request, 'Successfully updated Post')
            return  redirect('all_post')
        except:
            messages.error(request, 'Invalid updated Post')
            return  redirect('all_post.html',pk)
     return render(request,'update_post.html')


#detailPost

class detail_post(DetailView):
    model=Post
    template_name='detail_post.html'
    
#logout
def logout(request):
    logout(request)
    return redirect('home.html')


#all_post
def all_post(request):
    post=Post.objects.all().order_by('-created_at')
    return render(request,'all_post.html')





