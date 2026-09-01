from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Try to walk 5000 steps every day!",
    "february": "Do a good deed every day!",
    "march": "Practice an instrument for 20 minutes a day!",
    "april": "Listen to a new song every day!",
    "may": "Cook lunch at home every weekday!",
    "june": "Meditate at least 30 minutes every evening!",
    "july": "Visit a new place nearby every weekend!",
    "august": "Do a stretch session every morning!",
    "september": "Eat a fruit and a vegetable every day!",
    "october": "Talk to someone from your family every weekend!",
    "novebmber": "Take a cold shower every evening!",
    "december": "Go for a 15 km bike ride every weekend!"
}

# Create your views here.

# example:
# def january(request):
#   return HttpResponse("Eat no meat for the entire month!")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # as of Python 3.6, returns the list of all the keys sorted in the ascending numbered order

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month): # second argument is the placeholder from urls
    try:
        challenge_text = monthly_challenges[month] # uses the argument to access the corresponding dictionary key and return its value
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("The URL is not supported!")