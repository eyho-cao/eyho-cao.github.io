from django.shortcuts import render
from contracts.forms import GenerateContract

#Create your views here
def index(request):
    return render(request, 'contracts/index.html')
    
def contractview(request):
    form = GenerateContract()
    if request.method == "POST":
        form = GenerateContract(request.POST)
        if form.is_valid():
             form.save(commit=True)
             return render(request, 'contracts/contracts.html', {'form_data': form.cleaned_data})
        else:
             print('ERROR')
    return render(request, 'contracts/contracts.html', {'form':form})
