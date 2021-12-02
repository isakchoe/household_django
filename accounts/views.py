
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):  # User model CREATE
    
    # 데이터 받기 
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    username = request.data.get('username')

    if password != password_confirmation:
        return Response({"error": "비밀번호와 비밀번호 확인이 일치하지 않습니다."}, status = status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username = username).exists():
        return Response({"error" : "이미 존재하는 아이디입니다!"}, status = status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)


    # Create User Instance
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        
        # 비밀번호 해싱 및 저장 
        user.set_password(request.data.get('password'))
        user.save()
        return Response({"sign_up" : "success!"}, status=status.HTTP_201_CREATED)

