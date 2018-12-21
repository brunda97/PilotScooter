
import numpy as np 
global n 
global col,d1,d2
#col To check if coordinate lies in same column when n=p
#d1,d2 To check if coordinate lies for left and right diagonal when n=p
col=np.zeros([32],dtype=bool)
d1=np.zeros([32],dtype=bool)
d2=np.zeros([32],dtype=bool)
#c1=0
#Max Activity Point is stored in point
point=0
#f is filename to read input file
f = open("input.txt", "r")
n=int(f.readline())
#no of police officer
p=int(f.readline())
#no of scooters in the file
s=int(f.readline())
#list of coordinates of all scooters
list=f.readlines()
#m matrix to store coordinates for n*n when n=p
m=np.zeros([n,n],dtype=int)
f.close()
#Count of all coordinates where scooter move
count= np.zeros([int(n),int(n)],dtype="int")
for line in list:
        if ',' in line:
          x,y=line.split(",")
          count[int(x)][int(y)]=count[int(x)][int(y)]+1
#print (count)
result=dict()
#print count[np.where(count == count.max())][0]
for i in np.ndindex(count.shape):
  result[i]=count[i]
#print result
#print("\n")
result1= sorted(result, key=result.get, reverse=True)
#for i in result1:
  #print i,result[i]
#To check if its possible to store a particular point in n*n square
resultset=[]
def isSafe(resultset,value):
  if len(resultset)==0:
    return True
  x1,y1=value
  for coordinate in resultset:
    x2,y2=coordinate
    if(x1==x2 or y1==y2 or abs(x1-x2)==abs(y1-y2)):
      return False
  return True

#solution when n!=p
solutionset=[]
def solution1(arr, data, start,end, index, r) :
    global solutionset
    if (index == r):
          count=0
          #print data
          for i in data:
            #print result[i]
            count=count+result[i]
          solutionset.append(count)
          #data.pop()
          return
    
  
    for i in range(start,end+1):
      var1=end-i+1
      var2=r-index
      if (var1>=var2):
        #print "Data appended",arr[i]
        if isSafe(data,arr[i]):
          data.append(arr[i])
          solution1(arr, data, i+1, end, index+1, r)
          data.pop()

#solution when n==p
def solve(r,n):
 # global c1
  global point
  total=0
  if(r==n):
    #c1=c1+1
    for i in range(n):
      for j in range(n):
        if(m[i][j]==1):
          total=total+count[i][j]   
    if(point<=total):
      point=total
    return 
  for c in range(n):
    if(col[c]==False and d1[r-c+n-1]==False and d2[r+c]==False):
      col[c]=d1[r-c+n-1]=d2[r+c]=1
      m[r][c]=1
      solve(r+1,n)
      col[c]=d1[r-c+n-1]=d2[r+c]=0
      m[r][c]=0   


data=[]
#print result1
if p>=n:
  solve(0,n)
else:
   solution1(result1,data,0, len(result1)-1, 0, p)
   point=max(solutionset)
  
#print "Max Points is",point
#print count
#print c1

f1=open("output.txt","w")
f1.write("%d"%point)
f1.close()




