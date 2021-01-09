"""
Date : 21년 1월 9일
Description : 합집합 찾기 알고리즘
Title : Union find 
address : https://m.blog.naver.com/ndb796/221230967614 (동빈나 알고리즘)
"""

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x] 

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b: return 1
    else: return 0


if __name__ == "__main__":
    parent_list = [i for i in range(0,11)]
    
    unionParent(parent_list, 1, 2)
    unionParent(parent_list, 2, 3)
    unionParent(parent_list, 3, 4)
    unionParent(parent_list, 5, 6)
    unionParent(parent_list, 6, 7)
    unionParent(parent_list, 7, 8)
    print("1과 5는 연결되어 있나요? {}".format(findParent(parent_list, 1, 5)))
    unionParent(parent_list, 1, 5)
    print("1과 5는 연결되어 있나요? {}".format(findParent(parent_list, 1, 5)))

