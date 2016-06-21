
from Tkinter import *
import tkMessageBox

def ajoutFenetre() : 
	fenetre = Tk()
	cadre = Frame(fenetre, borderwidth=1)
	cadre.pack(fill=BOTH)
	fenetre.geometry('350x200+275+105')
	fenetre.title('Operations sur matrices')

	champ_label = Label(fenetre, text="Selectionnez le type d'operations a faire:")
	champ_label.pack()

	val = StringVar()

	inverse = Radiobutton(fenetre, text="Calcul de l'inverse", variable=val, value="inv")
	inverse.pack()
	
	produit = Radiobutton(fenetre, text="Produit de deux matrices", variable=val, value="pro")
	produit.pack()

	somme = Radiobutton(fenetre, text="Somme de deux matrices", variable=val, value="som")
	somme.pack()

	valide = Button(fenetre, text="Validez", bg="green", font="arial 10 bold", command=lambda:saisiNombreLigneColonne(val.get()))
	valide.pack()

	bouton = Button(fenetre, text="Quitter", bg="red", font="arial 10 bold", command=fenetre.quit)
	bouton.pack()
	return fenetre

def saisiNombreLigneColonne(typeOp) :
	fenetre.withdraw()
	fenetre1=Toplevel(fenetre)
	fenetre1.geometry('350x275+275+105')
	fenetre1.title('Operations sur matrices')
	fenetre2= Frame(fenetre1)
	fenetre2.pack()
	cadre1= Frame(fenetre1 ,padx=0)
	cadre1.pack()
	if typeOp=="inv" or typeOp=="som":
		ligneLabel=Label(fenetre2, text="Nombre de lignes:", width=20,height= 2, font="arial 10 bold")
		ligneLabel.pack()
		ligneEntry=Entry(fenetre2, width=14)
		ligneEntry.pack()
		colLabel=Label(fenetre2, text="Nombre de colonnes:", width=20,height= 2, font="arial 10 bold")
		colLabel.pack()   
		colEntry=Entry(fenetre2,width=14)
		colEntry.pack()
		OK = Button(fenetre2, text='Validez', width=20,height= 2, font="arial 10 bold", command=lambda:test1(ligneEntry.get(), colEntry.get(), typeOp))
		OK.pack()
	if typeOp=="pro":
		ligneLabel1=Label(fenetre2, text="Lignes matrice 1:", width=20,height= 2, font="arial 10 bold")
		ligneLabel1.pack()
		ligneEntry1=Entry(fenetre2, width=14)
		ligneEntry1.pack()
		colLabel1=Label(fenetre2, text="Colonne matrice 1:", width=20,height= 2, font="arial 10 bold")
		colLabel1.pack()   
		colEntry1=Entry(fenetre2,width=14)
		colEntry1.pack()
		ligneLabel2=Label(fenetre2, text="Lignes matrice 2:", width=20,height= 2, font="arial 10 bold")
		ligneLabel2.pack()
		ligneEntry2=Entry(fenetre2, width=14)
		ligneEntry2.pack()
		colLabel2=Label(fenetre2, text="Colonne matrice 2:", width=20,height= 2, font="arial 10 bold")
		colLabel2.pack()   
		colEntry2=Entry(fenetre2,width=14)
		colEntry2.pack()
		OK = Button(fenetre2, text='Validez', width=20,height= 2, font="arial 10 bold", command=lambda:test2(ligneEntry1.get(), colEntry1.get(), ligneEntry2.get(), colEntry2.get(), typeOp))
		OK.pack()

def test1(lig1, col1, TypeOp):
	try:
            l1 = int(lig1)
	    c1 = int(col1)
            if l1<=0 or c1<=0:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
            else:
                saisiMatrice(l1, c1, 0, 0, TypeOp)
        except:
	
	    tkMessageBox.showinfo('Erreur',"La taille de la matrice doit etre un entier")
def test2(lig1, col1, lig2, col2, TypeOp):
	try:
            l1 = int(lig1)
	    c1 = int(col1)
	    l2 = int(lig2)
	    c2 = int(col2)
            if l1<=0 or c1<=0 or l2<=0 or c2<=0:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
	    if c1!=l2:
		tkMessageBox.showinfo('Erreur de taille',"Le nombre de lignes de la 1ere matrice doit etre egal au nombre de colonnes de la 2e")
            else:
                saisiMatrice(l1, c1, l2, c2, TypeOp)
        except:
	
	    tkMessageBox.showinfo('Erreur',"La taille de la matrice doit etre un entier")

def saisiMatrice(lig1, col1, lig2, col2, typ):
	try :
	    fenetre.withdraw()
	    fenetreSaisi=Toplevel(fenetre)
	    fenetreSaisi.geometry('750x575+275+105')
	    fenetreSaisi.title('Saisi des matrices')
	    fenetreSaisi2= Frame(fenetreSaisi)
	    fenetreSaisi2.pack()
	    cadreSaisi= Frame(fenetreSaisi ,padx=0)
	    cadreSaisi.pack()
	    cadreSaisi.pack(anchor="nw")
	    for i in range(lig1):
		matcol=list()
		for j in range(col1):
		    p=Entry(cadreSaisi)
		    p.insert(0,'A(%s-%s)' % (i,j))
		    p.grid(row=i,column=j)
		    matcol.append(p)
		matcell1.append(matcol)
	    resButton=Button(cadreSaisi,text='Calculer',font="arial",command=lambda:create_matrice(fenetreSaisi,lig1,col1,lig2,col2,resButton,typ))
	    if lig1>=lig2 :
		i = lig1-1
	    else :
		i=lig2-1
	    resButton.grid(row=i/2,column=col1+1,rowspan=col1+1,columnspan=2)
	    if typ=="som" or typ=="pro" :
		if typ=="som":
			col2=col1
			lig2=lig1
		for i in range(lig2):
		    matcol=list()
		    for j in range(col2):
		        p=Entry(cadreSaisi)
		        p.insert(0,'B(%s-%s)' % (i,j))
		        p.grid(row=i+lig1+5,column=j)
		        matcol.append(p)
		    matcell2.append(matcol)
	except : 
	     tkMessageBox.showinfo("Erreur Saisie ligne/colonne", "Les valeurs saisies sont incorrectes. Veuillez entrer des eniers")

def create_matrice(fenetreSaisi,lig1 ,col1,lig2, col2,resButton,typ) :
    i=0
    try :
        resButton.configure(state=DISABLED)
        global resultatFrame
        while i<lig1:
            j=0 ;
            matcol=list()
            while j<col1 :
                matcol.append(float(matcell1[i][j].get()))
                j+=1
            matrice1.append(matcol)
            i+=1
        
        i=0
        if typ=="pro" or typ=="som" :
            while i<lig2:
                j=0 ;
                matcol2=list()
                while j<col2 :
                    matcol2.append(float(matcell2[i][j].get()))
                    j+=1
                matrice2.append(matcol2)
                i+=1
        if typ=="som" :
            resultat=addition(matrice1,matrice2)
        if typ=="pro" :
                    resultat=multiplier(matrice1,matrice2)
        if typ=="inv" :
                    resultat=inverser(matrice1,lig1,col1)
           
        resultatFrame=Frame(fenetreSaisi)
        for i in range(len(resultat)):
            for j in range(len(resultat[0])):
                    ligneText=StringVar()
                    ligneText.set("{}".format(str(resultat[i][j])))
                    ligneLabel=Label(resultatFrame,textvariable=ligneText, width=20,height= 2, bg='white',font="arial 12 bold",borderwidth=10)
                    ligneLabel.grid(row=i,column=j)
        resultatFrame.pack(anchor="center")
    except:
        tkMessageBox.showinfo("Erreur matrice", "Les elements des matrices ne sont pas correctement remplis. Veuillez reinitialiser et recommencer")

def addition(mat1,mat2):
    resultat = list()
    for i in range(len(mat1)):
        colonne = list()
        for j in range(len(mat1[0])):
            colonne.append(mat1[i][j]+mat2[i][j])
        resultat.append(colonne)
    return  resultat
def multiplier(mat1,mat2):
    resultat = list()
    for i in range(len(mat1)):
        ligne = list()
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat1[0])):
                element= element+ mat1[i][k]*mat2[k][j]
            ligne.append(element)
        resultat.append(ligne)
    return resultat

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
def permutation(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId
def elimination(matrice,identite,pivot,ligne,colonne ) :
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
def remonte(matrice,matId,ligne, colonne ) :
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
    matriceIdentite =identite(matriceIdentite,ligne,colonne)
    k=0
    arret = 1
    while k<ligne and arret == 1 :
        pivot=recherchePivot(matrice,k,ligne)
        if pivot==k :
            matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
        else :
            if pivot==-1 :
                arret = 0
            else :
                matrice,matriceIdentite = permutation(matrice,matriceIdentite,k,pivot)
                pivot = k
                matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
                k=k+1
    if arret==1 and matrice[ligne-1][colonne-1]!=0 :
            matrice,matriceIdentite = remonte(matrice,matriceIdentite,ligne,colonne)
    else :
            matriceIdentite.append(-1) 
    return matriceIdentite

fenetre=ajoutFenetre()
resultatFrame=Frame()
matrice1= list()
matrice2=list()
matcell1 =list()
matcell2=list()
fenetre.mainloop()
