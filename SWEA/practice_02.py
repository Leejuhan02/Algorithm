sentence = '나는 군인입니다.'
print(sentence)
sentence2 = "파이썬은 쉽습니다."
print(sentence2)
sentence3 = """나는 군인이고 
파이썬은 쉽습니다."""
print(sentence3) # """ 사용시 줄 바꿈도 적용되서 출력된다. 

juhan = "020407-1234567" # 첫번째 숫자인 0은 첫번쩨 숫자가 아닌 시스템에서 0번쨰 숫자로 인식한다. 

print("성별:" + juhan[7])
print("출생년도:" + juhan[0:2]) # 0부터 2 전까지 
print("월:" + juhan[2:4])
print("일:" + juhan[4:6])

print("생년월일:" + juhan[:6]) #처음부터 6 전까지
print("뒤 7자리:" + juhan[7:]) #7번부터 끝까지
print("뒤 7자리 (뒤에서부터)" + juhan[-7:]) #맨 끝부터 뒤로 7개를 세어 출력

python = "Python is Amazing"
print(python.lower()) # 모든문자 소문자 출력
print(python.upper())
print(python[0].isupper()) # python 문자열의 첫번째 글자는 대문자인가? 
print(python.replace("Python", "java")) # 문장내의 파이썬을 자바로 바꿔 출력 

index = python.index("n")
print(index) # 파이썬 문자열에서 n이라는 문자가 몇번쨰에 위치하고 있는지 출력
index = python.index("n", index+1)
print(python.find("java")) # find 없으면 -1
print(python.index("Python"))

print("나는 %d살입니다." % 20) # %d 안에는 정수만 들어감 
print("나는 %s를 좋아해요" % "파이썬")
print("나는 %c형입니다." % "A")

print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))

age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문
print("백문이 불여일견 \n백견이 불여일타") # \n은 줄바꿈 
print("저는 '이주한'입니다.")
print('저는 "이주한"입니다.')
print("저는 \'이주한\'입니다.")
print('저는 \"이주한\"입니다.')

#\\ 는 출력되는 문장 내에서 \ 하나로 출력된다. 

# \r 커서를 맨 앞으로 이동 
print("red apple\rpine") # 커서를 맨 앞으로 옮겨 pine을 덮어씌움 즉, red와 뒤의 빈 칸 하나 총 4칸을 pine이 덮어쓴것이다. 

print()


#quiz 사이트 별로 비밀버호를 만들어주는 프로그램을 작성하시오. 

url = "https://google.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")] # my_str의 인덱스로 찾은 . 의 위치 이전까지 라는 의미 [0:.의 위치]
# my_str를 초기화, 재정의 하였다. 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# str 문자열,  len 문자열의 길이 측정, replace로 앞 주소 날림. 

