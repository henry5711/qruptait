
from django.shortcuts import render
import qrcode
from .models import User
from .models import TypeUser
from .models import Asistence
from django.http import HttpResponse,StreamingHttpResponse
from django.utils import timezone
from reportlab.pdfgen import canvas




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

def createUser(request):
    user=User.objects.create(
        ci=request.POST['ci'],
        name1=request.POST['name1'],
        name2=request.POST['name2'],
        lastname1=request.POST['lastname1'],
        lastname2=request.POST['lastname2'],   
        user_id=request.POST['user_id'],
)
    user.save()
    users=User.objects.all()
    return render(request, "bootstrap/tables.html", {"users": users})


def qr_reader(request):
    return render(request, 'bootstrap/qr_reader.html')


def createAsistence(request,user):
    asistence=Asistence.objects.create(
      user_id=user,
      asistence=timezone.now())
    asistence.save()
    asistences=Asistence.objects.all()
    return render(request, "bootstrap/Asistencias.html", {"asistences": asistences})