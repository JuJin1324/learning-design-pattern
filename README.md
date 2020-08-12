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
### import modules
* compare string contain: [Does Python have a string 'contains' substring method? - Stack overflow](https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method)
* urlparse: [파이썬으로 URL 가지고 놀기 - urllib.parse 편](https://velog.io/@city7310/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-URL-%EA%B0%80%EC%A7%80%EA%B3%A0-%EB%86%80%EA%B8%B0)
* BeautifulSoup: [[Python] BeautifulSoup Library 사용법 및 예제](https://codetravel.tistory.com/22)
* urllib: [urllib.request : urlretrieve, urlopen, urlerror, urlparser](https://velog.io/@shchoice/urllib.request-urlretrieve-urlopen)
* httplib2: [python으로 REST API 호출](https://glshlee.tistory.com/94)
* requests: [Python requests 모듈 간단 정리](https://dgkim5360.tistory.com/entry/python-requests)

### change module
httplib2 -> requests
```
status, response = httplib2.Http().request(url) ---> response = requests.get(url)
status.get('content-type')                      ---> response.headers['Content-Type']
```

## chapter3: Building Factories to Create Objects
Factory Method Pattern: Creator(Factory)가 Product 를 method 를 통해서 만들어내는 패턴   
참고사이트: [[Design pattern] Factory method pattern (팩토리 메소드 패턴)](https://eomtttttt-develop.tistory.com/86?category=851834)   
위 사이트에서는 Creator 가 `PizzaStore`이고 Creator 는 추상화 클래스로 제공하며 해당 추상화 Creator 클래스를 상속받은 클래스(ChicagoPizzaStore, NYPizzaStore)
를 통해서 Product(Pizza)를 만들어낸다. - 해당 사이트의 구현은 프로젝트 디렉터리 아래 addition 디렉터리에 해놨다.

### string join / split
> join example
```python
str_list = ['hello', 'world']
joined = ''.join(str_list)
print(joined)
# 결과
# helloworld

joined = '\n'.join(str_list)
print(joined)
# 결과
# hello
# world
```

> split example
``` python
'1,2,3'.split(',', maxsplit=1)
['1', '2,3']
```

* [[python] 파이썬 문자열 합치기 나누기 split/join 함수](https://devpouch.tistory.com/77)
* [실용적인 Python 디자인 패턴 정리](https://velog.io/@jahoy/%EC%8B%A4%EC%9A%A9%EC%A0%81%EC%9D%B8-Python-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-%EC%A0%95%EB%A6%AC)


### change module
BeautifulStoneSoup for Parsing XML Document -> BeautifulSoup(content, 'xml')   

urllib2 for connect to FTP server -> ftplib   
예제)
```python
from ftplib import FTP

host = 'ftp.freebsd.org'
path = '/pub/FreeBSD'
with FTP(host) as ftp:
    ftp.login()
    ftp.cwd(path)
```
주의) FTP() 안에는 url이 아닌 path를 제외한 host 주소만 넣어주어야 한다.


### Syntax
is 와 == 차이
> is는 객체(Object) 비교 / == 는 값(Value) 비교
> [[Python] 'is'와 '=='의 차이](https://twpower.github.io/117-difference-between-python-is-and-double-equal)

Abstract Class 선언 변경
```python
# 기존
import abc
class Port:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __str__(self):
        pass

# 변경
from abc import abstractmethod, ABC
class Port(ABC):
    @abstractmethod
    def __str__(self):
        pass
```

## chapter4: The Facade Design Pattern
### URL Encoding
URL에 사용할 수 없는 문자를 사용할 수 있는 문자 집합으로 변환하는 것. 이것도 두 가지가 있는데, 공백을 '%20'으로 변환하는 것과 '+'로 변환하는 것이 다르다.
```python
>> urllib.parse.quote('안녕 python')
'%EC%95%88%EB%85%95%20python'
>> urllib.parse.quote_plus('안녕 python')
'%EC%95%88%EB%85%95+python'
```

### requests.get().json() / requests.get(url).text 
* `requests.get(url).json()`을 통해서 json의 dict 객체를 가져올 수 있다. 사실상 이 기능으로 인해서 Parser 클래스는 필요가 없어졌지만 
Facade 패턴 사용 샘플을 위해서 일부러 남겨두었다.
* `requests.get(url).text` 를 통해서 text 형식의 객체를 가져올 수 있다. 이 문장을 통해서 json을 str 로 가져와서 return 하였다.

### pickle 사용시 주의사항
pickle로 데이터를 저장하거나 불러올때는 파일을 바이트형식으로 읽거나 써야한다. (wb, rb)

## chapter5: Proxy & Observer Patterns
### Syntax
* getattr() 함수: [파이썬 getattr()](https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_getattr())
* 여기서 사용한 self.__class__ 는 인스턴스 메서드에서 클래스 변수에 접근하기 위한 cls 대용.