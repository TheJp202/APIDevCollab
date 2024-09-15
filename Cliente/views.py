from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente

@api_view(['POST'])
def login_view(request):
    dni = request.data.get('Dni') 
    raw_password = request.data.get('Password')
    cliente = Cliente.objects.filter(Dni=dni).first()    
    if cliente is None:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)

    if check_password(raw_password, cliente.Password):
        request.session['cliente_id'] = cliente.id
        cliente_data = {
            "id": cliente.id,
            "nombre": cliente.Nombre,
            "dni": cliente.Dni,
            "fecha_registro": cliente.FechaRegistro,
        }
        response_data = {"message": "Inicio de sesión exitoso", "cliente": cliente_data}
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
    hashed_password = make_password(raw_password)
    
    if not all([nombre, dni, hashed_password]):
        return JsonResponse({'error': 'Se requieren todos los campos'}, status=400)
    if Cliente.objects.filter(Dni=dni).exists():
        return JsonResponse({'error': 'El DNI ya está en uso'}, status=400)

    cliente = Cliente.objects.create(
        Nombre=nombre,
        Dni=dni,
        Password=hashed_password
    )
    
    if cliente:
        return JsonResponse({'message':'Cliente registrado exitosamente'}, status=201)
    else:
        return JsonResponse({'error': 'Error al crear el cliente'}, status=500)
    

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
            cliente_id = session.get_decoded().get('cliente_id')
            cliente = Cliente.objects.get(id=cliente_id)
            cliente_data = {
                "id": cliente.id,
                "nombre": cliente.Nombre,
                "dni": cliente.Dni,
                "fecha_registro": cliente.FechaRegistro,
            }
            return JsonResponse({'cliente': cliente_data})
        except Session.DoesNotExist:
            return JsonResponse({'error': 'Sesión no encontrada'}, status=404)
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Cookie de sesión no proporcionada'}, status=400)
    
@api_view(['POST'])
def change_password(request):
    dni = request.data.get("Dni")
    raw_old_password = request.data.get("OldPassword")
    raw_new_password = request.data.get("NewPassword")
    cliente = Cliente.objects.filter(Dni=dni).first()    
    if cliente is None:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)
    if not check_password(raw_old_password, cliente.Password):
        return JsonResponse({"error": "Contraseña antigua incorrecta"}, status=400)
    cliente.Password = make_password(raw_new_password)
    cliente.save()
    return JsonResponse({"message": "Contraseña actualizada correctamente"}, status=200)