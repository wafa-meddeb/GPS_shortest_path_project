import tkinter as tk
import nbimporter
from nbimporter import NotebookLoader
import RO2

#loader = NotebookLoader() 
#module = loader.load_module('RO1.ipynb')
#dijkstra = module.dijkstra(G, city1, city2)


fenetre = tk.Tk()
fenetre.title("Interface graphique")

# ajouter une fonction pour gérer la fermeture de la fenêtre
def fermer_fenetre():
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", fermer_fenetre)

# label
label = tk.Label(fenetre, text="Bienvenue", font=("Arial", 20))
label1 = tk.Label(fenetre, text="Voici la carte géographique",font=("Arial", 16))
label.pack()
label1.pack()

# entrée
#entree = Entry(fenetre, width=30)
#entree.pack()
#entree.insert(0, "Entrez votre phrase ici")

# checkbutton
#bouton = Checkbutton(fenetre, text="Nouveau?")
#bouton.pack()

# création de la variable qui stockera la valeur sélectionnée
#value = StringVar() 
# valeur par défaut à None pour aucun bouton radio sélectionné
#value.set(None)
# création des boutons radio
#bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
#bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
#bouton3 = Radiobutton(fenetre, text="Peut être", variable=value, value=3)
# affichage des boutons radio dans la fenêtre
#bouton1.pack()
#bouton2.pack()
#bouton3.pack()

# liste
liste = tk.Listbox(fenetre, font=("Arial", 16),width=40)
#liste.insert(1, "    Veuillez choisir une méthode de recherche:    ")
label = liste.insert(1, "     Veuillez choisir une méthode de recherche:   ")

#liste.insert(2, "1-Dijkstra")
#liste.insert(3, "2-Bellman-Ford")
#liste.insert(4, "3-Largeur")
#liste.insert(5, "4-Profondeur")
# obtenir le nombre d'éléments dans la liste
nb_elements = liste.size()
# ajuster la hauteur de la Listbox en fonction du nombre d'éléments
liste.config(height=nb_elements)
liste.pack()

#Dijkstra_botton =Button(master, option=value,activeforeground="grey",command=print("Dijkstra"))
#Dijkstra_botton.pack()
G = RO2.graph()
b1 = tk.Button(fenetre, text="Dijkstra", relief="raised", width=25, command= RO2.dijkstra).pack()
b2 = tk.Button(fenetre, text="Bellman-Ford", relief="raised", width=25, command= RO2.bellman_ford).pack()
b3 = tk.Button(fenetre, text="Largeur", relief="raised", width=25, command= RO2.bfs_path).pack()
b4 = tk.Button(fenetre, text="Profondeur", relief="raised", width=25, command= RO2.dfs_path).pack() 
b5 = tk.Button(fenetre, text ="bidirectional", relief="raised", width=25, command= RO2.bidirectional_search).pack()

# canvas
canvas = tk.Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

fenetre.geometry("600x800+{}+{}".format(int(fenetre.winfo_screenwidth() / 2 - 400), 
                                       int(fenetre.winfo_screenheight() / 2 - 300)))

# scale
value = tk.DoubleVar()
value1=tk.DoubleVar()
scale = tk.Scale(fenetre, variable=value, from_=0, to=500, orient="horizontal", length=600)
scale1 = tk.Scale(fenetre, variable=value1, from_=0, to=500, orient="vertical", length=580)
scale.pack()
scale1.pack()
scale.place(relx=1, rely=0.75, anchor="ne")
scale1.place(relx=0.9, rely=0, anchor="ne")


liste = tk.Listbox(fenetre, font=("Arial", 15), height=5, width=30)
# obtenir le nombre d'éléments dans la liste
nb_elements = liste.size()
# ajuster la hauteur de la Listbox en fonction du nombre d'éléments
liste.config(height=nb_elements)


# démarrage de la boucle principale Tkinter
fenetre.mainloop()