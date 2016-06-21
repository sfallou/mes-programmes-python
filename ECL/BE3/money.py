# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:46:43 2016

@author: nicol
"""

from numpy import zeros
from numpy import array

#L=[[1,5],[2,5],[5,100],[10,2],[20,1],[50,1],[100,0],[200,5]]
S=10

def Glouton(S,L):
    M=[]
    n=len(L)
    k=200
    if S==0:
        return M
    else:
        while k>S:
            n=n-1
            k=L[n]
        M=M+[L[n]]+Glouton(S-k,L)
    return (M)
    

def Glouton2(S,L):
    M=[]
    n=len(L)
    k=200
    if S==0:
        return M
    else:
        while k>S:
                n=n-1
                k=L[n][0]
        while L[n][1]==0:
            n=n-1
        k=L[n][0]
        L[n][1]=L[n][1]-1
        M=M+[L[n][0]]+Glouton2(S-k,L)
    return (M)   
    
#print (Glouton2(S,L))

def Monnaie(S,M):
    n=len(S)
    mat=zeros([n,M+1])
    for i in range (0,n):
        for m in range(0,M+1):
            if m==0 :
                mat[i][m]=0
            elif i==0:
                mat[i][m]=1000
            else:
                if m-S[i]>=0:
                    a=1+mat[i][m-S[i]]
                else:
                    a=1000
                if i>=1:
                    b=mat[i-1][m]
                else:
                    b=1000
                mat[i][m]=min(a,b)
    print(mat[n-1][M])
               

S=[0,1,2]
M=7


def Monnaie2(S,M):
    L=[]
    n=len(S)
    mat=zeros([n,M+1])
    for i in range (0,n):
        for m in range(0,M+1):
            if m==0 :
                mat[i][m]=0
            elif i==0:
                mat[i][m]=1000
            else:
                if m-S[i]>=0:
                    a=1+mat[i][m-S[i]]
                else:
                    a=1000
                if i>=1:
                    b=mat[i-1][m]
                else:
                    b=1000
                mat[i][m]=min(a,b)
    U=M
    while U>0:
        G=1000
        k=1
        s=1
        for i in range (0,n):
            if mat[i][U]==1:
                L=L+[S[i]]
                U=U-1
                k=0
            else:
                if G>mat[i][U]:
                    G=mat[i][U]
                    s=i
        if k==1:
            L=L+[S[s]]
            U=U-S[s]
    
            
            
        
        
                         
                
                
#    a=0
 #   for m in range (0,M+1):
  #      b=a
   #     a=1000
    #    for i in range(0,n):
     #       if mat[i][m]<a and mat[i][m]>=b:
      #          a=mat[i][m]
       #         c=S[i]
        #    else :
         #       c=0        
        #L=L+[c]        
    
    print(mat[n-1][M],L)
    print(mat)

Monnaie(S,M)        