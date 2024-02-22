from django.shortcuts import render,redirect
from .models import URL
import random
import string

def url_shortener(request):
    if request.method == 'POST':
        long_url=request.POST['long_url']
        short_url = generate_short_url()
        URL.objects.create(long_url=long_url,short_url=short_url)
        return  render(request,'url_shortener.html',{'short_url':short_url})
    return render(request,'url_shortener.html')


def redirect_to_original(request, short_url):
    url = URL.objects.get(short_url=short_url)
    return redirect(url.long_url)
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    complete_url = f'www.{short_url}.com'
    return complete_url
