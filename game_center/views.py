from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Game Center Champion"}
    return render(request,'game_center/index.html', context_dict)

def about(request):
    return render(request,'game_center/about.html')