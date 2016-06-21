from math import *
n = 0 # Init matrix size (Global Variable)
############################### Fonctions utiles ################################


#fonction de creation d'une matrice de type (n,p)
# avec initialisation d'une valeur X
def creer_matrice(n, p, X) :
  A = n * [None]
  for i in range(n) :
    A[i ] = p * [X]
  return A

def CreerListe(n):
    return [0.0 for i in range(n)]

def identite(identite,ligne,colonne) :
    i,j=0,0
    while i<ligne :
        matligne = list()
        while j <colonne :
            if i==j :
                matligne.append(1)
            else :
                matligne.append(0)
            j=j+1
        identite.append(matligne)
        i=i+1
        j=0
    return identite

def recherchePivot(matrice,k,ligne) :
    i=k
    while i < ligne:
        if matrice[i][k]!= 0 :
            return i
        i=i+1
    return -1

def permutation1(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId

def elimination1(matrice,identite,pivot,ligne,colonne ) :
    i=0
    while i < ligne :
       j=0
       if i!=pivot and matrice[i][pivot]!=0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite

def remonte1(matrice,matId,ligne, colonne ) :
    pivot,i=0,0
    while pivot<ligne :
        b=matrice[pivot][pivot]
        while i<colonne:
            a=matrice[pivot][i]
            d=matId[pivot][i]
            matrice[pivot][i]= float(a) / float(b)
            matId[pivot][i]= float(d) / float(b)
            matId[pivot][i]=format(matId[pivot][i],'.2f')
            i+=1
        pivot+=1
        i=0
    return matrice,matId

def inverser(matrice,ligne,colonne):
    matriceIdentite = list()
    matriceIdentite =identite1(matriceIdentite,ligne,colonne)
    k=0
    arret = 1
    while k<ligne and arret == 1 :
        pivot=recherchePivot(matrice,k,ligne)
        if pivot==k :
            matrice,matriceIdentite =elimination1(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
        else :
            if pivot==-1 :
                arret = 0
            else :
                matrice,matriceIdentite = permutation1(matrice,matriceIdentite,k,pivot)
                pivot = k
                matrice,matriceIdentite =elimination1(matrice,matriceIdentite,pivot,ligne,colonne)
                k=k+1
    if arret==1 and matrice[ligne-1][colonne-1]!=0 :
            matrice,matriceIdentite = remonte1(matrice,matriceIdentite,ligne,colonne)
    else :
            matriceIdentite.append(-1) 
    return matriceIdentite

#Fonction qui permet de copier une matrice A
#dans une matrice B
def copie_matrice(A) :
  n = len(A)
  B = n * [None]
  for i in range(n) :
    B[i ] = A[i ]
  return B

#Fonction qui renvoit la dimension de la matrice
def dimensions(A) :
  n=len(A)
  p=len(A[0])
  return n,p

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
  for k in range(len(M)-1,-1,-1):
    (M[k][j],M[k][i])=(M[k][i],M[k][j])


"""Fonction qui calcule le produit des diagonales"""
def ProdDiag(M):
  j=0
  p=1
  while j<len(M):     
    p=p*M[j][j]
    j+=1  
  return p

"""Fonction qui triangule une matrice carre--triangulaire superieure--"""
def Triangule(M):
  sign=1
  n=len(M) -1
  for i in range(n,0,-1):#A partir de  la derniere jusqua la 2eme ligne 
    for j in range(0,i):#Mij=0 si j<i
      if M[i][j+1] !=0.0:#Si c'est nulle, jai qu'a faire une permutation pour avoir 0
        q=(M[i][j])/(M[i][j+1]) 
        if q!=0.0:#Si c'est nulle, pas besoin de le rendre nulle
          for k in range(n,-1,-1):#A chaque combinaison, c'est les elements de toute la colonne qui doivent changer
            M[k][j]= M[k][j] - q*M[k][j+1]
      else:
        PermCol(M,j+1,j)
        sign=sign*(-1)#le determinant est multipli par -1 si on permute deux colonnes de la matrice
  return M,sign

"""Fonction qui calcule le determinant une matrice carre"""
def determinant(M):
  (Mtriang,sign)=Triangule(M)
  return round(sign*ProdDiag(Mtriang),2)

########################## Pour Gauss ########################################
def recherchepivot1(k,A):
    i = k
    while i != n and A[i][k] == 0:
        i+=1
    if i != n:
        return i
    else:
        return -1

def permutation1(i0,i,A,b):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination1(k,A,b):
    i=k+1
    while i < n:
        r = A[i][k]/A[k][k]        
        b[i] -= r*b[k]
        j=k
        while j < n:
            A[i][j] -= r*A[k][j]
            j+=1
        i+=1    
    return A,b

def remonte1(A,b):
    x = []
    i = 0
    while i<n:
        x.append(0)
        i+=1        
    x[n-1] = b[n-1]/A[n-1][n-1]
    i = n-2
    while i>=0:    
        x[i] = b[i]            
        j = i+1
        while j<n:
            x[i] -= A[i][j]*x[j]
            j+=1            
        x[i]/=A[i][i]
        i-=1
    return x


####################################Pour LU####################################
def elimination2(k,A,n):
    for i in range(k+1,n):
        r = A[i][k]/A[k][k]        
        for j in range(k,n):
            A[i][j] -= r*A[k][j]
    return A
    
def factoLu(A,b,n):
    arret = 0
    k =0 
    L =[ [0 for i in range(n)] for j in range(n)]
    while k!=n and arret!=1:
        L[k][k] = 1
        if A[k][k] != 0:
            for i in range(k+1,n):
                L[i][k] = A[i][k]/A[k][k]
            elimination2(k,A,n)
            k = k+1
        else:
            arret = 1
    print L
    """arret == 1 and """
    if k ==n :
        result = "\nA est factorisable en LU\n"
        result += remonter(L,A,b,n)
        return result
    else:
        result = "les conditions ne sont pas reunis \n pour une factorisation LU"
        return result
    
#descente
def descente(L,b,n):
    y = []
    i = 0
    #initialisation de y
    while i<n:
        y.append(0)
        i +=1
        
    y[0] = b[0]
    for i in range(1,n):
        y[i] = b[i]
        for j in range(i-1):
            y[i] -= L[i][j]*y[j]
    return y

#remonter
def remonter(L,u,b,n):
    x = []
    #initialisation de x
    i = 0
    while i<n:
        x.append(0)
        i +=1
 
    y = descente(L,b,n)
    result = "Ce systeme a pour solution: "
    x[n-1] = y[n-1]/u[n-1][n-1]
    for i in range(n-2,0,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] -= u[i][j]
        x[i] /= u[i][i] 
    for i in range(n):
        result += "\n x{} = {}".format(i+1, x[i]) 
    return result


#
def subtition_avant(L,b,n):
    z[1] = b[1]
    for i in range(1,n):
        z[i] = (b[i] - som(L,z,i))
    subtition_arriere(L,u,n,z)

####################################### Pour Cholesky##############################

def iteratif(A, b, n,error):
    d = b
    x = initVect(n)
    t = initVect(n)
    r = diff(b,prodMat(A,d,n),n)
    while float(norme(r,n)*norme(r,n) ) > error :
        t = float(produitScal(r,d,n)/produitScal(produitMat(A,d, n),d, n) )
        x =sommeVect(x,produitVectScal(d,t,n), n)
        r = diff(r,produitVectScal(prodMat(A,d,n), t, n),n)
    #resultat
    result ="le resultat vaut: "
    for i in range(n):
        result += "\n x{} = {}".format(i+1, x[i])
    return result
    
#somme de 2 vecteurs
def sommeVect(a,b,n):
    s =initVect(n)
    for i in range(n):
        s[i] = a[i] + b[i]
    return s

#produit d'un vecteur et d'un scalaire
def prodVectScal(a,t,n):
    p =initVect(n)
    for i in range(n):
        p[i] = t*a[i]
    return p

#initialisation d'une matrice
def initMat(n):
    m = [ [0 for i in range(n)] for j in range(n)]
    return m

#initialisation d'un vecteur
def initVect(n):
    d = []
    i = 0
    while i<n:
        d.append(0)
        i+=1
    return d
    
#diffrence de 2 vecteurs
def diff(A,B,n):
    d = initVect(n)
    for i in range(n):
        d[i] = A[i]-B[i]
    
    return d

#produit scalaires de 2 vecteurs
def prodScal(a,b,n):
    p=0
    for i in range(n):
        p +=a[i]*b[i] 
    return p

#produit d'une matrice et d'un vecteur
def prodMat(A, b,n):
    p = initVect(n)
    for i in range(n):
        p[i] =0
        for j in range(n):
            p[i] += A[i][j]*b[i]
    
    return p
#norme d'un vecteur
def norme(A,n):
    norme=0
    for i in range(n):
        norme += A[i]*A[i]
    return sqrt(norme)
