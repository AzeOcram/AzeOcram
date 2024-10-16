import random

nums = []
toShow=[]

for i in range(1, 101):
    nums.append(i)

random.shuffle(nums)

print("Think of a number from 1 to 100")

while True:
    if input("Are you ready? [Y/N] ") == 'Y':
        break

while True:
    print()
    if len(nums) == 1:
        break

    for i in range(int(len(nums)/2)):
        toShow.append(nums[0])
        nums.pop(0)
        print(toShow[i], end=' ')

        if i%5 == 0:
            print()

    print()
    ans = input("Is your number here? [Y/N] ")

    if ans == 'Y':
        for i in range(len(nums)):
            nums.pop(0)

        for i in range(len(toShow)):
            nums.append(toShow[i])
    
    for i in range(len(toShow)):
        toShow.pop(0)
    

print("Your number is " + str(nums[0]))