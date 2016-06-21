def matInv:
 
def MatriceNull( n):
  return [[0 for j in range(0, n)] for i in range(0, n)]

def MatriceId(n):
    m = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(n):
         m[i][i] = 1
    return m

def pij(line,col,n):
  m = MatriceId(n)
  for i in range(n):
      ech = m[i][line]
      m[i][line] = m[i][col]
      m[i][col]  = ech
  return m

def som(l,u,i,j):
  s=0
  for k in range(0,i-1):
      s += l[i][k]*u[k][j]

def lu(a,n):
  u = MatriceNull(n)
  l = MatriceNull(n)
  u[0][0] = a[0][0]
  for j in range(1,n):
      u[0][j] = a[0][j]
      l[j][0] = a[j][0]/a[0][0]

  for i in range(1,n):
      for k in range(0,i-1):
          sm = som(l,u,i,i)
      u[i][i] = a[i][i] - sm
      for j in range(i+1,n):
          u[i][j] = a[i][j] - som(l,u,i,j)
          l[j][i] = 1/u[i][i]*(a[j][i] - som(l,u,j,i)
   u[n][n] = a[n][n] - som(l,u,j,i)          
 
def LuSolve(a,l,u,n):
  for i in range(n):
    for j in range(n):
      for k in range(min(i,j)):
        a[i][j] +=l[i][k]*u[k][j]
      u[i][j] = a[i][j] -som(l,u,i,j)
      l[i][j] = a[i][j] - som(l,u,j,i) 


def min(i,j):
  if (i<j):
    return i
  else
    return j
    
