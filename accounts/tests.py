from warnings import resetwarnings
from django.test import TestCase, Client
import unittest, json
from .models import User

client = Client()


class SignupTest(unittest.TestCase):
    
    def tearDown(self):
        User.objects.all().delete()


    def test_singup_login(self):
        
        # 올바른 회원가입
        signup_data = {
            'username': 'admin',
            'password': 'test1',
            'passwordConfirmation': 'test1'
        }

        response = client.post('/accounts/signup/', json.dumps(signup_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)


        # 올바른 회원 로그인 
        login_data = {
            'username': 'admin',
            'password': 'test1',
        }

        response = client.post('/accounts/login/', json.dumps(login_data), content_type = 'application/json')
        # 200 응답 
        self.assertEqual(response.status_code, 200)


        # 잘못된 로그인 
        false_login_data = {
            'username': 'admin',
            'password': 'test2',
        }

        response = client.post('/accounts/login/', json.dumps(false_login_data), content_type = 'application/json')
        # 400 에러, 잘못된 요청!
        self.assertEqual(response.status_code, 400)



        # 잘못된 회원가입 -- 비밀번호와 비밀번호 확인 불일치 
        false_signup_data = {
            'username': 'admin',
            'password': 'test',
            'passwordConfirmation': 'test1'
        }
        response = client.post('/accounts/signup/', json.dumps(false_signup_data), content_type = 'application/json')
        self.assertEqual(response.json(), {"error": "비밀번호와 비밀번호 확인이 일치하지 않습니다."})
