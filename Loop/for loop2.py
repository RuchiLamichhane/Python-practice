#sum of all even number from 0 to 20
sum=0
for i in range (0,21):
  if i%2==0 :
   sum=sum +i
print(sum)


#print the triangle with numbers
#1
#12
#123
#1234
#12345
#using nested for loop
n=int(input("Enter a number:"))
for i in range (1,n+1) :
  for j in range(1,i) :
    print(j,end='')
  print()

  





