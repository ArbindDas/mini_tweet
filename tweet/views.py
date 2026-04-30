from django.shortcuts import render

# Create your views here.


def tweetindex(request):
    return render (request, 'tweets/tweetindex.html')