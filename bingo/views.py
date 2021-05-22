from django.shortcuts import render
import random
from .forms import CardNameForm

def index(request):

    if request.method == 'POST':
        form = CardNameForm(request.POST)
        if form.is_valid():
            seed = form.cleaned_data['card_name']
            random.seed(seed)
    else:
        form = CardNameForm()

    with open('data/entries.txt') as f:
        lines = f.read().splitlines()

    options = random.sample(lines, 25)
    options = [options[i:i + 5] for i in range(0, len(options), 5)]

    context = {
        "options": options,
        "form": form
    }

    print(context)
    return render(request, 'index.html', context=context)