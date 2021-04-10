x, y = map(int, input().split())

add_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0
for index, day in enumerate(add_day[:x-1]):
    cnt += day
cnt += y-1
result = cnt % 7

day_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(day_week[result])
# if result == 0:
#     print("MON")
# elif result == 1:
#     print("TUE")
# elif result == 2:
#     print("WED")
# elif result == 3:
#     print("THU")
# elif result == 4:
#     print("FRI")
# elif result == 5:
#     print("SAT")
# elif result == 6:
#     print("SUN")

# 다른 풀이
# x, y = map(int, input().split())
# for i in range(1, x):
#     if i in [1, 3, 5, 7, 8, 10, 12]:
#         y += 31
#     elif i == 2:
#         y += 28
#     else:
#         y += 30
# day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# print(day_week[y % 7])