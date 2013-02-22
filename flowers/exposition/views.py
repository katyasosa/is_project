# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from exposition.models import Exposition
from django import forms


class AddExpositionForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=250)


@user_passes_test(lambda u: u in Group.objects.get(name="manager").user_set.all())
def create_exposition(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AddExpositionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            exp = Exposition()
            exp.name = form.data['name']
            exp.description = form.data['description']
            exp.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        form = AddExpositionForm() # An unbound form

    return render(request, 'create_exposition.html', {
        'form': form,
    })