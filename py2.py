def change_number(number):
    hiding_number=number.replace(number[3:7],'*'*4)
    print(hiding_number)
change_number(input("请输入你的手机号码："))

a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))

a=111
isinstance(a,int)

str1='hello world!'
str2="python runoob"
len('hkjalsf')

a=2**3**2/4
print(a)

pi=3.1415926535897932384626
r=2
a=pi*r**2
print(a)

for a in range(5,10,3):
    print(a)

for n in range(11,6):
    print(n)

score=int(input("请输入学生成绩："))
if 90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
else:
    print("F")

a=0
sum=0
while a<100:
    a=a+1
    sum=sum+a
print(sum)

print(2)
n=3
count=1
is_prime==True
while n<=30:
    if n%2==0:
        n+=1
        continue
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n)
        try:
            count+=1
            if count==6:
                break
        except:
            print("catch an error")
    else:
        is_prime=True
    n+=1


def f(local_a):
    local_b="This is also."
    print(local_a)
    print(local_b)
f("This is a local vatiable.")
print(local_a)
print(local_b)

def f(a):
    print(a)
f("haksdsdas")
print(fsanf)

def max_of(x,y):
    if x>y:
        return x
    else:
        return y
print(max_of(1,10))

max=lambda x,y:x if x>y else y
print(max(1,10))


def f(str):
    last=""
    length=len(str)
    for i in range(length-1,-1,-1):
        last+=str[i]
    return last
print(f(input("请输入需要置换的字段：")))

number=[1,2,3]
print(6 in number)
print(len(input("请输入你的序列号：")))

print(list.sort(input("请输入你的数组："))) #这行代码不对

number=[1,243,63424,2]
number.sort()
print(number)

def mas(a):
    return a[1]
random=[(1,2),(4,5),(3,1),(4,9)]
random.sort(key=mas)
print(random)

color=["yellow","red","black","white"]
print(tuple(color))

jd="Hello,Python3!"
print(jd[7::2]

print(r'i\'m means a new line.')


area=3.1415**2
print('This area of circle is %.5f'%area)


balls={"black":5,"red":4,"white":6,"green":7,"gold":9}
print(len(balls))
print(balls.get("green"))
print(balls.keys())
print(balls.values())
print(balls.items())

balls={"black":5,"red":4,"white":6,"green":7,"gold":9}
print(balls["black"])
balls["white"]=3
print(balls)

a=[(1),(1,2,3,4,5),{"w":90,"l":95}]
b=a[1]
print(b[:2])
a[2]["l"]=96
print(a)

c={1,2,3,4,5}
d={2,4,6,8,10}
print(c.symmetric_difference(d))
print(c&d)
print(c^d)
print(c-d)
print(c|d)
print(c|d-c&d)

try:
    dividend=int(input("Enter the divideng"))
except ValueError:
    print("The dividend is not a number.")
try:
    divisor=int(input("Enter the divisor"))
except ValueError:
    print("The divisor is not a number.")
try:
    result=dividend/divisor
except ZeroDivisionError:
    print("Divison by zero.")
else:
    print("We get the result:%.2f"%result)

profiles={}
a=[("name",str),("age",int),("height",float)]
for a_name,a_type in a:
    value=input("Please enter your %s:"%a_name)
    valid_value=a_type(value)
    print("We have got your %s.\n"%a_name)
    profiles[a_name]=valid_value

报错修改：

profiles={}
a=[("name",str),("age",int),("height",float)]
for a_name,a_type in a:
    valid_value=None
    while valid_value is None:
        try:
            value=input("Please enter your %s:"%a_name)
            valid_value=a_type(value)
        except ValueError:
            print("cannot convert %s'%s'to type %s.""Please try again.\n"%(a_name,value,a_type.__name__))
        else:
        print("We have got your %s.\n"%a_name)
    profiles[a_name]=valid_value

for i in range(4,10):
    print(i)

from functools import reduce
sum=reduce(lambda x,y:x+y,range(10))
print(sum)

even_list=list(filter(lambda x:x%2==0,range(10)))
print(even_list)