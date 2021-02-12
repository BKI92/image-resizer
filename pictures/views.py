from datetime import datetime as dt

from django.shortcuts import render, redirect
from requests import get

from pictures.forms import PictureForm
from pictures.models import Picture


def index(request):
    pictures = Picture.objects.all()
    return render(
        request,
        template_name='index.html',
        context={'pictures': pictures}
    )


def new(request):
    form = PictureForm(request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            if post.link:
                content = get(post.link).content
                date = dt.now()
                filename = f'{date}.jpg'
                with open(f'media/images/{filename}', mode='wb') as file:
                    file.write(content)
                post.image = filename
            post.save()
            return redirect('index')
    return render(request, 'new.html', {'form': form})


def change_image(request, image_id):
    pass

