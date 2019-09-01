from django.http import HttpResponse


# Create your views here.
def home(request):
    # return render(request, 'home.html', {'text': '<BR><BR>Hello<BR><BR>World<BR><BR>'})
    return HttpResponse('<H1><BR><BR><BR><BR>Hello, World!<BR><BR></H1>')
