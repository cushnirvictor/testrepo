a,b,c,d = int(input('a= ')), int(input('b= ')), int(input('c= ')), int(input('d= '))
if a<=b and c<=d and a<=10 and b<=10 and c<=10 and d<=10:
  for j in range (c,d+1):
      print ('\t',j, end='')
  for i in range (a,b+1):
    print ('\n', i, end='')
    for j in range (c,d+1):
      print ('\t',j*i, end='')
#####################################################
s,a = 0,''
while a!=0:
  a=int(input('a= '))
  s+=a
  print(s)
print(s)
#####################################################
a=int(input('a= '))
b=int(input('b= '))
s=0
while a<=b:
  print(s+a)
  s+=a
  a+=1
print('����� ����� ��������� �� a �� b �����:', s)
#####################################################
i=''
n=int(input())
k=('*'*n)
while i<=k:
  i+='*'
  print(i)
i = ''
n = int(input())
while n:
  i += '*'
  n -= 1
  print(i)

n=int(input())
while 4<n<55:
  n+=2
  print(n, end=' ')

n=5
while n<55:
  if n%2==1:
    print(n, end=' ')
  n+=1
#####################################################
n=int(input())
l=n%1000
f=(n-l)/1000
sl=(l//100)+((l%100)//10)+(((l%100)%10)%10)
sf=(f//100)+((f%100)//10)+(((f%100)%10)%10)
if sl==sf:
  print("����������")
else:
  print("�������")
#####################################################
n=int(input())
a=str(' �����������')
if n<0 or n>1000: 
  print()
elif 10<n%100<15 or 10<n<15:
  b='��'
elif n==1 or n%10==1: 
  b=''
elif 1<n%10<5 or 1<n%100<5:
  b='�'
else:
  b='��'
print(str(n)+ a+b)

a,b,c=int(input()), int(input('b= ')), int(input('c= '))
if a>=b<=c and a>=c:
  max=a; min=b; med=((a+b+c)-(max+min))
elif a>=c<=b and a>=b: 
  max=a; min=c; med=((a+b+c)-(max+min))  
elif b>=a<=c and b>=c: 
  max=b; min=a; med=((a+b+c)-(max+min))
elif b>=c<=a and b>=a: 
  max=b; min=c; med=((a+b+c)-(max+min))
elif c>=a<=b and c>=b: 
  max=c; min=a; med=((a+b+c)-(max+min))
elif c>=b<=a and c>=a: 
  max=c; min=b; med=((a+b+c)-(max+min))
print(max, min, med, sep="\n")'''

'''f=input("����� ������: ")
if f=='����':
  r=float(input("������ �����: "))
  print(3.14*(r**2))
elif f=='�������������':
  a=float(input("a= "))
  b=float(input("b= "))
  print(a*b)
elif f=='�����������':
  a=float(input("a= "))
  b=float(input("b= "))
  c=float(input("c= "))
  print((((a+b+c)/2)*((-a+b+c)/2)*((a-b+c)/2)*((a+b-c)/2))**0.5)
else:
  print('���������� ������!!!')'''
 
"""a=float(input())
b=float(input())
c=str(input())
if c=='+':
  print(a+b)
elif c=='-':
  print(a-b)
elif c=='*':
  print(a*b)
elif c=='pow':
  print(a**b)
elif b!=0 and c=='/':
  print(a/b)
elif b!=0 and c=='mod':
  print(a%b)
elif b!=0 and c=='div':
  print(a//b)
else:
  print('������� �� 0!')
  
a=int(input('a= '))
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
  a=(True)
else:
  a=(False)
print(a)
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
#p=((a+b+c)/2)
S=(((a+b+c)/2)*((-a+b+c)/2)*((a-b+c)/2)*((a+b-c)/2))**0.5
#S=16**0.5
print('S=', S)
print ('1' < 'b')
A=int(input('������� ����� ������ ��� �� 1900 �� 3000: '))
if A<=1900 or A>=3000:
  print('�� 1900 �� 3000')
elif A%4 == 0 and A%100 != 0 or A%400 == 0:
  print('����������')
else:
  print('�������')


a=(a+(H*60)+M)
print(a//60,a%60, sep='\n')
a = 5
y = 10
print (y >= (2 * a))
print (a < y)
print (y >= (2 * a) and a < y)
print(y > a * a)
print(False or True)
print(y > a * a or y >= (2 * a) and a < y)
a = True
b = False
print(a and b or not a and not b)
a=int(input('a= '))
b=int(input('b= '))
if b == 0:
  print('�� ���� ����� �� ����')
else:
  print('��� ��� �������', a/b)
A=int(input('����������� ����� ���: '))
B=int(input('������������ ����� ���: '))
H=int(input('��� ����: '))
if H<A:
  print('�������� ����� ���')
elif H>B:
  print('��� ����')
elif H==B or H==A:
  print('������� ���� �������')
else:
  print('������� ��� ��� ���� �� ������ �� ������')"""