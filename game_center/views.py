from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Game Center Champion"}
    return render(request,'game_center/index.html', context_dict)
