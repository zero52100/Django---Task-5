from django.shortcuts import render,redirect
from .forms import SecondModelForm
from .models import SecondModel

def add_second_model(request):
    if request.method == 'POST':
        form = SecondModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_second_models')
    else:
        form = SecondModelForm()
    return render(request, 'second_app/add_second_model.html', {'form': form})



def list_second_models(request):
    second_models = SecondModel.objects.all()
    return render(request, 'second_app/list_second_models.html', {'second_models': second_models})
