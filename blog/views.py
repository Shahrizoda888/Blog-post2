from django.contrib import  messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
#home

    
class home(ListView):
    model=Post
    template_name='home.html'
    




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
@login_required(login_url='login')
def add_post(request):
     if request.method == 'POST':
       title=request.POST.get('title')
       body=request.POST.get('body')


       try:
           messages.success(request, 'Successfully added Post')
           post_model=Post(title=title)
           post_model=Post(body=body)
           post_model.save()
           return  redirect('all_post')
       except:
           messages.error(request, 'Invalid added Post')
           return  redirect('add_post')
     return render(request,'add_post.html')


#delete_post
@login_required(login_url='login')
def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    messages.success(request, 'Successfully deleted Post')
    return redirect('all_post')


#update_post
@login_required(login_url='login')
def update_post(request,pk):
     post=Post.objects.get(id=pk)    #shu
     if request.method == 'POST':
        title=request.POST.get('title')
        try:
            post_model=Post(title=title)
            post_model.save()
            messages.success(request, 'Successfully updated Post')
            return  redirect('all_post')
        except:
            messages.error(request, 'Invalid updated Post')
            return  redirect('all_post',pk)
     return render(request,'update_post.html',{'post':post})


#detailPost

def detail_post(request,pk):
    post=Post.objects.get(id=pk)
    return render(request,'detail_post.html',{'post':post})



    
#logout


def logout(request):
    django_logout(request)
    return redirect('home')


#all_post
@login_required(login_url='login')
def all_post(request):
    post=Post.objects.all().order_by('created_at')
    return render(request,'all_post.html',{'post':post})





