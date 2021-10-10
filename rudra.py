import random
k=random.randint(1,100)
y=input("do you want to play number gusseing game (yes/no) : ")
y=y.lower()
if y=="yes":
    print("rule -> you cannot guess more than  10 times  ")
while y=="yes":
    i=int(input("guess the number between 1 to 100 : "))
    m=1
    while m<10:
      m=m+1
      if i==k:
          print(f"you won :) \n no of attempt  {m-1}")
          break 
      elif i<k:
          print("no. is too low enter again :")
      else:
          print("no. is to high enter again :")
      i=int(input())

    if m>=10:
         print(f"Game Over :( \n Hidden no. is {k}")
        
    y=input("do you want to play again : ")
    y=y.lower()
    

print(" Thank you ")