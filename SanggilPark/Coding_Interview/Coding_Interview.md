# 파이썬 알고리즘 인터뷰 정리

파이썬 알고리즘 인터뷰라는 책을 읽으면서 따로 정리하고자 한다.

[TOC]

## 1. 파이썬 

### 1. 파이썬 문법

#### 1-1. 네이밍 컨벤션

- 스네이크 케이스(Snake Case)를 따르자

  -  snake_case: int = 1

    > 카멜 케이스(Camel case)는 자바의 대표적인 표기 방식이다

#### 1-2. 타입 힌트

- 파이썬 버전 3.5부터 사용할 수 있다.

  ~~~python
  a: str = "1"
  b: int = 1
  ~~~

- 가독성을 위해 함수에 사용하자.

  ~~~python
  # 파라미터 a는 정수형이며 리턴값으로 True 또는 False를 리턴할 것이다.
  def fn(a: int) -> bool:
    pass
  ~~~

- 코딩 테스트 시에는 mypy를 사용하여 타입 힌트에 오류가 없는지 자동으로 확인한다.

#### 1-3. 리스트 컴프리헨션

- map, filter와 같은 함수형 기능을 지원하며 람다 표현식도 지원한다.

- 무리하게 복잡하게 작성할 경우 가독성을 떨어뜨릴 수 있으므로 적절히 사용하자. (대체로 표현식은 2개를 넘지 않아야 한다.)

  ~~~python
  list(map(lambda x: x + 10, [1, 2, 3]))
  >>> [11, 12, 13]
  [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
  >>> [2, 6, 10, 14, 18]
  a = {key: value for key, value in original.items()}
  ~~~

#### 1-4. 제너레이터

- 루프의 반복(Iteration) 동작을 제어할 수 있는 루틴 형태를 말한다.

- 이때, yield 구문을 사용하며 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미이다.

  ~~~python
  def get_natural_number():
      n = 0
      while True:
          n += 1
          yield n
  g = get_natural_number()
  for _ in range(0, 100):
      print(next(g))
  >>> 1 2 3 ... 98 99 100
  def generator():
      yield 1
      yield 'string'
      yield True
  
  g = generator()
  for _ in range(3):
      print(next(g))
  >>> 1, 'string', True
  ~~~

#### 1-5. range

- 주로 for 문에서 쓰이며 range()는 range 클래스를 리턴한다.

- 생성할 숫자가 100만 개쯤 된다면 메모리에서 적지 않은 공간을 차지하고, 생성 시간도 오래 걸릴 것이다. 이때는 제너레이터를 리턴하듯 range 클래스만 리턴하자.

  ~~~python
  a = [n for n in range(1000000)] # size : 8697464
  b = range(1000000) # size : 48
  b[999]
  >>> 999
  ~~~

  - 100만개가 아니라 1억 개라도 b 변수의 메모리 점유율은 동일하다.

#### 1-6. enumerate

- 순서가 있는 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다.

  ~~~python
  a = [1,2,3,2,45,2,5]
  list(enumerate(a))
  >>> [(0, 1), (1,2), (2, 3), ... , (6, 5)]
  ~~~

- 리스트의 인덱스와 값을 함께 출력할 때 이용한다.

  ~~~python
  for i, v in enumerate(a):
    print(i, v)
  ~~~

#### 1-7. // 나눗셈 연산자

- 몫을 구하는 연산자이다.  5 // 3 은 int(5 / 3)과 동일하다

- 나머지는 % 연산자이다.

- 몫과 나머지를 동시에 구하려면 divmod() 함수를 사용하자

  ~~~python
  divmod(5, 3)
  >>> (1, 2)
  ~~~

#### 1-8. print

- print() 함수는 항상 줄바꿈을 하므로 end 파라미터를 공백으로 처리하여 넘기자

  ~~~python
  print('aa', end=' ')
  print('bb')
  >>> aa bb
  ~~~

- 리스트를 출력할 때 는 join()으로 묶어서 처리한다.

  ~~~python
  a = ['A', 'B']
  print(' '.join(a))
  >>> A B
  ~~~

- format보다 f-string을 사용하면 훨씬 간결하고 직관적이며 속도도 빠르다.

  ~~~python
  id = 1
  fruit = "Applie"
  print('{0}: {1}'.format(id + 1, fruit))
  print(f'{idx + 1}: {fruit}')
  >>> 2: Apple
  >>> 2: Apple
  ~~~

#### 1-9. pass

- 인덴트 오류 같은 불필요한 오류를 방지하며 목업(mockup) 인터페이스부터 구현 후 추후 구현을 진행할 수 있게 한다.

#### 1-10. locals

- 로컬에 선언된 모든 변수를 조회할 수 있는 명령이므로 디버깅에 많은 도움이 된다.

---

### 2. 코딩 스타일

- **Clean Code 클린 코드**(로버트 C. 마틴 지음)

  **프로그래밍 수련법** 책을 추천한다.

#### 2-1. 변수명과 주석

- 변수명이 무엇을 의미하는지, 주석을 상세하게 달자.

#### 2-2. 리스트 컴프리헨션

- 한 줄 풀이에 집착하기보다 라인을 좀 더 여유있게 활용해 가독성을 높이자.
- 리스트 컴프리헨션은 표현식이 2개를 넘지 않도록 하자

#### 2-3. 구글 파이썬 스타일 가이드

- 가변 객체(Mutable Obejct)를 사용하지 않아야 한다.

- 기본값으로 []나 {}를 사용하는 것은 지양하자.

- 다음과 같이 불변 객체를 사용하며, None을 명시적으로 할당하는 것도 좋은 방법이다.

  ~~~python
  No: def foo(a, b=[]):
      ...
  No: def foo(a, b: Mapping = {}):
      ...
  Yes: def foo(a, b=None):
      if b is None:
        b = []
  Yes: def foo(a, b: Optional[Sequence] = None):
      if b is None:
        b = []
  ~~~

- True, False를 판별할 때는 암시적인 방법을 사용하자

  굳이 False임을 if foo != []: 와 같은 형태로 판별할 필요가 없으며,

  if foo:로 충분하다

  ~~~python
  --- 좋은 예 ---
  if not users:
    pass
  if foo == 0:
    pass
  if i % 10 == 0:
    pass
  --- 안좋은 예 ---
  if len(users) == 0:
    pass
  if foo is not None and not foo:
    pass
  if not i % 10:
    pass
  ~~~


---

### 3. 빅오

- O(1)
  - 입력값이 아무리 커도 실행 시간이 일정하기 때문에, 최고의 알고리즘
  - 해시 테이블의 조회 및 삽입이 이에 해당
- O(log n)
  - 로그는 매우 큰 입력값에도 크게 영향을 받지 않고, 웬만한 n의 크기에 대해서도 매우 견고함
  - 이진 검색이 이에 해당
- O(n)
  - 선형시간(Linear-Time) 알고리즘 
  - 정렬되지 않은 리스트에서 최댓값 또는 최솟값을 찾는 경우
- O(nlog n)
  - 병합 정렬을 비록한 대부분의 효율 좋은 정렬 알고리즘이 이에 해당
  - 비교 기반 정렬 알고리즘은 아무리 좋은 알고리즘도 O(nlog g)보다 빠를 수 없음
- O(n^2)
  - 버블 정렬 같은 비효율적인 정렬 알고리즘이 이에 해당
- O(2^n)
  - 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당
  - n^2과 혼동하는 경우가 있는데 2^n이 훨씬 큼
- O(n!)
  - 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제를 브루트 포스로 풀이할 때가 이에 해당
  - 가장 느린 알고리즘

---

### 4. 문자열 조작

#### 4-1. 유효한 팰린드롬

[문제 바로가기](https://leetcode.com/problems/valid-palindrome/)

팰린드롬인지 확인하기, 대소문자 구분하지 않고 영문자와 숫자만을 대상으로

- 내풀이 (Runtime : 44ms)

~~~python
data = input()
input_data = []
for char in data:
    if char.isalnum():
        input_data.append(char.lower())

n = len(input_data)
if n % 2 == 0:
    m = n // 2 - 1
else:
    m = n // 2 
    
if input_data[:n//2] == input_data[-1:m:-1]:
    print("true")
else:
    print("false")
~~~

- 풀이 1. 리스트로 변환 ( Runtime : 304 ms)

~~~python
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True
~~~

- 풀이 2. 데크 자료형을 이용한 최적화 (Runtime : 64 ms)

~~~python
import collections
def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
~~~

- 풀이 3. 슬라이싱 사용 (Runtime : 36ms)

  re(정규식 표현) library 사용법을 익히면 좋을 것 같다.

~~~python
import re
def isPalindrome3(self, s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]
~~~

#### 4-2. 문자열 뒤집기

[문제 바로가기](https://leetcode.com/problems/reverse-string)

- 풀이 1. 투 포인터를 이용한 스왑

~~~python
# 풀이 1. 투포인터를 이용한 스왑
def reverseString(self, s: list[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
~~~

- 풀이 2. 파이썬다운 방식

~~~python
# 풀이 2. 파이썬다운 방식
def reverseString2(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # 1
    s.reverse()
    # 2
    s[:] = s[::-1]
~~~

#### 4-3. 로그 파일 재정렬

[문제 바로가기](https://leetcode.com/problems/reorder-data-in-log-files/)

- 풀이 1. 람다와 + 연산자 이용

  람다 표현식이 필요한 경우엔 사용해도 좋다

  map, filter와 함께 섞어서 사용하기 시작하면 가독성이 떨어질수 있으니 주의하자

~~~python
def reorderLogFiles(logs: list[str]) -> list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
~~~

#### 4-4. 가장 흔한 단어

[문제 바로가기](https://leetcode.com/problems/most-common-word/)

- 풀이 1. 리스트 컴프리헨션, Counter 객체 사용

  >  단어가 아닌 모든 문자를 공백으로 치환
  >   \w : 단어 문자
  >   ^ : not 

~~~python
import re
from collections import Counter
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
  words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
  counts = Counter(words)
  # [('ball', 2)]
  return counts.most_common(1)[0][0]
~~~

[re.md 파일](./re(정규식표현).md)

참고 사이트 : [re 관련 정리1](https://whatisthenext.tistory.com/116) [re 관련 정리2](https://yganalyst.github.io/data_handling/memo_6/)

#### 4-5. 그룹 애너그램

[문제 바로가기](https://leetcode.com/problems/group-anagrams/)

- 풀이 1. 정렬하여 딕셔너리에 추가

  애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다.

  존재하지 않는 키를 삽입할 경우 KeyError가 발생하므로, 항상 디폴트를 생성해주는 `defaultdict()`로 선언하며, 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간략하게 구성한다.

~~~python
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
~~~

- 여러 가지 정렬 방법

  - sorted() 함수

    > a = [2, 5, 1, 9, 7]
    >
    > sorted(a)

    output : [1, 2, 5, 7, 9]

    > b = 'zbdaf'
    >
    > sorted(b)

    output : ['a', 'b', 'd', 'f', 'z']

    > b = 'zbdaf'
    >
    > "".join(sorted(b))

    output : 'abdfz'

    > c = ['ccc', 'aaaa', 'd', 'bb']
    >
    > sorted(c, key=len)

    output : ['d', 'bb', 'ccc', 'aaaa']

    > a = ['cde', 'cfc', 'abc']
    >
    > def fn(s):
    >
    > ​	return s[0], s[-1]
    >
    > print(sorted(a, key=fn))

    output : ['abc', 'cfc', 'cde']

    > sorted(a, key=lambda s: (s[0], s[-1]))

    output : ['abc', 'cfc', 'cde']

  - sort() 함수

    >alist.sort() # sort()는 리스트 자체를 제자리 정렬
    >
    >alis = blist.sort() # 잘못된 구문, sort()함수는 None을 리턴한다.

#### 4-6. 가장 긴 팰린드롬 부분 문자열

[문제 바로가기](https://leetcode.com/problems/longest-palindromic-substring/)

- 풀이 1. 중앙을 중심으로 확장하는 풀이 (포인터 개념)

  다이나믹 프로그래밍의 전형적인 문제지만 직관적으로 이해가 어렵고, 실행 속도가 느리므로 **두 포인터가 중앙을 중심으로 확장**하는 형태로 풀이하고자 한다.

~~~python
def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1  # 중심을 기준으로 (왼쪽으로 확장)
            right += 1 # 중심을 기준으로 (오른쪽으로 확장)
        return s[left + 1: right]
    
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, 
        expand(i, i), 	# 길이가 홀수
        expand(i, i+1), # 길이가 짝수
        key=len)				# 길이가 가장 긴 문자열 
    return result
~~~

### 5. 배열

#### 5-1. 두 수의 합

[문제 바로가기](https://leetcode.com/problems/two-sum/)

- 풀이 1. 브루트 포스로 계산 (나의 풀이..)

  최적화할 수 있는 여러 가지 방법이 숨어 있기 때문에, 코딩 인터뷰 시 높은 빈도로 출제되는 문제이다.

  시간 복잡도는 O(n^2)이고 지나치게 느리다.

~~~python
def twoSum(self, nums: List[int], target: int) -> List(int):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return[i, j]
~~~

- 풀이 2. in을 이용한 탐색

  모든 조합을 비교하지 않고 타겟에서 첫 번째 값을 뺀 값 target - n이 존재하는지 탐색하는 문제로 변경해보자. 

~~~python
def twoSum(self, nums: List[int], target: int) -> List(int):
  for i, n in enumerate(nums):
    complement = target - n
  	if complement in nums[i+1:]:
      return nums.index(n), nums[i+1:].index(complement) + (i+1)
~~~

- 풀이 3. 첫 번째 수를 뺀 결과 키 조회

  타겟에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있다. 두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장해두면, 나중에 두번째 수를 키로 조회해서 정답을 즉시 찾아낼 수 있다.

  딕셔너리는 해시 테이블로 구현되어 있으므로 시간 복잡도는 평균적으로 O(1)이며, 최악의 경우 O(n)이 된다.

~~~python
def twoSum(self, nums: List[int], target: int) -> List(int):
  nums_map = {}
  # 키와 값을 바꿔서 딕셔너리로 저장
  for i, num in enumerate(nums):
    nums_map[num] = i
  for i, num in enumerate(nums):
    if target - num in num_map and i != nums_map[target - num]:
      return nums.index(num), nums_map[target - num]
~~~

- 풀이 4. 조회 구조 개선 (여러번 풀어서 감을 익혀야 할듯)

~~~python
def twoSum(self, nums: List[int], target: int) -> List(int):
  nums_map = {}
  # 하나의 for 문으로 통합
  for i, num in enumerate(nums):
    if target - num in nums_map:
      return [nums_map[target - num], i]
    nums_map[num] = i 
~~~

- 풀이 5. 투 포인터 이용

이 문제에서는 적용이 불가능하다 

만약 이 문제가 인덱스가 아니라 값을 찾는 문제라면, 얼마든지 정렬하고 투 포인터로 풀 수 있지만 인덱스를 찾아내는 문제에서 정렬을 하게 되면 원래의 인덱스를 찾을 수가 없기 때문이다.

방법은 익혀두자!

~~~python
def twoSum(self, nums: list[int], target: int) -> list[int]:
  left, right = 0, len(nums) - 1
  while not left == right:
    # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
    if nums[left] + nums[right] < target:
      left += 1
    elif nums[left] + nums[right] < target:
      right -= 1
    else:
      return left, right
~~~

#### 5-2. 빗물 트래핑

난이도 상.. 이해할 때 까지 봐야할 듯

[문제 바로가기](https://leetcode.com/problems/trapping-rain-water/)

- 풀이 1. 투 포인터를 최대로 이동

~~~python
def trap(self, height: List[int]) -> int:
  if not height:
    return 0
  volume = 0
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]
  
  while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)
    if left_max <= right_max:
      volume += left_max - height[left]
      left += 1
    else:
      volume += right_max - height[right]
      right -= 1
  return volume
~~~

- 풀이 2. 스택 쌓기

~~~python
def trap2(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()
            if not len(stack):
                break
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
        stack.append(i)
    return volume
~~~

#### 5-3. 세수의 합

[문제 바로가기](https://leetcode.com/problems/3sum/)

- 풀이 1. 브루트 포스로 계산

  앞 뒤로 같은 값이 있는 경우, sort() 함수를 사용해 정렬하자

~~~python
def threeSum(self, nums: List[int]) -> List(List[int]):
  results = []
  nums.sort()
  
  # 브루트 포스 n^3 반복
  for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i-1]:
      continue
    for j in range(i+1, len(nums) - 1):
      if j > i+1 and nums[j] == nums[j-1]:
        continue
      for k in range(j + i, len(nums)):
        if k > j+1 and nums[k] == nums [k-1]:
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          results.append((nums[i], nums[j], nums[k]))
  return results
~~~

O(n^3) 은 어림도 없다.. 최적화를 진행하자

- 풀이 2. 투포인터로 합 계산

~~~python
def threeSum(self, nums: List[int]) -> List(List[int]):
  results = []
  nums.sort()
  
  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    left, right = i+1, len(nums)-1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum < 0:
        left += 1
      elif sum > 0:
        right -= 1
      else:
        results.append((nums[i], nums[left], nums[right]))
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1
  return results 
~~~

#### 5-4. 배열 파티션 1

[문제 바로가기](https://leetcode.com/problems/array-partition-i/)

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

- 풀이 1. 오름차순 풀이

  min()을 합산했을 때 최대가 되려면 결국 min()이 되도록 커야한다.

~~~python
def arrayPairSum(self, nums: List[int]) -> int:
  sum = 0
  pair = []
  nums.sort()
  
  for n in nums:
    pair.append(n)
    if len(pair) == 2:
      sum += min(pair)
      pair = []
  return sum
~~~

- 풀이 2. 짝수 번째 값 계산

~~~python
def arrayPairSum(self, nums: List[int]) -> int:
  sum = 0
  nums.sort()
  
  for i, n in enumerate(nums):
    if i % 2 == 0:
      sum += n
  return sum
~~~

- 풀이 3. 파이썬다운 방식

~~~python
def arrayPairSum(self, nums: List[int]) -> int:
  return sum(sorted(nums)[::2])
~~~





































