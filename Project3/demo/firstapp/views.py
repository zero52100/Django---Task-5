from django.shortcuts import render,redirect
from .forms import FirstModelForm
from .models import FirstModel

def add_first_model(request):
    if request.method == 'POST':
        form = FirstModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_first_models')
    else:
        form = FirstModelForm()
    return render(request, 'first_app/add_first_model.html', {'form': form})



def list_first_models(request):
    first_models = FirstModel.objects.all()
    return render(request, 'first_app/list_first_models.html', {'first_models': first_models})
