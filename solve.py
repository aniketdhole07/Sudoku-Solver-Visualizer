import os
  
from time import sleep 
  

def clear():
 os.system( 'clear' )
 
  

clear() 

sud= [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
        
n=9
m=9
def disp(sud):
 for i in range(n):
  if(i==0 or i%3==0):
   print("-------------------------")  
  for j in range(m):
   if(j==0 or j%3==0):
    print("|",end=' ')
   if(sud[i][j]==0):
    print("_",end=' ')
   else:  
    print(sud[i][j],end=' ')
   if(j==m-1):
    print("|",end=' ')
  print()  
  if(i==n-1):
   print("-------------------------")   

def possible(a,b,c):   #Check if Number is valid at Position
 for i in range(0,n):   #Check for row
  if(sud[a][i]==c and i!=a):
   return False
 for j in range(0,m):   #Check for column
  if(sud[j][b]==c and i!=b):
   return False 
 bx=a//3
 by=b//3
 for i in range(bx*3,bx*3+3): #Check for box
  for j in range(by*3,by*3+3):
   if(sud[i][j]==c and i!=a and j!=b):
    return False

 return True  


def slv1():
 
 for i in range(9):
  for j in range(9):
   if(sud[i][j]==0):
    for t in range(1,10):
     if(possible(i,j,t)):
      sud[i][j]=t
      disp(sud)
      sleep(0.1)
      clear()
      if(slv1()):
       return True
      else:
       sud[i][j]=0
    return False
 return True   

slv1()  
disp(sud)

