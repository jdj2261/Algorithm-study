"""
입력 데이터 개수가 많으면 input() 함수를 사용했을 때 느려진다.
sys 라이브러리의 readline() 함수를 이용하자!
"""
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)