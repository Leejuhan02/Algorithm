print(1+1)
print(3-2)
print(6/3)

print(2**3) # **는 제곱
print(5%3) # %는 나누고 난 나머지 
print(5//3) # 몫

print((10/3)>(5)) # 한번 계산된 값을 대조하여 True False.
print(3 == 3)

print((3>0) and (3<5)) # and 앞뒤로 둘다 참이면, True
print((3>0) & (3<5)) # &는 and와 같음

print(5>4>3) #연속되는 수도 가능
#수식
print(2+3*4) #14
number= 2+3*4
print(number)

#초기화, 재정의 
number=number+3
print(number) # 17

number += 3 # 기존의 것의 +3 
# 이전에 초기화한 값 유지
print(number) # 20
# 이런 식으로 = 앞에 사칙연산 기호 *+-/ 등을 넣어 계산 가능함

print(abs(-10)) # abs는 의 값을 절대값으로 나타낸다.
print(pow(4,2)) # pow는 뒤 값을 (a,b)라고 하였을 때, a^b로 계산한다. 
print(max(5,12)) # max는 뒤 문자열 중 가장 큰 값을 출력한다. 
print(min(1,2,3,4,5,6)) # min은 뒤 숫자열 중 가장 낮을 값을 출력한다. 
print(round(3.14)) # round는 뒤 숫자를 반올림하여 출력한다. 이 경우 3이 출력된다. 

from math import * # math 파일의 요소를 임포트하여 사용한다. 
print(floor(4.99)) # 위 파일을 임포트하여 floor을 사용할 수 있다. 정수 뒷부분을 내린다. 이경우 출력되는 값은 4
print(ceil(3.14)) # 뒤 숫자에 소수점이있다면 무조건 올린다. 4.
print(ceil(4)) # floor와 ceil 뒤의 숫자가 정수라면 정수 그대로 출력한다. 4.
print(sqrt(9)) # 뒤 숫자의 재곱근을 출력한다. 3. 

# 랜덤함수, 난수
from random import * #random 파일을 임포트한다. 

print(random()) #말 그대로 난수를 출력한다. 0.0~1.0 미만의 값
print(random()*10) # 0.0 ~ 10.0
print(int(random()*10)) #0 ~ 10 미만의 값, 단, 정수 
print(int(random()*10)+1) #1 ~ 10 이하의 값.
print(randrange(1,46)) # 1 ~ 46 미만의 값.
print(randint(1,45)) # 1 ~ 45 이하의 값.

'''Quiz) 월 4회 스터디, 3번은 온라인 1번은 오프라인 

조건1 : 랜덤으로 날짜를 뽑아야함 
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외
출력문 예제) 오프라인 스터디 모임 날짜는 매월 ~일로 선정되었습니다.'''

# from random import *
date = str(randrange(4,28)) # randint를 사용해야 4, 28일이 포함된다. 
print("오프라인 스터디 모임 날짜는 매월" + date + "일로 선정되었습니다.") 
# date를 정의할 때 string을 사용할 수도 있지만, 이후 print 안에서 str(date)를 사용해도 정상적으로 출력이 가능하다. 

date = randint(4,28) # randint를 사용해야 4, 28일이 포함된다. 
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")