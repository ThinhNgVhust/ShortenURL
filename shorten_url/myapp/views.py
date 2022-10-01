
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import URLModel
from . import util
# Hash 256 for using to generate shorten url
from hashlib import sha256
# Create your views here.

cache = {} # after this will be replace by using redis sever


def index(request):
    return render(request,"myapp/index.html")

@csrf_exempt
def get_link(request):
    '''
    Do the following step:
        - Check csrf by using csrf_exempt decorator
        - Get long url from form, and check if it a valid url or not?
        If valid:
            - Check it exist in cache? 
                    - If not write to database, save it to cache. redirect to success page
                    - If it is in cache: read from cache and then return 
        else:
            return to error page
    '''
    context = {}
    longURL =request.POST["longURL"]
    if util.valid_url(longURL):
        shortURL = sha256(longURL.encode('utf-8')).hexdigest()[:7]
        if shortURL in cache:
            context = {cache[shortURL]}
        elif shortURL in database:
            read from database
            cache[shortURL] = longURL
            context = {cache[shortURL]}
        else:
            # create one 
            URL
        return render(request,"myapp/success.html",context)
    else:
        return render(request,"myapp/error.html")