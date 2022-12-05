from django.shortcuts import render, redirect
from .forms import DweetForm, RegisterForm
from .models import Profile
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
# Create your views here.
# dwitter/views.py
# dwitter/views.py
from django.shortcuts import render
from .models import Profile, Dweet


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect(reverse("dwitter:login"))
    else:
        form = DweetForm()  # instead we can delete both statment
        # and use form=DweetForm(request.POST or None)

        if request.method == "POST":

            form = DweetForm(request.POST)
            if form.is_valid():

                """A key point here  is using the commit kw.
                commit logic tells django to either reflect
                changes made so far to database or not,
                in our case we tell django to wait untill we
                assign the user to Dweet model
                so we say commit=False

                had this been not the case , it would have
                thrown a -NOT NULL CONSTRAINTS EXCEPTION- ;as
                User is NOT DEFINED in Dweet yet
                """
                # """
                dweet = form.save(commit=False)  # don't commit to DB yet
                # still new data to be assigned
                dweet.user = request.user  # (user_id ->[User] in Dweet model)
                dweet.save()

                # redirect using view name from url.py
                return redirect("dwitter:dashboard")

                # redirect using relative hard-coded url
                # / means '' empty relative url
                # because the url of dashboard is '' in the path urls.py
                # if the dashboard was for example path('dashboard/',view ... )
                # the rediret would then be return redirect('/dashboard/)
                """return redirect('/')"""

                # """
                """
                body=request.POST.get('body')
                d=Dweet(user= request.user,body=body)
                d.save()
                """
                form = DweetForm()

        followed_dweets = Dweet.objects.filter(
            user__profile__in=request.user.profile.follows.all()
        ).order_by("-created_at")

        return render(
            request, "dwitter/dashboard.html", {"form": form, "dweets": followed_dweets}
        )


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, "profile"):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

        # this is a method of redirects
        # it uses a url name , and passes arguments
        # but becarefull to namespace

        return redirect("dwitter:profile", pk=pk)

        # another method
        """return redirect(f"/profile/{pk}",pk = pk)"""

        # below we use Model Redirect mehtod through
        # get_absolute_url() method in profile model
        # but cant be used here because it will always redirect to the logged in user only
        """return redirect(profile)"""

    return render(request, "dwitter/profile.html", {"profile": profile})


def register(request):

    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            new_user = registerForm.save()
            new_user.save()
            login(request, new_user)
            messages.add_message(
                request, messages.SUCCESS, f"{new_user.username}\tSuccessfully Created!"
            )
            return redirect("dwitter:dashboard")
        messages.error(request, "Invalid Information, Rgistration Faild")
        return redirect("dwitter:register")

    registerForm = RegisterForm()
    return render(
        request, "register.html", {"form": registerForm, "errors": registerForm.errors}
    )


# just to customize logout page
def myLogout(request):
    logout(request)
    return render(request, "dwitter/logout.html")


# #overide password_reset_done view
# class  password_reset_done(auth_views.PasswordResetDoneView):
#     template_name="registration/password_reset_done.html"

# #extends password_reset view
# class password_reset(auth_views.PasswordResetView):
#     print("this is an overriden view")
#     template_name="registration/password_reset_form.html"
#     success_url=reverse_lazy("dwitter:password_reset_done")
    
    
    

# we can use a RedirectView Class-based redirection
from django.views.generic.base import RedirectView


class goToDashboard(RedirectView):
    url = "/"
