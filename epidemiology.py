day = 0
target = int(input())
people = int(input())
infections = int(input())
total = people
while True:
    if total > target:
        print(day)
        break
    else:
            day += 1
            people = people * infections
            total += people
