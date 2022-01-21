'''
   정수 하나를 입력받아,
   1부터 입력받은 수까지의 합계를 구하는 프로그램을 완성하시오.
   (입력예시) N : 10
   (출력예시) 합계 : 55  
'''

num = input("숫자입력 : ")
num = int(num)

a = 1
sum = 0


while a <= num:
    sum = sum + a 
    

print('합계는 {} 입니다'.format(sum))
   