"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 그룹 애너그램
"""
"""
https://leetcode.com/problems/group-anagrams/
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = defaultdict(list)
for word in strs:
    anagrams[''.join(sorted(word))].append(word)
    print(anagrams.keys(), anagrams.values())