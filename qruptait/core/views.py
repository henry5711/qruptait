from django.shortcuts import render
import qrcode
from .models import User
from .models import TypeUser
from .models import Asistence
from django.http import HttpResponse,StreamingHttpResponse
import cv2
from pyzbar.pyzbar import decode



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
    
    
def video_feed(request):
    def generate():
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            decoded_objects = decode(frame)

            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                yield f"data: {data}\n\n"

            # Encuentra y muestra el código QR en la ventana de la cámara
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    points = hull
                num_of_points = len(points)

                for j in range(num_of_points):
                    cv2.line(frame, tuple(points[j]), tuple(points[(j+1) % num_of_points]), (0, 0, 255), 3)

            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')