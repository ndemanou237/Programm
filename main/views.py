from django.shortcuts import render

def page_context(request):
    return render(request, 'context.html')
