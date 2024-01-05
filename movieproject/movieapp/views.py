from django.shortcuts import render, HttpResponse, redirect
from .models import Movie
from .forms import Movieform

# Create your views here.
def home(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        cate=request.POST.get('cate',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img,cate=cate)
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,id):
    movie=Movie.objects.get(id=id)
    if request.method=='POST':
        movie.delete()
        return redirect('/')
    return render(request,'delete.html',{'movie':movie})

