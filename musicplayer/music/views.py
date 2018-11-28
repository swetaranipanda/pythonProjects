from django.shortcuts import render
from django.http import HttpResponse
from .models import Album , Song
from django.template import loader
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
     ### Without Template###
    # result = ""
    # for album in all_albums :
    #   result+=album.artist+" - "+album.album_title+"    "
    # return HttpResponse(result)

     ### With Template###
    template=loader.get_template('index.html')
    context = { 'all_albums' : all_albums  }
     # return HttpResponse(template.render(context,request))
    return render(request,'index.html',context)

def details(request,album_id):
      all_albums = Album.objects.all()
      album=all_albums.get(pk=album_id)
      context = {'album' : album}
      return render(request,'details.html',context)
    # return HttpResponse("The AlbumId is : "+ str(album_id))

def favorites(req,album_id):
    all_albums = Album.objects.all()
    album=all_albums.get(pk=album_id)
    try:
        selected_song =album.song_set.get(pk=req.POST['song'])
    except :
        return render(req ,'details.html', {'album' : album,
        'error_msg':'THere is no song with this id'})
    else:
        selected_song.is_favorite = True
        return render(req,'details.html',{'album':album})