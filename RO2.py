import networkx as nx
import matplotlib.pyplot as plt
import gmplot
import heapq 
import folium
import ipywidgets
import math
import tkinter as tk
from IPython.display import display


# **Graph avec networkx**


def listVoisins():
        nodes = list(adjacencies.keys())
        for node in nodes:
            if node in adjacencies:
                print(f"Les voisins de {node} sont :")
                for neighbor in adjacencies[node]:
                    print(f" - {neighbor} : {adjacencies[node][neighbor]} km")
            else:
                print(f"{node} n'est pas présent dans le graphe.")




def graph():
    # créer un nouveau graphe
    global G
    adjacencies = {
    'Genève': {'Vaud': 65.0},
        'Vaud': {'Berne':[105.2,116.1,121.6],'Valais':148.9, 'Fribourg':[86.2,81.8,82.1], 'Neuchatel':69.2},
        'Valais': {'Berne':[200.1,133.0,243.6], 'Uri':[148.3,226.4,368.5], 'Tessin':[177.8,250.7]},
        'Fribourg': {'Berne':35.4},
        'Neuchatel': {'Jura':[68.9,68.7,97.5],'Berne':[52.3,69.9]},
        'Jura':{'Solothurn':[61.0,68.9]},
        'Berne': {'Uri':[172.3,170.3,158.8],'Jura':[106.7,109.9],'Solothurn':[41.1,37.7,40.7], 'Luzern':[190.9,96.4,124.0],'Obwalden':[132.7,102.8,96.2],'Nidwalden':[128.6,126.6,115.1]},
        'Solothurn': {'Basel-Landschaft':[45.6,45.8,45.0],'Aargau':68.4,'Luzern':[82.0,85.7]},
        'Basel-Landschaft': {'Aargau':[60.1,66.7,63.3], 'Basel-Stadt':26.1},
        'Aargau': {'Luzern':[61.7,49.8,49.0], 'Zurich':[36.6,44.7,35.5], 'Zug':[43.4,39.2,59.8],'Basel-Stadt':[70.2,83.6,72.1]},
        'Zurich': {'Schaffhausen':[52.7,46.4,52.5],'Thurgau':[64.5,75.1],'St. Gallen':[86.2,82.8,97.3],'Zug':[33.8,31.5,29.8],'Schwyz':[59.7,54.5,64.2]},
        'Thurgau': {'St. Gallen':[34.4,41.4,41.8],'Schaffhausen':[69.0,55.7,47.5]},
        'St. Gallen': {'Graubunden':[140.7,174.2],'Glarus':[88.6,124.3,96.9],'Schwyz':[114.1,151.4,168.5]},
        'Glarus': {'Graubunden':[107.8,102.3],'Schwyz':[66.4,101.1],'Uri':[111.1,142.3,155.9]},
        'Schwyz': {'Uri':43.7,'Nidwalden':[46.5,63.6],'Luzern':[45.3,34.8],'Zug':[25.8,37.9,28.3]},
        'Uri': {'Graubunden':[196.7,184.4],'Tessin':126.4,'Nidwalden':53.6},
        'Tessin': {'Graubunden':145.3},
        'Luzern':{'Zug':[31.0,33.4],'Obwalden':24.2,'Nidwalden':20.6},
        'Nidwalden':{'Obwalden':26.9}
    }
    G = nx.Graph()
    # ajouter des noeuds au graphe
    nodes = list(adjacencies.keys())
    G.add_nodes_from(nodes)

    for node, neighbors in adjacencies.items():
        for neighbor, distances in neighbors.items():
            if isinstance(distances, float):
                distance = distances
            else:
                distance = min(distances)
            G.add_edge(node, neighbor, weight=distance)

        #print(nx.draw(G, with_labels=True) )       
    return  G



# **Graph avec folium**

# Coordonnées des villes
coords = {
        'Genève': (46.204391, 6.143158),
        'Vaud': (46.561313, 6.536765),
        'Zug':(47.166167, 8.515495),
        'Valais': (46.190461, 7.544923),
        'Fribourg': (46.806403, 7.153656),
        'Neuchâtel': (46.992979, 6.931933),
        'Jura': (46.762475, 5.672916),
        'Berne': (47.313555, 7.444609),
        'Solothurn': (47.208835, 7.532291),
        'Basel-Landschaft': (47.441812, 7.764400),
        'Basel-Stadt':(447.561925, 7.592768),
        'schaffhaussen':(47.707766, 8.641442),
        'Aargau': (47.390434, 8.0457015),
        'Zürich': (47.368650, 8.539183),
        'thurgau': (47.6321, 9.1087),
        'st.Gallen': (47.424482, 9.376717),
        'Glarus': (47.040427, 9.067208),
        'Graubunden':(46.656987, 9.578026),
        'schwyz': (47.020714, 8.652988),
        'uri': (41.486065, -71.530854),
        'Tessin': (46.331734, 8.800453),
        'Luzern': (47.050038, 8.308929),
        'nidwalden': (46.926702, 8.384998),
        'obwalden': (46.877858, 8.251249)
    }

# show map types using ipywidgets et folium

# widget
def foliumMap():
        select_widget=ipywidgets.Select(
        options=['Open Street Map', 'Terrain', 'Toner', 'Watercolor', 'Positron', 'Dark Matter'],
        value='Open Street Map',
        description='Map Type:',
        disabled=False)

        # Initialisation de la carte centrée sur la Suisse
        m = folium.Map(location=[46.8182, 8.2275], zoom_start=8)

        # Ajout des marqueurs pour chaque ville
        for ville, coord in coords.items():
            folium.Marker(location=coord, popup=ville).add_to(m)
            
        # Affichage de la carte
        return m
        

# widget function
def select(map_type):
    
    if map_type == 'Open Street Map':
        display(foliumMap())
    if map_type == 'Terrain':
        display(folium.Map(location=[46.815514 , 8.224472], tiles='Stamen Terrain', zoom_start=8, height=400))
    if map_type == 'Toner':
        display(folium.Map(location=[46.815514 , 8.224472], tiles='Stamen Toner', zoom_start=8, height=400))
    if map_type == 'Watercolor':
        display(folium.Map(location=[46.815514 , 8.224472], tiles='Stamen Watercolor', zoom_start=8, height=400))
    if map_type == 'Positron':
        display(folium.Map(location=[46.815514 , 8.224472], tiles='CartoDB Positron', zoom_start=8, height=400))
    if map_type == 'Dark Matter':
        display(folium.Map(location=[46.815514 , 8.224472], tiles='CartoDB Dark_Matter', zoom_start=8, height=400))
        #if map_type == 'Satellite':
        #    display(folium.Map(location=[46.815514 , 8.224472], tiles='CartoDB positron', zoom_start=8, height=400))
        # interaction between widgets and function    
    select_widget=ipywidgets.Select(
        options=['Open Street Map', 'Terrain', 'Toner', 'Watercolor', 'Positron', 'Dark Matter'],
        value='Open Street Map',
        description='Map Type:',
        disabled=False)    
    ipywidgets.interact(select, map_type=select_widget)
        


# **algorithms** 


#dijkstra

def dijkstra():

    cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
           "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", 
           "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais","Neuchatel", "Genève", "Jura"]

 
    # Define a function to validate user input for canton selection
    def validate_canton(canton):
        return canton in cantons

    city1 = input("Donner le point de départ : ")
    if not validate_canton(city1):
        print("Invalid input. Please enter a valid canton.")
        dijkstra()

    city2=input("Donner le point d'arrivée : ")
    if not validate_canton(city2):
        print("Invalid input. Please enter a valid canton.")
        dijkstra()

    distance = nx.dijkstra_path_length(G, city1, city2)
    path = nx.dijkstra_path(G, city1, city2)
    print(f"The shortest path between {city1} and {city2} is: {path}")
    print(f"The shortest distance between {city1} and {city2} is: {distance} km") 

        





#bellman_ford
def bellman_ford():

    cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
           "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", 
           "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais","Neuchatel", "Genève", "Jura"]

        
        

    # Define a function to validate user input for canton selection
    def validate_canton(canton):
        return canton in cantons
       
    city1 = input("Donner le point de départ : ")
    if not validate_canton(city1):
        print("Invalid input. Please enter a valid canton.")
        bellman_ford()
    city2 = input("Donner le point d'arrivée : ")
    if not validate_canton(city2):
        print("Invalid input. Please enter a valid canton.")
        bellman_ford()
    
    # Calculate the shortest path and distance between two cities using Bellman-Ford algorithm

    path = list(nx.bellman_ford_path(G, source=city1,target=city2))
    distance = nx.bellman_ford_path_length(G, city1, city2)
        
    # Print the shortest path and distance
    print(f"The shortest path between {city1} and {city2} is: {path}")
    print(f"The shortest distance between {city1} and {city2} is: {distance} km")
        



def shortest_path(adjacencies, start, goal):
        
    start = input("Donner le point de départ : ")
    goal=input("Donner le point d'arrivée : ")

    # Create a dictionary to store the distances from the start node to all other nodes
    distances = {node: float('inf') for node in adjacencies}
    distances[start] = 0

    # Create a priority queue to store the nodes to be visited
    queue = [(0, start)]  # (distance, node)

    # Create a dictionary to store the previous node in the shortest path
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Check if the current node is the goal
        if current_node == goal:
            path = []
            while current_node in previous:
                path.append(current_node)
                current_node = previous[current_node]
            path.append(start)
            path.reverse()
            return path

        # Check if the current distance is smaller than the recorded distance for the current node
        if current_distance > distances[current_node]:
            continue

        # Explore the neighboring nodes
        neighbors = adjacencies[current_node]
        for neighbor, distance in neighbors.items():
            if isinstance(distance, list):
                min_distance = min(distance)  # Use the minimum distance if multiple distances are available
            else:
                min_distance = distance

            new_distance = current_distance + min_distance

            # Check if the new distance is smaller than the recorded distance for the neighbor
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

        # If no path is found
        return None




#depth first search (profoundeur d'abord)
def dfs_path():
        
    cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
           "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", 
           "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais","Neuchatel", "Genève", "Jura"]

    
    # Define a function to validate user input for canton selection
    def validate_canton(canton):
        return canton in cantons
    
    start = input("Donner le point de départ : ")
    if not validate_canton(start):
        print("Invalid input. Please enter a valid canton.")
        dfs_path()

    goal =input("Donner le point d'arrivée : ")
    if not validate_canton(goal):
        print("Invalid input. Please enter a valid canton.")
        dfs_path()
            
        
    visited = set()  # ensemble des noeuds déjà visités
    stack = [(start, [start])]  # pile contenant les noeuds à visiter et leur chemin parcouru jusqu'à présent
        
    
    while stack:
        (node, path) = stack.pop()  # noeud actuel et chemin parcouru jusqu'à présent
        visited.add(node)  # ajouter le noeud actuel à l'ensemble des noeuds visités
        path_found = False  # reset path_found to False at the beginning of each iteration
        if node == goal:
            print("le chemin trouvé est: "+ str(path))  # chemin trouvé
            path_found = True
            break  # exit the loop when the goal is found
        for neighbor in G[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))  # ajouter le voisin à la file avec son chemin parcouru jusqu'à présent
    if path_found == False:
        print("aucun chemin trouvé")

        

#breadth first search
def bfs_path():
    cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
        "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", 
        "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais","Neuchatel", "Genève", "Jura"]

       
        

    # Define a function to validate user input for canton selection
    def validate_canton(canton):
        return canton in cantons

    start = input("Donner le point de départ : ")
    if not validate_canton(start):
        print("Invalid input. Please enter a valid canton.")
        bfs_path()
    goal =input("Donner le point d'arrivée : ")
    if not validate_canton(goal):
        print("Invalid input. Please enter a valid canton.")
        bfs_path()
        
    visited = set()  # ensemble des noeuds déjà visités
    queue = [(start, [start])]  # file contenant les noeuds à visiter et leur chemin parcouru jusqu'à présent
        
    
    while queue:
        (node, path) = queue.pop(0)  # noeud actuel et chemin parcouru jusqu'à présent
        visited.add(node)
        path_found = False  # reset path_found to False at the beginning of each iteration
        if node == goal:
            print("le chemin trouvé est: "+ str(path))  # chemin trouvé
            path_found = True
            break  # exit the loop when the goal is found
        for neighbor in G[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # ajouter le voisin à la file avec son chemin parcouru jusqu'à présent
    if path_found == False:
        print("aucun chemin trouvé")


#bidirectional search algorithm
def bidirectional_search():
    cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
        "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", 
        "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais","Neuchatel", "Genève", "Jura"]

    # Define a function to validate user input for canton selection
    def validate_canton(canton):
        return canton in cantons

    start = input("Donner le point de départ : ")
    if not validate_canton(start):
        print("Invalid input. Please enter a valid canton.")
        bidirectional_search()
    goal =input("Donner le point d'arrivée : ")
    if not validate_canton(goal):
        print("Invalid input. Please enter a valid canton.")
        bidirectional_search()

    forward_visited = set()
    backward_visited = set()
    forward_parent = {}
    backward_parent = {}

    forward_visited.add(start)
    backward_visited.add(goal)

    intersect_node = None
    path = []

    while len(forward_visited) > 0 and len(backward_visited) > 0:
        # Forward search
        current_node = forward_visited.pop()
        for neighbor in G.neighbors(current_node):
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_parent[neighbor] = current_node

            if neighbor in backward_visited:
                intersect_node = neighbor
                break

        if intersect_node is not None:
            break

        # Backward search
        current_node = backward_visited.pop()
        for neighbor in G.neighbors(current_node):
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_parent[neighbor] = current_node

            if neighbor in forward_visited:
                intersect_node = neighbor
                break

        if intersect_node is not None:
            break

    if intersect_node is not None:
        # Construct the path from start to goal
        path.append(intersect_node)
        node = forward_parent[intersect_node]
        while node != start:
            path.append(node)
            node = forward_parent[node]
        path.append(start)
        path.reverse()

        # Extend the path from goal to intersect
        node = backward_parent[intersect_node]
        while node != goal:
            path.append(node)
            node = backward_parent[node]
        path.append(goal)

        print("le chemin trouvé est: "+ str(path))
    else:
        # No path was found
        print("aucun chemin trouvé")
    


