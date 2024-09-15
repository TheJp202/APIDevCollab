from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Encargado

@api_view(['POST'])
def login_view(request):
    dni = request.data.get('Dni') 
    raw_password = request.data.get('Password')
    encargado = Encargado.objects.filter(Dni=dni).first()    
    if encargado is None:
        return JsonResponse({"error": "Encargado no encontrado"}, status=404)

    if check_password(raw_password, encargado.Password):
        request.session['user_id'] = encargado.id
        encargado_data = {
            "id": encargado.id,
            "nombre": encargado.Nombre,
            "dni": encargado.Dni,
            "estacionamiento": encargado.Estacionamiento.id,  
        }
        response_data = {"message": "Inicio de sesión exitoso", "encargado": encargado_data}
        response = JsonResponse(response_data)
        response.set_cookie(
            key='sessionid', 
            value=request.session.session_key, 
            httponly=True,  
            samesite='None',
            secure=True  
        )
        return response
    else:
        return JsonResponse({"error": "Credenciales inválidas"}, status=400)


@api_view(['POST'])
def register_view(request):
    nombre = request.data.get('Nombre')
    dni = request.data.get('Dni')
    raw_password = request.data.get('Password')
    estacionamiento_id = request.data.get('Estacionamiento')  # Asegúrate de pasar este dato
    hashed_password = make_password(raw_password)

    if not all([nombre, dni, hashed_password, estacionamiento_id]):
        return JsonResponse({'error': 'Se requieren todos los campos'}, status=400)
    if Encargado.objects.filter(Dni=dni).exists():
        return JsonResponse({'error': 'El DNI ya está en uso'}, status=400)

    encargado = Encargado.objects.create(
        Nombre=nombre,
        Dni=dni,
        Password=hashed_password,
        Estacionamiento_id=estacionamiento_id
    )
    
    if encargado:
        return JsonResponse({'message': 'Encargado registrado exitosamente'}, status=201)
    else:
        return JsonResponse({'error': 'Error al crear el encargado'}, status=500)


@api_view(['POST'])
def logout_view(request):
    request.session.flush()
    response = Response({'message': 'Cierre de sesión exitoso'})
    response.delete_cookie('sessionid')
    return response


@api_view(['POST'])
def user_data_cookie_view(request):
    sessionid = request.COOKIES.get('sessionid')
    if sessionid:
        try:
            session = Session.objects.get(session_key=sessionid)
            user_id = session.get_decoded().get('user_id')
            encargado = Encargado.objects.get(id=user_id)
            encargado_data = {
                "id": encargado.id,
                "nombre": encargado.Nombre,
                "dni": encargado.Dni,
                "estacionamiento": encargado.Estacionamiento.id,
            }
            return JsonResponse({'encargado': encargado_data})
        except Session.DoesNotExist:
            return JsonResponse({'error': 'Sesión no encontrada'}, status=404)
        except Encargado.DoesNotExist:
            return JsonResponse({'error': 'Encargado no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Cookie de sesión no proporcionada'}, status=400)


@api_view(['POST'])
def change_password(request):
    dni = request.data.get("Dni")
    raw_old_password = request.data.get("OldPassword")
    raw_new_password = request.data.get("NewPassword")
    encargado = Encargado.objects.filter(Dni=dni).first()    
    if encargado is None:
        return JsonResponse({"error": "Encargado no encontrado"}, status=404)
    if not check_password(raw_old_password, encargado.Password):
        return JsonResponse({"error": "Contraseña antigua incorrecta"}, status=400)
    encargado.Password = make_password(raw_new_password)
    encargado.save()
    return JsonResponse({"message": "Contraseña actualizada correctamente"}, status=200)
