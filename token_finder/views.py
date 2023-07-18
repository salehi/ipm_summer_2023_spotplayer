from django.shortcuts import render, get_object_or_404

from token_finder.forms import KeyForm
from token_finder.models import SpotPlayer


def find_key(request):
    print(request.method)
    if request.method == "POST":
        form = KeyForm(request.POST)
        print("HERE")
        if form.is_valid():
            print("FORM VALID")
            data = form.cleaned_data
            key = get_object_or_404(
                SpotPlayer,
                national_code=data["national_code"],
                registry_code=data["registry_code"],
            )
            return render(request, 'token_finder/find_key.html', {'KEY': key.key})
        else:
            print(form.errors)
    return render(request, 'token_finder/get.html')
