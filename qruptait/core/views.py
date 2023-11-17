from django.shortcuts import render
import qrcode
from .models import User
from .models import TypeUser
from .models import Asistence
from django.http import HttpResponse

# Create your views here.
# USer---------------------------------------------

def index(request):
    return render(request, "bootstrap/index.html")
def indexUser(request):
    users=User.objects.all()
    return render(request, "bootstrap/tables.html", {"users": users})

# asistence--------------------------------------------
def indexTypeUser(request):
    TypeUser=TypeUser.objects.all()
    return render(request, "Typeuser.html", {"TypeUser": TypeUser})


# asistence---------------------------------------
def indexasistence(request):
    asistences=Asistence.objects.all()
    return render(request, "bootstrap/Asistencias.html", {"asistences": asistences})

def generate_qr(request, data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    response =HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


def formUser(request):
    Ty=TypeUser.objects.all()
    return render(request, "bootstrap/register.html", {"typeUser": Ty})