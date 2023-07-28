from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect, render

# Create your views here.
from .models import User


def register(request: HttpRequest):
    context = {'operating_systems': User.OPERATING_SYSTEMS,
               'hardwares': User.COMP_HARDWARES,
               'recommenders': User.RECOMMENDERS}
    
    if request.method == 'POST':
        tmp = request.POST.dict()
        del tmp['csrfmiddlewaretoken']
        cUser = User(**tmp)
        try:
            User.full_clean(cUser)
        except ValidationError as e:
            context = e.message_dict
            print(context)
        else:
            cUser.save()
            return redirect('stub-page')
        request.POST = type(request.POST)()
    return render(request, 'registration/register.html', context)


def stub_page(request: HttpRequest):
    return render(request, 'registration/stub-page.html')
