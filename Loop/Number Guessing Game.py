#guessthe number
# if used wants to exit enter 10
#example 4 digit number:7632

import random
nump=random.randint(1000,9999)
print(nump)
n = int(input("Enter a 4 digit number : "))

while n!=10 :
    num= nump
    cor=0
    while num%10 :
      numc=num%10
      nc=n%10
      num=num//10
      n=n//10
      if numc==nc:
        cor=cor+1
    if cor==4 :
        print("Congrats ! YOu guesses it right")
        break
    else:
        print("%d digits were guessed right" %cor)
        n = int(input("Enter a 4 digit number : "))
else:
  print("You quit the game")