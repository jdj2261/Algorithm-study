"""
Date : 21년 3월 13일
Description : Algorithm Study
Title : 가장 흔한 단어
"""
"""
https://leetcode.com/problems/most-common-word/
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""


import re
from collections import Counter
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

    counts = Counter(words)
    return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]

print(mostCommonWord(paragraph, banned))