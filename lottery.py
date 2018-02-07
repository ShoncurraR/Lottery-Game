from random import randint

NewNumber = 0
Lottery = []
MyNumber = []
RightNumbers = 0

print ("Welcome to the Lottery Game!!!!!!!!")

while(len(Lottery) < 5):
    iNewNumber = randint(1,20)
    if(iNewNumber not in Lottery):
        Lottery.append(iNewNumber)

while(len(MyNumber) < 5):
    try:
        NewNumber = int(input("Pick a number between 1-20:\n"))
    except ValueError:
        print("Try again")
        continue
    

    if NewNumber in MyNumber:
        print("Please no duplicates")
    else:
        print("I SAID ONLY NUMBERS 1-20")

    if(NewNumber not in MyNumber and (int(NewNumber) <= 20 or int(NewNumber) > 0)):
        MyNumber.append(NewNumber)

for number in Lottery:
    for myNumber in MyNumber:
        if(NewNumber == MyNumber):
            RightNumbers += 1

print ("You have " + str(RightNumbers) + " numbers right!")
print("The lottery numbers were: ")
for num in Lottery:
    print(str(num))

if RightNumbers == 5:
    print("AWWWWW SNAP YOU HIT THE JACKPOT!!!!!!!")
else:
    print("Sorry you lost don't be sad")
