from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage

from .forms import *
from .models import *
from .decorators import *
from .filters import *

# Create your views here.
def testingErrors(Modelname, pk):
    try:
        modelname = Modelname.objects.get(id=pk)
    except:
        modelname = False
    return modelname
    


def home(request):
    posts = Post.objects.order_by("-create_date")
    posts = list(posts)
    post = []
    if str(request)[20:22] in ('uz', 'ru', 'en', 'oz'):
        lan = str(request)[20:22]
    else:
        lan =  'ru'
    for item in posts:
        if item.language == lan:
            post.append(item)
     
    # posts.filter(language=str(request)[20:22])
    print(len(posts))
    postList = []
    for item in post:
        if len(postList) >= 4:
            pass
        else:
            postList.append(item)
    posts = postList
    return render(request, 'insuranceApp/index.html', {'posts':posts})

@logout_required
def user_login(request):
    loginning = True
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        loginning = user

        if user:
            if user.is_active:
                login(request, user)
                return redirect("/")

        else:
            print("SOMEONE TRIED TO LOGIN and FIELD!")
            print(f"Username: {username} and password: {password}")
    return render(request, "login.html",
                    {'loginning':loginning})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/")

def newsList(request):
    posts = Post.objects.order_by("-create_date")
    posts = list(posts)
    post = []
    if str(request)[20:22] in ('uz', 'ru', 'en', 'oz'):
        lan = str(request)[20:22]
    else:
        lan =  'ru'
    for item in posts:
        if item.language == lan:
            post.append(item)
    paginator = Paginator(post, 5)
    
    try:
        print("Hey try ???")
        page_num = request.GET.get('page')
        posts = paginator.page(page_num)
    except:
        print("Hey Except ???")

        posts = paginator.page(1)
    return render(request, 'insuranceApp/news/newsList.html', context={'posts':posts})
def newsView(request, pk):
    post = testingErrors(Post, pk)
    if post != False:
        return render(request, 'insuranceApp/news/newsView.html', context={'post':post})
    else:
        return render(request, '404.html')
@admin_only
def newsCreate(request):
    form = PostForm()
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect("news")
    return render(request, 'insuranceApp/news/newsCreate.html', {'form':form})

@admin_only
def newsUpdate(request, pk):
    post = testingErrors(Post, pk)
    if post != False:    
        form = PostForm(instance=post)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect("news")
        return render(request, 'insuranceApp/news/newsUpdate.html', {'form':form})
    else:
        return render(request, '404.html')
    
        
    

@admin_only
def newsDelete(request, pk):
    post = testingErrors(Post, pk)
    if post != False:
        if request.method == "POST":
            post.delete()
            return redirect("news")
        return render(request, 'insuranceApp/news/newsDelete.html', {'item':post})
    else:
        return render(request, '404.html')

def serviceClassList(request):
    services = ServiceClass.objects.order_by("-create_date")
    return render(request, 'insuranceApp/serviceClass/serviceList.html', context={'services':services})

def serviceClassView(request, pk):
    service = testingErrors(ServiceClass, pk)
    return render(request, 'insuranceApp/serviceClass/serviceView.html', context={'service':service})


@admin_only
def serviceClassCreate(request):
    form = ServiceClassForm()
    if request.method == "POST":
       form = ServiceClassForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect("service")
    return render(request, 'insuranceApp//serviceClass/serviceCreate.html', {'form':form})

@admin_only
def serviceClassUpdate(request, pk):
    service = testingErrors(ServiceClass, pk)
    form = ServiceClassForm(instance=service)
    if request.method == "POST":
       form = ServiceClassForm(data=request.POST, files=request.FILES, instance=service)
       if form.is_valid():
           form.save()
           return redirect("service")
    return render(request, 'insuranceApp/serviceClass/serviceCreate.html', {'form':form})

@admin_only
def serviceClassDelete(request, pk):
    service = testingErrors(ServiceClass, pk)
    if request.method == "POST":
        service.delete()
        return redirect("service")
    return render(request, 'insuranceApp/serviceClass/serviceDelete.html', {'item':service})
def about(request):
    services = ServiceClass.objects.order_by("-create_date")
    postList = []
    for item in services:
        if len(postList) >= 3:
            pass
        else:
            postList.append(item)
    services = postList
    return render(request, "insuranceApp/about.html", {'services':services})

def service(request):
    return render(request, 'insuranceApp/service.html')

def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(request.POST, request.FILES)
        if contactForm.is_valid():
            contactForm.save()
            return redirect("/")
    return render(request, 'insuranceApp/contact.html', {'form':contactForm})

def contactList(request):
    contacts = Contact.objects.all()
    myFiler = LocationFilter(request.GET, queryset=contacts)
    contacts = myFiler.qs
    return render(request, 'insuranceApp/contact/contactList.html', {'contacts':contacts, 'filter':myFiler})

def contactView(request):
    pass


def kodeks(request):
    return render(request, 'insuranceApp/kodeks.html')

def locations(request):
    locations = Location.objects.all()
    myFiler = LocationFilter(request.GET, queryset=locations)
    locations = myFiler.qs
    return render(request, 'insuranceApp/locations/locations.html', {'locations':locations, 'filter':myFiler})

@admin_only
def locationsCreate(request):
    form = LocationForm()
    if request.method == "POST":
       form = LocationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("locations")
    return render(request, 'insuranceApp/locations/locationsCreate.html', {'form':form})
@admin_only
def locationsUpdate(request, pk):
    locations = testingErrors(Location, pk)
    if bool(locations):
        form = LocationForm(instance=locations)
        if request.method == "POST":
            form = LocationForm(data=request.POST, instance=locations)
            if form.is_valid():
                form.save()
                return redirect("locations")
        return render(request, 'insuranceApp/locations/locationsCreate.html', {'form':form})
    else:
        return render(request, '404.html')
@admin_only
def locationsDelete(request, pk):
    locations = testingErrors(Location, pk)
    print(locations.name)
    if bool(locations):
    
        if request.method == "POST":
            locations.delete()
            return redirect("locations")
        return render(request, 'insuranceApp/locations/locationsDelete.html', {'item':locations})
    else:
        return render(request, '404.html')




    