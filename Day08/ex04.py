
'''
   ���������� 
   : �Լ� ���ο��� ������ ����
     �Լ� ���ο����� ���� �����ϰ�, �ܺο����� ������ �� ����.
   
   
   ����������
   : �Լ� �ܺο��� ������ ����
     �Լ� ���γ� �ܺ� ��� �������� ������ �� �ִ�.
'''

def func():
    a = 10     # 지역변수 
    print('f() 내부 - a : {}'.format(a))
  
func()         # 함수호출
    
# print('f() 외부 - a : {}'.format(a))
# 에러 발생
# NameError: 'a' is not defined (변수 'a'가 선언되어있지 않습니다.)

b = 10         # 전역변수

def test():
    print('f() 내부 - b : {}'.format(b))
    
test()         # 함수호출
print('f() 외부 - b : {}'.format(b))