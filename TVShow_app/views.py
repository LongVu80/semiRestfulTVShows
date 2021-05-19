from django.shortcuts import render, redirect
from .models import *

#View all shows
def allShows(request):
    context = {
        'allShows': Shows.objects.all().values()
    }
    return render(request, 'allShows.html', context)

def createShow(request):
    return render(request, "createShow.html")

def addShow(request):
    print(request.POST)
    Shows.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date']
    )
    return redirect('/')

def editShow(request, show_id):
    edit = Shows.objects.get(id=show_id)
    context = {
        'editShow': edit
    }
    return render(request, 'editShow.html', context)

def updateShow(request, show_id):
    toUpdate = Shows.objects.get(id=show_id)
    toUpdate.title = request.POST['title']
    toUpdate.network = request.POST['network']
    toUpdate.description = request.POST['description']
    toUpdate.release_date = request.POST['release_date']
    toUpdate.save()

    return redirect(f'/displayShow/{show_id}')

def deleteShow(request, show_id):
    Shows.objects.get(id=show_id).delete()

    return redirect('/')

def displayShow(request, show_id):
    context = {
        'show': Shows.objects.get(id=show_id)
    }
    return render(request, "displayShow.html", context)
