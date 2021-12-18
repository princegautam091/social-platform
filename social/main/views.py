from django.http.response import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import *
from django.db.models import Q

#register form
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required(login_url='login')
def main_home(request):
    users = User.objects.exclude(username__in=[request.user.username, 'admin'])
    followers_list = [u.follow_user.username for u in request.user.customer.followers_list]
    print("followers list:\n{}".format(followers_list))
    return render(request, 'main/home.html', {'users': users, 'followers_list': followers_list})

#add connection
def user_follow(request, follow_username):
    if request.user.is_authenticated:
        current_user = request.user
        follow_user = User.objects.get(username=follow_username)
        follow = Follow.objects.create(user=current_user, follow_user=follow_user)
        follow.save()
        return redirect('main-home')
    else:
        return redirect('login')

#profile update form
@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.customer)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.customer)

    return render(request, 'main/profile.html', {'uform': uform, 'pform': pform})

#try to using this method but still not working
'''
@login_required
def searchposts(request):
    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions =Customer.objects.filter(username_icontains=search)

        name = request.GET.get('name')
        query = Customer.object.create(query=search, user_name=name)
        query.save()

    return render(request, 'main/search.html',{
        'questions': questions,
    })


'''
#search users
@login_required
def searchposts(request):
    if 'username' in request.POST and request.POST["username"]:
        search_term = request.POST.get("username")
        searched_users = Customer.search(search_term)
        message = f"{search_term}"

        return render(request, 'main/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'main/search.html',{"message":message})

    
        

#this function only work for posting your file in storage folder
@login_required
def uploadpost(request):
    if request.user.is_authenticated:
        try:
            if request.method == 'POST':
                profile = Customer.objects.get(user=request.user)
                postdesc = request.POST['desc']
                file = request.FILES['file']
                posts = Post.objects.create(post=file, profileuser=profile, user=request.user)
                for files in posts:
                    variable= files
            return render(request, 'main/upload-post.html',{'files':variable})
        except:
            messages= 'pls put some data in post field'
            return render(request, 'main/upload-post.html',{'error_messages':messages})
        
   
