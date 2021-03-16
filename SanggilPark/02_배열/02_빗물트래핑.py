"""
Date : 21년 3월 16일
Description : Algorithm Study
Title : 빗물 트래핑
"""
"""
https://leetcode.com/problems/trapping-rain-water/

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""
# 다시 풀기.. (이해가 안돼ㅠㅠㅠ)
def trap(height: list[int]) -> int:
    if not height:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        print(left_max, right_max, height[left], volume)
        if left_max <= right_max:
            print("왼쪽 이동")
            volume += left_max - height[left]
            left += 1
        else:
            print("오른쪽 이동")
            volume += right_max - height[right]
            right -= 1
    return volume

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
# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
