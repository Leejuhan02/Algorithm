# Data types_List

odd= [1,2,3,4,5,6,7]
print(odd)
print(odd[2]) #List 안에서 설정된 좌표값. 2 는 0,1,2 순으로 3이된다.
a= odd[1]+odd[3] #List 안에 저장된 변수들은 각각의 Data type을 따른다. 
print(a)

b= odd[-1] #뒤에서부터 첫번째
print(b)

odd2= [1,2,3,[4,5,6]]
print(odd2[3]) #List 안에서 묶인 또 하나의 list가 바깥의 list에서 한 묶음으로 취급된다. 
print(odd2[3][1]) # odd2를 인덱싱하여 두번째 list를 불러오고 싶을때, 두번째 list의 좌표를 찍어주고 그 안에서 원하는 숫자의 좌표를 다시 0,1,2롤 잡아주면 된다. 

c=odd[0:3] #list도 슬라이싱이 가능하다. 
print(c) #문자열 슬라이싱과 완전히 같다. 

print("="*50)

# Quiz) A=[1,2,3,4,5] 에서 리스트 [2,3]을 만들어라 
A= [1,2,3,4,5]
print(A[1:3])

print("="*50)

odd3=odd+odd2
print(odd3)

odd4=odd*2
print(odd4)

print(len(odd4))

odd[0]=0
print(odd) # list 값 중 하나를 초기화 재정의 할 수 있다.

del odd[0] #list 값 중 하나를 삭제 할 수 있다. 
print(odd)

print("="*50)

odd5=[3,4,2,1,6,9,7,0]
print(odd5)

odd5.append(10) # List맨 뒤에 ()안의 요소 추가 
print(odd5)

odd5.sort() # List 내용물을 숫자 크기대로 정렬, 문자는 알파뱃 순서대로 정렬 
print(odd5)

odd5.reverse() # List를 앞뒤로 뒤집는다. 이때, List의 내용물을 정렬하지 않고 뒤집기만 한다.
print(odd5)

odd6=[1,2,3,4,5]
print(odd6.index(3)) # index는 ()의 요소의 List 내에서의 좌표값을 돌려준다. 

odd6.insert(0,0) #.insert(a,b) 는 a좌표 값을 뒤로 밀고, 그 자리에 b를 삽입한다. 
print(odd6)

odd7=[1,1,2,2,3,3,4,4]
odd7.remove(2) #.remove(a) 는 List내에서 첫번째로 등장하는 요소 a를 지운다. 복수로 존재해도 앞의 a만 삭제한다. 
print(odd7)

print(odd6.pop(0)) # .pop(a)는 List의 a좌표의 값을 돌려주고, 그 좌표의 값은 삭제한다. 괄호 안이 비어있을 경우 마지막값. odd6의 0좌표 값인 0이 출력되는 것을 확인할 수 있다.
print(odd6) # odd6의 0좌표 값인 0이 빠진 체 출력되는 것을 확인할 수 있다. 

print(odd7.count(1)) #.count(a) 는 List안의 a의 개수를 세어 돌려준다. 

odd8=[6,7,8]
odd6.extend(odd8) # list에 list를 더한다. 괄호 안에는 list만 올 수 있다. 
print(odd6) 

#tuple Data type
#tuple은 한번 선언한 이상, tuple 안의 요솟값을 삭제 변경이 불가능하다는 점을 제외하고는 list와 완전히 동일하다. 
print("="*50)
t1=(1,2,3,4)
print(t1[0]) #인덱싱 가능
print(t1[:3]) #슬라이싱 가능
print(t1*2) #반복 가능
print(len(t1)) #길이 구하기 가능

t2=(1,2,3)
print(t2+(4,)) # tuple끼리 더할 수 있다. tuple의 요솟값이 하나일 경우, (a,)식으로 ,가 필요하다. 

# Dictionary Data type
print("="*50)
dic = {'name':'John', 'phone':'01012345678', 'sex':'male'} 
print(dic)
# dictionary는 {'a':'b'} 형식으로 구성된다. a가 key, b가 value이다.

dic['birth']= '020407' # key인 birth와 value인 생년월일을 추가했다. 
print(dic)

dic[1]=[1,2,3,4] # list를 추가했다. 
print(dic)

del dic[1] # key가 1인 dictionary쌍을 삭제했다. 
print(dic)

value1= dic['name'] # dictionary의 key를 사용해 정의하면, value가 정의된다. 
print(value1) # key 없이 value를 바로 꺼낼 수는 없다. 

dic2={1:'a', 1:'b'}
print(dic2[1]) # 같은 key가 두개 이상 존재할 경우, 앞에서 key에 배정된 value는 무시하고, 마지막에 배정된 value를 돌려준다.

# key는 변하지 않는 값이어야 한다. 예를들어 tuple은 변하지 않기 때문에 key로 사용 가능한 반면, list는 수정 삭제가 가능하기 때문에 불가능하다. 

print(dic.keys()) # key만을 나열하여 출력한다. list와 같이 인식되지만, list고유의 append, insert, pop, sort는 사용할수 없다.  
list(dic.keys()) # list형으로 변환

print(dic.values()) #''

print(dic.items()) # dictionary 쌍을 나열해준다. 

print(dic.get('name')) # print(dic['name']) 과 다를 바 없으나, 존재하지 않는 key를 입력했을 때, 오류를 발생시키지 않고, None을 돌려준다. 
print(dic.get(123))

dic3={1:2, 3:4, 5:6}
dic3.clear() # dictionary의 요솟값을 모두 지운다. 
print(dic3)

print('name' in dic) # 'a' in dictionary 는 a가 dictionary안에 존재하는지 조사할 때 사용한다. 

print("="*50)

quiz= {'name':'홍길동', 'birth':1128, 'age':30}
print(quiz)
print(quiz['name'])
print(quiz['birth'])
print(quiz['age'])
quiz['phonenumber']='01012345678'
print(quiz.get('phonenumber'))
print(quiz.get('sex', 'male'))

print("="*50)

# set Data type
s1= set([1,2,3])
print(s1)

s2= set(["hello"])
print(s2)

s3= set("hello") # 괄호 하나에 싸여있는 문자열의 경우, 개별 구성요소를 순서없이 나열한다. 이때, 중복을 허용하지 않는다. 
print(s3)

l1= list(s3)
l1.sort()
print(l1)
print(l1[0])

t1= tuple(s3) # s3에서 임의의 순서로 정의된 것을 따라 tuple화 한다. 
print(t1)
print(t1[0])

s4=set([1,2,3,4,5,6])
s5=set([4,5,6,7,8,9])
intsec= s4&s5 # 두 set 사이의 교집합을 구한다. 
print(intsec)

intsec2= s4.intersection(s5) # 이것으로도 교집합을 구할 수 있다. 
print(intsec2)

uni= s4 | s5 # 합집합을 구하는 공식이다. shift + \ 이다. 
print(uni)

uni2= s4.union(s5)
print(uni2)

dif= s4-s5
print(dif)

dif2= s5-s4
print(dif2)

dif3= s4.difference(s5)
print(dif3)

s4.add(7)
print(s4)

s5.update([7,8,9,10,11])
print(s5)

s5.remove(11)
print(s5)

print("="*50)

# bool Data type
# True False 를 나타내는 자료형.

bo1= True
bo2= False

type(bo1)
type(bo2)

# 보류
