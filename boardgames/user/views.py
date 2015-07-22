from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def home(request):
	return render(request, "user/home.html")
