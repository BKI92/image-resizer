from django.shortcuts import get_object_or_404, redirect, render

from pictures.forms import PictureForm, ResizeForm
from pictures.handlers import get_image, get_image_size, resize_image
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
    if form.is_valid():
        picture = form.save(commit=False)
        if picture.link:
            picture.image = get_image(picture.link)
        path = picture.image
        picture.width, picture.height = get_image_size(path)
        picture.save()
        return redirect('index')
    return render(request, 'new.html', {'form': form})


def change_image(request, picture_id):
    picture = get_object_or_404(Picture, id=picture_id)
    form = ResizeForm(request.POST or None, files=request.FILES or None,
                      instance=picture, initial={'picture_id': picture_id})
    if form.is_valid():
        changed_picture = form.save(commit=False)
        picture.pk = None
        picture.save()
        picture.width = changed_picture.width
        picture.height = changed_picture.height
        resize_image(picture.image, changed_picture.width,
                     changed_picture.height)
        form.save()
    return render(request, 'resize.html', {'form': form,
                                           'picture': picture})
