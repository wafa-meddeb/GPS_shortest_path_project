import tkinter as tk
import nbimporter
from nbimporter import NotebookLoader
import RO2
import folium
import ipywidgets

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
label = tk.Label(fenetre, text="Bienvenue à la Suisse", font=("Arial", 20), fg="red")
label1 = tk.Label(fenetre, text="Voici la carte géographique: ",font=("Arial", 16))
label.pack()
label1.pack()

# Load the image file
image_file = tk.PhotoImage(file="mapImage.PNG")

# Create a label widget and display the image in it
image_label = tk.Label(fenetre, image=image_file)
image_label.pack()



# liste
liste = tk.Listbox(fenetre, font=("Arial", 16),width=40)
#liste.insert(1, "    Veuillez choisir une méthode de recherche:    ")
label = liste.insert(1, "     Veuillez choisir une méthode de recherche:   ")


# obtenir le nombre d'éléments dans la liste
nb_elements = liste.size()
# ajuster la hauteur de la Listbox en fonction du nombre d'éléments
liste.config(height=nb_elements)
liste.pack(pady= 20)

#Dijkstra_botton =Button(master, option=value,activeforeground="grey",command=print("Dijkstra"))
#Dijkstra_botton.pack()
G = RO2.graph()
b1 = tk.Button(fenetre, text="Dijkstra", relief="raised", width=25, command= RO2.dijkstra).pack()
b2 = tk.Button(fenetre, text="Bellman-Ford", relief="raised", width=25, command= RO2.bellman_ford).pack()
b3 = tk.Button(fenetre, text="Largeur", relief="raised", width=25, command= RO2.bfs_path).pack()
b4 = tk.Button(fenetre, text="Profondeur", relief="raised", width=25, command= RO2.dfs_path).pack() 
b5 = tk.Button(fenetre, text ="bidirectional", relief="raised", width=25, command= RO2.bidirectional_search).pack()



fenetre.geometry("600x800+{}+{}".format(int(fenetre.winfo_screenwidth() / 2 - 400), 
                                       int(fenetre.winfo_screenheight() / 2 - 300)))




liste = tk.Listbox(fenetre, font=("Arial", 15), height=5, width=30)
# obtenir le nombre d'éléments dans la liste
nb_elements = liste.size()
# ajuster la hauteur de la Listbox en fonction du nombre d'éléments
liste.config(height=nb_elements)


# démarrage de la boucle principale Tkinter
fenetre.mainloop()