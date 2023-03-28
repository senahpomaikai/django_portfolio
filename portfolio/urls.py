from django.urls import path
from .views import indexPageView, aboutPageView, contactPageView, fpPageView, fpLivePageView, fpMockUpPageView, samsClubPageView, byuMarriottPageView
from .views import linkedInPageView, pinterestPageView, instagramPageView, spotifyPageView, byuInstaPageView
urlpatterns = [
        path('', indexPageView, name="index"),
        path("about/", aboutPageView, name="about"),   
        path("contact/", contactPageView, name="contact"),
        path("freshly-picked/", fpPageView, name="freshly-picked"),
        path("freshly-picked-live", fpLivePageView, name="freshly-picked-live"),
        path("freshly-picked-mockup", fpMockUpPageView, name="freshly-picked-mockup"),
        path("sams-club/", samsClubPageView, name="sams-club"),
        path("byu-marriott/", byuMarriottPageView, name="byu-marriott"),
        path("linkedin/", linkedInPageView, name="linkedin"),
        path("pinterest/", pinterestPageView, name="pinterest"),
        path("instagram/", instagramPageView, name="instagram"),
        path("spotify/", spotifyPageView, name="spotify"),
        path("byu-insta/", byuInstaPageView, name="byu-insta"),


]  
