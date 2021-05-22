from django.shortcuts import render
import numpy as np
import pandas as pd
import random
from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):

    with open('data/entries.txt') as f:
        lines = f.read().splitlines()

    options = random.sample(lines, 25)
    options = [options[i:i + 5] for i in range(0, len(options), 5)]

    context = {
        "options": options
    }

    print(context)
    return render(request, 'index.html', context=context)