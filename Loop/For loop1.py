#for loop is used to iterate over a sequence which could be list,tuple,array or a string.

#to print:
#1
#6
#simplilearn
X = [1, 6, "Simplilearn"]
for i in X:
  print(i)
 
 #to print :16simplilearn
  x = [1, 6, "simplilearn"]
for i in x:
  print(i, end="")

# To print :
#l
#e
#a
#r
#n
X = "learn"
for i in X:
  print(i)

 #to print from 0 to 5 
for i in range(0, 6):
 print(i)
  

#to print even number from 0 to 21  
for i in range(0, 21, 2):
  print(i)
  
  
  
   # sum of all even number from 0 to 20
sum = 0
for i in range(0, 21):
  if i % 2 == 0:
   sum = sum + i
print(sum)


#print the triangle with numbers
#1
#12
#123
#1234
#12345
#using nested for loop
n = int(input("Enter a number:"))
for i in range(1, n+1):
  for j in range(1, i):
    print(j, end='')
  print()


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

"""Enter number of rows : 2
Enter number of columns : 2
Enter the 0 * 0 element : 1
Enter the 0 * 1 element : 2
Enter the 1 * 0 element : 3
Enter the 1 * 1 element : 4
Enter the 0 * 0 element : 5
Enter the 0 * 1 element : 6
Enter the 1 * 0 element : 7
Enter the 1 * 1 element : 8
[[6,8], [10,12]]"""


