#While loop is used to repeat a section of code for an unknown no.of times until a specific condition is met.


'''#To find multiple of 7
val=int(input("Enter a multiple of 7 : "))
while val%7 !=0 :
  val= int (input("Enter a multiple of 7: "))
else:
  print("%d is a multiple of 7" %val)


#To print string 10 times
i=1
while i<=10:
  print("Simplilearn")
  i+=1 

  #To print string 10 times
i=10
while i>=1:
  print("Simplilearn")
  i-=1 

  #To print sum of first 10 natural number
i=1
sum=0
while i<=10:
  sum=sum+i
  i+=1
print(sum) 

#To print sum of first 10 even number
i = 1
sum = 0
while i <= 10:
  if i%2==0 :
    sum = sum+i
  i += 1
print(sum)
#To print certain code for unknown number of times
#n=5678
#nr=8765
n=int(input("Enter a number: "))
nr=0
while n%10!=0 :
    c=n%10
    nr=nr*10 +c
    n=n//10
print(nr)


#Calculate the lenth of list without using len function/ using try block
X=[1,2.3,"Simplilearn"]
length=0
i=0
try:
  while X[i] :
    length+=1
    i+=1
except IndexError :
    print(length)

#print:
        #1
        #22
        #333
        #4444
        #55555

n= int(input("Enter a number: "))
i=1
while i<=n :
    j=1
    while j<=i :
        print(i,end='')
        j+=1
    i+=1
    print() '''

    
