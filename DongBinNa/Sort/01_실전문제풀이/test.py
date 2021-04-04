
n = int(input())

stages = list(map(int, input().split()))
stages.sort()

result = []
total_palyers = len(stages)
for i in range(1, n+1):
    num_players = stages.count(i)
    if num_players == 0:
        fail_rate = 0
    else:
        fail_rate = num_players / total_palyers
    total_palyers -= num_players
    result.append((i, fail_rate))

print(result)
result.sort(key=lambda x: x[1], reverse=True)

for i in result:
    print(i[0], end= " ")