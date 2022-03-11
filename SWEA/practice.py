print(5)
print(-10)
print(3.14)
print(1000)
print("고카페")
print(5+3)
print(2*8) # print 에서 간단한 사칙연산이 가능하다. 숫자 데이터형식은 지정할 필요 없다. 

print('파이썬')
print("파이썬") # 같은 파이썬이지만, ''는 문자 그대로 출력하라는 뜻이고, ""는 문자를 하나의 기호로 설정해서 계산이 가능하다 
print("파이썬"*2) 

print(5>10)
print(5<10) # 참 거짓을 판별하여 true, false로 출력한다. 
print(not True) # not, 뒤 문장의 부정형으로 출력. false로 출력될것.
# 대,소문자에 주의할 것

# 애완동물 소개
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집"+ animal + "의 이름은 "+ name + "에요")
print(name + "는 "+ str(age) + "살이며," + hobby + "를 아주 좋아해요.")
print(name + "는 어른일까요?"+ str(is_adult))
# str은 문자열이며, str을 제외하고 age, "살이며" 등 콤마로도 문장을 연결할 수있다. 

''' Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력 
출력 문장 
: xx행 열차가 들어오고 있습니다. '''

station = "사당"
station1= "신도림"
station2= "인천공항"

print(str(station) + "행 열차가 들어오고 있습니다.")
print(str(station1) + "행 열차가 들어오고 있습니다.")
print(str(station2) + "행 열차가 들어오고 있습니다.")
