from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

# example:
# def january(request):
#   return HttpResponse("Eat no meat for the entire month!")

def monthly_challenge(request, month): # second argument is the placeholder from urls
    challenge_text = None
    if month == "january":
        challenge_text = "Try to walk 5000 steps every day!"
    elif month == "february":
        challenge_text = "Do a good deed every day!"
    elif month == "march":
        challenge_text = "Practice an instrument for 20 minutes a day!"
    else:
          return HttpResponseNotFound("This month isn't supported yet")
    return HttpResponse(challenge_text)