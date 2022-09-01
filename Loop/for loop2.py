'''#sum of all even number from 0 to 20
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
  print()'''


  #using nested for loop acessing the elements of a matrix
  #matrix as a list containing list
  #take 2 such matrix from user and get sum

r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))
X=[]
val=[]
for i in range(0,r):
    for j in range(0, c):
      val.insert(j,int(input("Enter the %d * %d element : " %(i,j))))
    X.insert(i,val)
    val=[]
Y=[]
for i in range(0, r):
    for j in range(0, c):
      val.insert(j,int(input("Enter the %d * %d element : " % (i, j))))
    Y.insert(i, val)
    val=[]
sum=[]

for i in range(0, r):
  for j in range(0, c):
    val.insert(j, X[i][j]+Y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)





