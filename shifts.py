text = input()
compare = input()
inarray = [char for char in compare]
counter = 0
for i in range(len(compare)):
    if compare in text:
        print("yes")
        break
    else:
        counter += 1
        temp = compare[0]
        inarray.remove(temp)
        inarray.append(temp)
        compare = ""
        for i in inarray:
            compare = compare + i
if counter == len(compare):
    print("no")
