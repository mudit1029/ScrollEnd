from django.shortcuts import render
from django.http import JsonResponse
import time
# Create your views here.
def index(request):
	return render(request, "posts/index.html")

def posts(request):
	# Get Start and End Points
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or (start + 9))

	# Generate Lists Of Posts
	posts = []
	for i in range(start, end + 1):
		posts.append(f"Post #{i}")

	# Artificially delay speed of response	
	time.sleep(1)

	# Return Lists Of Posts
	return JsonResponse({
		"posts": posts
		})