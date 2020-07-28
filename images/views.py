from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Image
from .forms import ImageCreateForm

def image_create_formview(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image Added Successfully")

            return redirect(new_item.get_absolute_url())

    else:
        form = ImageCreateForm(data=request.GET)
        return render(request, 
                      "images/image/create.html", 
                      {
                          "form": form,
                          "section": "images"})               

def image_detail(request, id, slug=None):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(request, 
                  "images/image/detail.html", 
                  {"image": image})   