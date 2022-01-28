

path = 'C:/SBS_Python 과정(git)/SBS_Python/Day10/'

# 읽기모드 : r (read)
# 파일유형 : t (text)
file = open(path + 'hello.txt', 'rt', encoding = 'UTF-8')

while True:
   # str = file.read(10)     # 파일로부터 10글자씩 읽어온다.
   str = file.readline()     # 파일로부터 한 줄씩 읽어온다.
   if not str:             # 읽어온 글자가 없으면, 멈춤
       break
   print(str, end='')
        
file.close()