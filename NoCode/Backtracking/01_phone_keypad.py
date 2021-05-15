'''
Date : 21. 05. 16
'''

import sys
input = sys.stdin.readline

graph = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
        '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
input_number = input().strip()

result = []
def dfs(index, letter):
    if len(letter) == len(input_number):
        result.append(letter)    
    for i in range(index, len(input_number)):
        for j in graph[input_number[i]]:
            dfs(i+1, letter+j)

dfs(0,"")
print(result)