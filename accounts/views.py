
from rest_framework import serializers, status
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['POST'])
def signup(request):  # User model CREATE
    
    # 데이터 받기 
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)


    # Create User Instance
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        

# @require_http_methods(['GET', 'POST'])
# def update(request):
#     # 회원정보 수정은, 타인이 아닌 본인에 의해서만 가능
#     if request.user.is_authenticated:
#         user = request.user
#         if request.method == 'POST':
#             form = CustomUserChangeForm(request.POST, instance=user)
#             if form.is_valid():
#                 user = form.save()
#                 return redirect('movies:home')
#         else:
#             form = CustomUserChangeForm(instance=user)
        
#         context = {
#             'form': form
#         }
#     return render(request, 'accounts/update.html', context)


# @login_required
# @require_http_methods(['GET', 'POST'])
# def change_password(request):
#     user = request.user
#     if request.method == 'POST':
#         form = PasswordChangeForm(user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('movies:home')
#     else:
#         form = PasswordChangeForm(user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/change_password.html', context)


# @require_POST
# def delete(request):
#     # 회원정보 삭제는, 타인이 아닌 본인에 의해서만 가능
#     user = request.user
#     if user.is_authenticated:
#         user.delete()
#     return redirect('movies:home')


# @require_http_methods(['GET', 'POST'])
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('movies:home')

#     if request.method == 'POST':
#         # AuthenticationForm => 일반 Form
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():  # authenticate(id, pw) => 맞으면, user 객체를 반환
#             user = form.get_user()
#             auth_login(request, user)  # auth_login() => session & cookie 세팅
#             return redirect(request.GET.get('next') or 'movies:home')
#     else:
#         form = AuthenticationForm()

#     context = {'form': form,}
#     return render(request, 'accounts/login.html', context)
    

# def logout(request):
#     if request.user.is_authenticated:
#         auth_logout(request)  # auth_logout => session, cookie 날리기
#     return redirect('movies:home')

