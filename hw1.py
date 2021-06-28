from random import randint

random_number = randint(1,45)
bonus_number = randint(1,45)
print("Lotto Number is ")
print(random_number)
print("Bonus Number is ")
print(bonus_number)

bonus_bingo = 0
if bonus_number == random_number:
    bonus_bingo = 1

bingo = 0
time = 1
while time <= 6:
    random_number = randint(1,45)
    print("Lotto Number is ")
    print(random_number)
    i = input("Input the number: ")
    input_number = int(i)
    if random_number == input_number:
        bingo = bingo + 1
    time = time + 1

if bingo == 6:
    print("You are 1st!!!!")
else:
    if bingo == 5:
        
        if bonus_bingo == 1:
            print("You are 2nd!!!")
        else:
            print("You are 3rd!!")
            
    else:
       if bingo == 4:
           print("You are 4th!")
       else:
            if bingo == 3:
                print("You are 5th...")