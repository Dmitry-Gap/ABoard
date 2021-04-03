from django.shortcuts import render, HttpResponseRedirect
from home.forms import QuickContactForm, QuickForm


def home_page(request):
    context = {}
    return render(request, "home.html", context)

# def about_page(request):
#     context = {}
#     return render(request, "about.html", context)

# def contact_page(request):
#     context = {}
#     return render(request, "contact.html", context)

def post_page(request):
    context = {}
    return render(request, "singl-post.html", context)

def contact_page(request):
    context = {
        "form": QuickContactForm(),
    }
    if request.method == "POST":
        form = QuickContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/hposts/")
        else:
            context.update(form=form)
    return render(request, "contact.html", context)