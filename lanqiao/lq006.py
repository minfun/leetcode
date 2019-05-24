# -*-encoding:utf8-*-
import random
num_list = [str(i) for i in range(10)]
verify_code = ''.join(random.sample(num_list, 6))
print('您的登录验证码为 {}'.format(verify_code))
username = str(input('请输入用户名:'))
password = str(input('请输入密码:'))
input_code = str(input('登录验证码:'))
with open('./userpass.txt', 'r') as f:
    real_user, real_pass = f.read().split(',')
if username == real_user and password == real_pass and input_code == verify_code:
    print('身份验证通过，欢迎登录!')
else:
    print('身份验证失败!')
