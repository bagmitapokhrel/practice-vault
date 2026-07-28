from django.shortcuts import render, redirect
from .forms import PackageForm, DestinationForm
from django.contrib import messages

# Create your views here.
def PackageCreateView(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Package created successfully!")
            return redirect('package_create')
        else:
            messages.error(request, "There was an error creating the package. Please check the form for errors.")
            return render(request, 'adminpage/package_form.html', {'form': form})
    else:
        form = PackageForm()
    
    return render(request, 'adminpage/package_form.html', {'form': form})

def DestinationCreateView(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination created successfully!")
            return redirect('destination_create')
        else:
            messages.error(request, "There was an error creating the destination. Please check the form for errors.")
            return render(request, 'adminpage/destination_form.html', {'form': form})
    else:
        form = DestinationForm()
    
    return render(request, 'adminpage/destination_form.html', {'form': form})