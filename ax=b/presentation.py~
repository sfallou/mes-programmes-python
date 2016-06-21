from Tkinter import *
from gauss import *
def getMatriceId(n):
	        m = [[0 for j in range(0, n)] for i in range(0, n)]
	        for i in range(n):
	            m[i][i] = 1
        	return m

def produitMatrice( mat1, mat2, n):
		p = MatriceNull(n)
		for i in range(n):
			for j in range(n):
				for k in range(n):
					p[i][j] += mat1[i][k] * mat2[k][j]
		return p
	

def traceMat( mat, n):
	        trc = 0
	        for i in range(n):
	            trc += mat[i][i]
        	return trc

def matrice_diff( mat1, mat2, n):
	        m = MatriceNull(n)
	        for i in range(n):
	            for j in range(n):
	                m[i][j] = mat1[i][j] - mat2[i][j]
	        return m
	
def scal_mult_mat( mat, n, scal):
	        m = MatriceNull(n)
	        for i in range(n):
	            for j in range(n):
	                m[i][j] = mat[i][j] * scal
	        return m


def determinant( mat, n):
	        t = [0 for j in range(0, n)]
	        q = [0 for j in range(0, n)]
	        c = [MatriceNull(n) for j in range(0, n)]
	        b = [MatriceNull(n) for j in range(0, n)]
	        #initialisation
	        Id = getMatriceId(n)
	        c[0] = mat
	        t[0] = traceMat(c[0], n)
	        t_mult_id =  scal_mult_mat(Id, n, t[0])
	        b[0] = matrice_diff(c[0], t_mult_id, n)
	 
	        for i in range(1, n):
	            c[i] = produitMatrice(b[(i - 1)], mat, n)
	
	            t[i] = (1.0 / (i + 1)) * traceMat(c[i], n)
	            t_mult_id =  scal_mult_mat(Id, n, t[i])
	            b[i] = matrice_diff(c[i], t_mult_id, n)
	        for i in range(n):
	            q[i] = (t[i] * -1)
	        det = 0
	        if((n % 2) == 0):
	            det = q[n - 1]
	        else:
	            det = q[n - 1] * -1
	        return det
	        #print(det) 

def PolynomeCaracteristique( mat, n):
	        t = [0 for j in range(0, n)]
	        q = [0 for j in range(0, n)]
	        c = [MatriceNull(n) for j in range(0, n)]
	        b = [MatriceNull(n) for j in range(0, n)]
	        #initialisation
	        Id = getMatriceId(n)
	        c[0] = mat
	        t[0] = traceMat(c[0], n)
	        t_mult_id =  scal_mult_mat(Id, n, t[0])
	        b[0] = matrice_diff(c[0], t_mult_id, n)
	        

	        for i in range(1, n):
	            c[i] = produitMatrice(b[(i - 1)], mat, n)
	
	            t[i] = (1.0 / (i + 1)) * traceMat(c[i], n)
	            t_mult_id =  scal_mult_mat(Id, n, t[i])
	            b[i] = matrice_diff(c[i], t_mult_id, n)
	        for i in range(n):
	            q[i] = (t[i] * -1)
	        #print q
	        #print (getPoly(q, n))
	        return getPoly(q,n)

def getPoly( q, n):
	        poly = ""
	
	        if((n % 2) == 0):
	            poly += "X^" + str(n)
	        else:
	            poly += "-X^" + str(n)
	            for i in range(n):
	                q[i] = q[i] * -1
	                #pour la derniere valeur on a pas besoin de X
	                if (i== n-1):
	                	if (q[i]>0):
	                		poly +="+"+str(q[i])
	                	else:
	                	    poly +=str(q[i])
	                	#on saute l'etape
	               		continue

	                #si q est positif il faut mettre un plus devant	    
	                if q[i] >= 0:
	                    poly += "+" + str(q[i]) + "X^" + str(n - (i + 1))
	                else:
	                    poly += str(q[i]) + "X^" + str(n - (i + 1))
	        return poly

def MatriceNull( n):
	        return [[0 for j in range(0, n)] for i in range(0, n)]


class SimpleTableInput(Frame):
    def __init__(self, parent, rows, columns):
        Frame.__init__(self, parent)
        
        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = Entry(self, validate="key", validatecommand=vcmd, justify=CENTER, font=("Helvetica", 15), width=3)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if ((P.strip() == "")|(P.strip() == "-")):
            return True
        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True



def ordreMat():
	frameMat = Frame (panel)
	frameMat.pack()
	global taille
	taille=int(entree.get())
	if (taille<0):
		print ("erreur")
	else:
		taille=int(entree.get())

		Matrice(frameMat).pack(side="top", fill="both", expand=True)

def afficherResult():
	affichePoly = PolynomeCaracteristique(matrice, taille)
	afficheDet = str (determinant(matrice, taille))
	Label(frameResult, text=" Le determinant est :").pack()
	Label(frameResult, text=afficheDet).pack()
	Label(frameResult, text=" Le polynome carateristique est :").pack()
	Label(frameResult, text=affichePoly).pack()

class Matrice(Frame):
    def __init__(self, parent):
    	Frame.__init__(self, parent)
    	self.table = SimpleTableInput(self, taille, taille) # 3 est l'ordre de la matrice
    	self.submit = Button(self, text="VALIDER", command=self.on_submit)
    	self.back = Button(self, text="QUITTER", command=fenetre.destroy)
    	self.table.pack(side="top", expand=True)
    	self.submit.pack(side=RIGHT)
    	self.back.pack(side=LEFT)
    def on_submit(self):
        global matrice
        matrice=self.table.get() # On recupere la matrice
        #afficherResult()
        gauss(matrice,taille)
        
        #print (matrice)            # On affiche la matrice
        


# ----- Programme principal : -----


#Creation de la fenetre principale
fenetre = Tk()
fenetre.title("Matrice")
panel=PanedWindow(orient=VERTICAL)
panel.pack(expand='yes', fill='both')

frameDescription=Frame(panel)
frameDescription.pack()
Label(frameDescription, text="ce programme vous permet de \n "
						"1-Determiner le polynome caracteristique\n"
						"2-Calculer le Determinant d'une matrice              ").pack()

frameOrdreMat = Frame(panel)
frameOrdreMat.pack()
Label(frameOrdreMat, text="donner la taille de votre matrice", fg="red").pack()
entree=Entry(frameOrdreMat)
entree.pack()
Button(frameOrdreMat, text="valider",command=ordreMat).pack()

frameResult = Frame(panel).pack()

fenetre.mainloop()
