from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return render(request, 'portfolio/index.html')

def aboutPageView(request) :
    return render(request, 'portfolio/about.html')

def contactPageView(request) :
    return render(request, 'portfolio/contact.html')

def fpPageView(request) :
    return render(request, 'portfolio/freshly-picked.html')

def samsClubPageView(request) :
    return render(request, 'portfolio/sams-club.html')

def byuMarriottPageView(request) :
    return render(request, 'portfolio/byu-marriott.html')

def fpLivePageView(request):
    return redirect('https://freshlypicked.com/')
def fpMockUpPageView(request):
    return redirect('https://www.figma.com/proto/XvLFCsFthnDVcZySF4VHLy/FP-Wireframe-(Copy)?node-id=56-4255&scaling=scale-down&page-id=0%3A1&starting-point-node-id=56%3A4255&show-proto-sidebar=1')
def linkedInPageView(request):
    return redirect('https://www.linkedin.com/in/senah-park-kearl/')
def pinterestPageView(request):
    return redirect('https://www.pinterest.com/senahpomaikai/')
def instagramPageView(request):
    return redirect('https://www.instagram.com/senahpomaikai/')
def spotifyPageView(request):
    return redirect('https://open.spotify.com/user/1249033780?si=TFSPC6ceQp2KzQinOJAVgg&nd=1')
def byuInstaPageView(request):
    return redirect('https://www.instagram.com/byumarriottlife/')