from django.shortcuts import render, redirect
from home.models import Music

def home_index(request):
    infoData_sql = Music.objects.all
    context = {
        'Music': infoData_sql
    }
    return render(request,'home/index.html',context)

def cadastrar_music(request):
    if str(request.method) != "post":
        return render(request,'home/cadastrar.html')

    else:
        name = request.post.get('name')
        author = request.post.get('author')
        bpm = request.post.get('bpm')
        tom = request.post.get('tom')
        photos = request.files.get('photos')


    date_to_save = Music.objects.create(
        name=name,
        author = author,
        bpm = bpm,
        tom = tom,
        photos=photos,
    )

    date_to_save.save()

    return redirect('homeindex')

def detalhes(request):
    return render(request,'detalhes')
