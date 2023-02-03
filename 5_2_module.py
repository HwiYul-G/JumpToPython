# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 모듈을 사용하는 이유는 코드를 재사용하기 위해서이다.

# 모듈 만들기
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 모듈(파이썬 파일)을 파이썬에서 불러와 사용하려면
# cmd 창에 module 파일을 저장한 디렉터리로 cd 명령어를 통해 이동한 다음
# dir 명령어를 통해 대화형 인터프리터를 실행하자.

# 반드시 module 파일을 저정한 디렉터리로 이동한 다음 진행해야만
# 대화형 인터프리터에서 모듈파일(파이썬 파일)을 읽을 수 있다.

# import 모듈명을 해야하지, import 모듈명.py를 하면 안된다.

# 때로는 모듈명.함수명() 이런 식으로 쓰지 않고
# 편리하게 함수명() 만 사용할 수 있다. 이를 위해슨 아래와 같이 사용하면 된다.
# from 모듈이름 import 모듈함수
# 모듈 함수 여러개를 간단하게 사용하고 싶다면,
# from 모듈명 import 함수1, 함수2 이런식으로 작성하면 된다.
# 모든 함수를 import하고 싶다면
# from 모듈명 import * 이런식으로 작성하면 된다.

if __name__ == "__main__":
    print(add(3, 4))
    print(sub(4, 2))
    
# if __name__ == "__main__": 을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때
# __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는
# __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.

# __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# 만일 python mod1.py 처럼 직접 mod1.py 파일을 실행할 경우
# mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우
# mod1.py의 __name__변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.