from django.shortcuts import render
from .models import DataSetText
import random
# Create your views here.
def hello(request):
    return render(request, 'hello.html', {'text': DataSetText.objects.get(pk=1)})
def home(request):
    
    if request.GET:
        text = int(request.GET["textBack"])
        text = DataSetText.objects.get(pk=text)
        number = request.GET["buttonEmo"]
        if text:
            text.rating = text.rating + int(number)
            text.save()
    size = DataSetText.objects.count()
    b = random.randint(1, size)
    a = DataSetText.objects.get(pk=b)
    

    return render(request, 'index.html', {'text':a})
