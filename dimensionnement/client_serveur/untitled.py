            fenres=Tk()
            fenres.title("Dimensionnement")
            fenres.geometry("900x350")
            fenres.resizable(True, True)
            fsortie = Frame( fenres, bg ='#80c0c0', bd =5, relief =RAISED)
            fsortie.pack(side=TOP)
            lfsortie=LabelFrame(fsortie,text="Résultats",font="arial 12 bold italic",labelanchor = N,bg='white')
            lfsortie.pack(padx=5, pady=5, expand="yes")
            Label(lfsortie,text="ν (La longueur moyenne de la file d'attente):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=0 ,column=0)
            Label(lfsortie,text="n (Le nombre moyen de clients dans le systéme):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=1 ,column=0)
            Label(lfsortie,text="tf (Le temps moyen d'attente dans la file d'attente):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=2 ,column=0)
            Label(lfsortie,text="ρ (Le nombre de serveurs inoccupés):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=3 ,column=0)
            Label(lfsortie,text=res[0], font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=0 ,column=1)
            Label(lfsortie,text=res[2], font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=1 ,column=1)
            Label(lfsortie,text=res[1], font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=2 ,column=1)
            Label(lfsortie,text=res[3], font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=3 ,column=1)
            fenres.mainloop()