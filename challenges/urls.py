from django.urls import path
from . import views     # dot means import from the same folder

urlpatterns = [
    # example: path("january", views.january) -> first argument is an URL, second one is the pointer to a view
    path("<month>", views.monthly_challenge) # placeholder within <> can be anything
]
