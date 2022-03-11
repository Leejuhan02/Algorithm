food= "john's pie"
print(food)
print("he says, \"this pie looks great\"")
print('''h
e
l
l
o''')

a= "pithon"
b= a.replace("i", "y")
print(a)
print(b)

from random import *
date = str(randrange(4,28))
print("오프라인 스터디 모임 날짜는 매월 %s일로 선정되었습니다." % date) 

url = "https://google.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")] #[0:4]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

password2= my_str[:3] + "6" + "1" + "!"
print(password2)
