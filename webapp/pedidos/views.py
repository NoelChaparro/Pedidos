from django.shortcuts import render


def home(request):
	context = {
		"title": "Home",
		"angular": False
	}
	return render(request, 'home.html', context)