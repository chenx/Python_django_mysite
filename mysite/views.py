from django.http import HttpResponse


def index(request):
    s = """
        Hello world! You're at mysite.<br/>
        <a href="./admin">admin</a><br/>
        <a href="polls">polls</a><br/>
        """
    return HttpResponse(s)
    #return HttpResponse("Hello, world. You're at mysite.. ..")
