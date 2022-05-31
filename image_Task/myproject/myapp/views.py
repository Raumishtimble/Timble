from django.shortcuts import render

# Create your views here.
def table_data(request):
    return render(request,"index.html")
