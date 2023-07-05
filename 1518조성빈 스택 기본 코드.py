Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 빈 스택(리스트) 초기화
>>> stack = []
>>> stack
[]
>>> # 스택에 원소 추가
>>> 
>>> stack = [1,2,3]
>>> stack.append(4)
>>> 
>>> stack
[1, 2, 3, 4]
>>> 
>>> # 스택에서 원소 제거
>>> 
>>> stack = [1,2,3]
>>> top = stack.pop()
>>> 
>>> print(top)
3
>>> stack
[1, 2]
>>> 
>>> # 스택의 top 가져오기
>>> 
>>> stack = [1,2,3]
>>> top = stack[-1]
>>> 
>>> top
3
