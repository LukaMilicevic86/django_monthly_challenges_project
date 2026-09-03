from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string


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

def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        cap_month = month.capitalize()
        month_path = reverse("month_challenge", args = [month])
        list_items += f"<li><a href=\"{month_path}\">{cap_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        return render(request, "challenges/challenge.html")
        # instead of:
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>The URL is not supported!</h1>")