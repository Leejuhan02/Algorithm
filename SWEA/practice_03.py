from turtle import hideturtle


print("="*50)
print("hello")
print("="*50)

a= "life is too short"
len(a)
print(len(a))

print(a[3])
print(a[-3])

name = "John"
name2 = "Dwayne"
print("hello %s, long time no see." % name)

print("I ate {0} apple".format(4))

print("Hello {0}, long time no see. {1}, you too. ".format(name,name2))

b= "so"
c= "we"
d= "need"
e= "to"
f= "study."
print("{0}. {1}, {2} {3} {4} {5}".format(a,b,c,d,e,f)) # {~}의 숫자는 .format 뒤의 대입하는 값의 좌표를 의미한다. .format(a,b,c,d,e,f)인 경우, a=0, b=1인 식으로 좌표를 갖게 된다. 

print("Nice to meet you {name3}.".format(name3="steve")) #format에서 정의도 가능하다
print("Nice to meet you too, {name}.".format(name="saul")) #format에서 초기화, 재정의도 가능하다. 

print("{surprise:!<15}".format(surprise="Oh my god"))
print("{surprise:!>15}".format(surprise="Oh my god"))
print("{surprise:!^15}".format(surprise="Oh my god"))

print("{pai}".format(pai="3.1415926535897932384626433832795028"))
print("{pai:0.5f}".format(pai=3.1415926535897932384626433832795028)) # 위 코드와 같이 따옴표를 사용하면 {pai:0.5f} 가 동작하지 않는다. f를 사용하려면 실수가 필요하다.
print("{pai:=^20.5f}".format(pai=3.1415926535897932384626433832795028)) 

print(f"My name is {name}, and this is my friend {name2}.") #f 를 문장 앞에 붙여 format 할 수 있다.

name0= "Bruce"
print(f"Hi, Mr.{name0}" )

num= 3
word= str("weeks")
print(f"I ate this {num+1}days ago.")
print(f"I ate this {num,word} ago.") # 보류. 원인 찾기.

count= d.count('e')
print(count)

p="aappaac"
print(p.strip('pa')) # strip은 괄호 안의 인자를 제거한다. ''로 감싸져야한다. ''안의 적혀있는 모든 개별의 인자들을 제거한다. =c

from math import * 
from random import *

rannum= "1234567890"
random= str(randrange(0,10))
print(random)
stripnum= str(rannum.strip(random))
print(stripnum)
# 커밋 실험