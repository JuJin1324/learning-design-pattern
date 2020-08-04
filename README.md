# learning-design-pattern
It's a practice for programming design pattern using python.  
The code is from the book 'Learning Python Design Patterns'  
I'm not the author this book. It's just practice. Thank you.  

## chapter1
### Indexing
* [:-1] : 가장 마지막 원소를 뺀 전부
* [Python 문자열 관련 함수.](http://egloos.zum.com/itbaby/v/4243381)

### 클래스 내부에서 클래스 자신의 타입 표시하기
class 선언시 내부 메서드에서 클래스 자신을 type hint 표시하면 에러 발생   
예시)
```python
class Url(object):
    short_url = ""
    full_url = ""

    @classmethod
    def shorten(cls, full_url: str) -> Url: # <- NameError: name 'Url' is not defined 에러 발생!
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        return instance
```
Python 4.0 이상인 경우 해당 문제는 발생하지 않는다.   
하지만 Python 4.0 이하의 경우 발생하며 최상단에 `from __future__ import annotations` 추가를 통해서 해결한다.    
참조사이트: [Stack overflow - How do I specify that the return type of a method is the same as the class itself?](https://stackoverflow.com/questions/33533148/how-do-i-specify-that-the-return-type-of-a-method-is-the-same-as-the-class-itsel)

### pickle
* pickle 모듈
일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용한다.   
하지만 리스트나 클래스같은 텍스트가 아닌 자료형은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.   
파이썬에서는 이와 같은 텍스트 이외의 자료형을 파일로 저장하기 위하여 pickle이라는 모듈을 제공한다.  
* 참조사이트: [강의노트 04. 파이썬 pickle 모듈](https://wayhome25.github.io/cs/2017/04/04/cs-04/)

## chapter2
### compare string contain
[Does Python have a string 'contains' substring method? - Stack overflow](https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method)

### urlparse
netloc - [파이썬으로 URL 가지고 놀기 - urllib.parse 편](https://velog.io/@city7310/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-URL-%EA%B0%80%EC%A7%80%EA%B3%A0-%EB%86%80%EA%B8%B0)

### BeautifulSoup
[[Python] BeautifulSoup Library 사용법 및 예제](https://codetravel.tistory.com/22)

### urllib
[urllib.request : urlretrieve, urlopen, urlerror, urlparser](https://velog.io/@shchoice/urllib.request-urlretrieve-urlopen)

### httplib2
[python으로 REST API 호출](https://glshlee.tistory.com/94)

