"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 로그 파일 재정렬
"""
"""
https://leetcode.com/problems/reorder-data-in-log-files/
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
"""


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    
if __name__ == "__main__":
    sol = Solution()
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    result = sol.reorderLogFiles(logs)
    print(result)