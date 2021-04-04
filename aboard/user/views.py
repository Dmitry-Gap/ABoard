from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate, decorators as dec
from user.forms import UserForm, UserRegistrationForm


def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home")
    context = {
        "form": UserForm(),
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    request.META.get("HTTP_REFERER")
                    if request.META.get("HTTP_REFERER") is not None
                    else "/home/"
                )
        else:
            context.update(form=form)
    return render(request, "login.html", context)


@dec.login_required(login_url="/user/login/")
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/home/")


# def regist_page(request):
    # context = {}
    # return render(request, "registration.html", context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})

