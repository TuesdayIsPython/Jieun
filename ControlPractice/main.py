
'''money = input()
money = int(money)'''


'''
if money >= 3800:
    print("택시를 타세요.")
else:
    print("버스와 같은 대중교통을 이용하세요.")
'''

'''if money == 1250:
    print("어른이군요")
elif money == 720:
    print("청소년이군요")
elif money == 450:
    print("어린이군요")
else:
    print("요금을 잘못 내셨군요!!!! 다시 내세요!")'''


'''x = 200
y = 200

print(x == y)
'''

'''money = 2000
card = True

if money >= 3800 or card:
    print("돈도 3800원 이상 있고, 카드도 있으니 택시를 타세요.")
else:
    print("돈이 부족하네요..")'''


'''pocket = ['cellphone', 'money', 'card']

if 'coin' in pocket:
    print("주머니에 동전이 있네요.")
elif 'card' in pocket:
    print("주머니에 카드가 있네요.")
else:
    print("주머니에 무엇이 있나요?")'''

'''treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")'''


'''name = "투쓰데이 이즈 파이썬"
print("Hello %s" % name)'''


'''prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number == 1:
        print("Add를 입력하셨습니다.")
    elif number == 2:
        print("Del를 입력하셨습니다.")
    elif number == 3:
        print("List를 입력하셨습니다.")
    else:
        print("Quit을 입력하셨습니다. 프로그램을 종료합니다.")'''


'''money = 10000
menu = "아메리카노"

order = """
... 1. 아메리카노 -> 2500원
... 2. 카페라떼 -> 3000원
... 3. 바닐라라떼 -> 3500원
... 4. 아인슈페너 -> 4000원
... 
... 메뉴를 입력하세요: """

while money:
    print(order)
    menu = input()
    if menu == "아메리카노":
        money -= 2500
        print("아메리카노를 주문하셨습니다. 2500원입니다.")
        print("남은 금액은 %s원 입니다." %money)
    elif menu == "카페라떼":
        money -= 3000
        print("카페라떼를 주문하셨습니다. 3000원입니다.")
        print("남은 금액은 %s원 입니다." % money)
    elif menu == "바닐라라떼":
        money -= 3500
        print("바닐라라떼를 주문하셨습니다. 3500원입니다.")
        print("남은 금액은 %s원 입니다." % money)
    else:
        money -= 4000
        print("아인슈페너를 주문하셨습니다. 4000원입니다.")
        print("남은 금액은 %s원 입니다." % money)

    if money < 2500:
        print("더이상 주문가능한 메뉴가 없습니다. 주문 프로그램을 종료합니다.")
        break'''

'''a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)'''

'''while True:
    print("Ctrl+C를 눌러야 while문을 빠져나가 프로그램을 종료할 수 있습니다!")'''

'''test_list = ['one','two','three']
for i in test_list:
    print(i)'''

'''scores = [100, 70, 40, 20, 80]
passCnt = 0
failCnt = 0

for i in scores:
    if i >= 60:
        print("합격:",i)
        passCnt += 1
    else:
        print("불합격:", i)
        failCnt += 1

print("합격한 학생의 수는 %s명 입니다." %passCnt)
print("불합격한 학생의 수는 %s명 입니다." %failCnt)'''


'''scores = [90, 25, 67, 45, 80]

number = 0
for score in scores:
    number = number +1
    if score < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)'''


'''add = 0
for i in range(1,11):
    print("현재 진행되고 있는 숫자: ",i)
    add = add + i

print("더한 최종 결과: ",add)'''


'''for i in range(2,10):
    for j in range(1,10):
        print(i*j, end= " ")
    print('')'''

