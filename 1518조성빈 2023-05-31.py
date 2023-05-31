Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# marks1.py
marks = [90, 25, 67, 45, 80]
number=0
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
        else:
            
SyntaxError: invalid syntax
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
        else: print("%d번 학생은 불합격입니다." % number)
        
SyntaxError: invalid syntax
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)

        
1번 학생은 합격입니다.
3번 학생은 합격입니다.
5번 학생은 합격입니다.
else: print("%d번 학생은 불합격입니다." % number)
SyntaxError: invalid syntax
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)

        
6번 학생은 합격입니다.
8번 학생은 합격입니다.
10번 학생은 합격입니다.
>>> 
>>> 
>>> 
>>> for mark in marks:
...     number = number +1
...     if mark >=60:
...         print("%d번 학생은 합격입니다." % number)
... 
...         
11번 학생은 합격입니다.
13번 학생은 합격입니다.
15번 학생은 합격입니다.
>>> for mark in marks:
...     number = number +1
...     if mark >=60:
...         print("%d번 학생은 합격입니다." % number)
... 
...         
16번 학생은 합격입니다.
18번 학생은 합격입니다.
20번 학생은 합격입니다.
>>> for mark in marks:
...     number = number +1
...     if mark >=60:
...         print("%d번 학생은 합격입니다." % number)
... 
...         
21번 학생은 합격입니다.
23번 학생은 합격입니다.
25번 학생은 합격입니다.
>>> for mark in marks:
...     number = number +1
...     if mark >=60:
...         print("%d번 학생은 합격입니다." % number)
... 
...         
26번 학생은 합격입니다.
28번 학생은 합격입니다.
30번 학생은 합격입니다.
