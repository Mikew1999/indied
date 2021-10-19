from django.shortcuts import render


# Create your views here.
def index(request):
    ''' Renders home page '''
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = str(request.GET['q'])

    context = {
        'query': query,
    }

    return render(request, "home/index.html", context)
