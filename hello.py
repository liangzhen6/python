# a = int(input('place enter a number a='))
# b = int(input('place enter a number b='))
# if a+b>50:
# 	print(a-b)
# else:
# 	print(a+b)	

# L = ['Bart', 'Lisa', 'Adam']
# for a in L:
#     print('hello,',a+'!')
# x = '2'
# if x :
# 	print('sb')
# name = input('place enter your name:')
# weight  = input('place enter you weight(Kg):')
# print(name,'weight:'+weight+'kg')
# height = input('palce enter your height(m):')
# print(name,'height:'+height+'m')
# w = float(weight)
# h = float(height)
# print(w,h)
# bmi = w/(h*h)
# print(bmi)
# if   bmi>=32:
# 	print('严重肥胖')
# elif bmi>=28:
# 	print('肥胖')
# elif bmi>=25:
# 	print('过重') 
# elif bmi>=18.5:
# 	print('正常')
# else:
# 	print('过轻')
# 	




# n = input('palce enter a number:')
# sum = 0
# for x in range(int(n)):
# 	sum = sum + x
# print(sum)

# ad = 0
# num = int(n)
# if num%2==0:
# 	num = num-1

# while num>0:
# 	ad = ad + num
# 	num = num - 2
# print('奇数和:',ad)

# def my_abs(x):
# 	if x>0:
# 		return x
# 	else:
# 		return -x		

# print(my_abs(int(n)))




# js = 0
# en = int(n)
# if en>0:
# 	js = 1;
# count = 0
# if en%2==0:
# 	count = en/2
# else:
# 	count = int(en/2) + 1

# for x in range(count+1):
# 	js = js + (x*2-1)
# 	print('hello',js,x)
# print(js,count,n)



# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('传的参数有误')
# 	if x>0:
# 		return x, x
# 	else:
# 		return -x, x

# n = input('请输入一个数字:')
# print(my_abs(float(n)))










# import math

# def quadratic(a,b,c):

#     if not isinstance(a,(int,float)):
#     	raise TypeError('Invalid input parameter')
#     if not isinstance(b,(int,float)):
#     	raise TypeError('Invalid input parameter')
#     if not isinstance(c,(int,float)):
#     	raise TypeError('Invalid input parameter')

#     d = b*b-4*a*c
#     if a==0:
#     	if b==0:
#     		return '这不是一个方程'
#     	else:
#     		return -c/b
#     else:
#         if d < 0:
#             # raise TypeError('此方程无解')
#             return '此方程无解'
#         elif d==0:
#             return -b/(2*a)
#         else:
#     	    x1 = (-b + math.sqrt(d))/(2*a)
#     	    x2 = (-b - math.sqrt(d))/(2*a)
#     	    return x1, x2

# a = input('请输入一个数字a:')
# b = input('请输入一个数字b:')
# c = input('请输入一个数字c:')


# print('方程的根是',quadratic(float(a),float(b),float(c)))




# i=0
# def move(n, a, b, c):
# 	global i
# 	if n == 1:
# 		i+=1
# 		print('move', a, '--->', c, '移动次数:', i)
# 		return
# 	move(n-1, a, c, b)
# 	i+=1
# 	print('move', a, '--->', c, '移动次数:', i)
# 	move(n-1, b, a, c)


# n = int(input('请输入汉诺塔的层数:'))

# move(n,'A','B','C')



# L = []
# n = 1
# while n<=99:
# 	L.append(n)
# 	n+=2
# print(L)



# def power(x, n=2):
# 	s = 1
# 	while n > 0:
# 		n = n - 1
# 		s = s * x
# 	return s

# print(power(5,3))
# 
# 


# def add_end(L = None):
# 	if L is None:
# 		L = []
# 	L.append('END')
# 	return L

# print(add_end())
# print(add_end())


# def calc(*numbers):
# 	sum = 0
# 	for x in numbers:
# 		sum = sum + x*x
# 	return sum

# print(calc(*[1,3,5,7]))
# 



# def persion(name,age,**kw):
# 	print('name:',name,'age:',age,'other:',kw)


# persion('zs',18,city = 'bengjin',sex = 'nan')


# def persion(name,age,*ed,*,city,job = 'hehe'):
# 	print(name, age,ed,city, job)



# persion('sz',22,1,2,3,city = 'beijing')



from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = 'liangz@szmn.com.cn'#input('From: ')
password = 'Lzhen520'#input('Password: ')
# 输入收件人地址:
to_addr = 'liangz@szmn.com.cn'#input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.exmail.qq.com'#input('SMTP server: ')

import smtplib

server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

