from django.shortcuts import render
from .models import genNum

# Create your views here.
def datos_list(request):
    posts = genNum.objects.all()
    dic = {'valores': posts}
    sumas = []
    for post in posts:
        suma = 0
        suma = post.val1 + post.val3 + post.val4
        sumas.append(suma)
    dic["sumas"] = sumas
    return render(request, 'blog/index.html', dic)
