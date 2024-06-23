from collections import Counter
size_of_group = int(input())
list_of_rooms = list(map(int,input().split()))
not_repeated = Counter(list_of_rooms)

for room,count in not_repeated.items():
    if count == 1:
        print(room)
        break






