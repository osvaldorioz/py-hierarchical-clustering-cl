from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
from typing import List
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import hierarchical_clustering
import json

matplotlib.use('Agg')  # Usar backend no interactivo
app = FastAPI()

# Definir el modelo para el vector
class VectorF(BaseModel):
    vector: List[float]
    
def plot_hierarchical_clustering(data, output_file:str):
    merges, num_points = hierarchical_clustering.hierarchical_clustering(data)
    G = nx.Graph()
    
    # Add initial nodes
    for i in range(num_points):
        G.add_node(i, pos=(data[i, 0], data[i, 1]))
    
    # Add edges as clusters merge
    node_id = num_points
    for merge in merges:
        a, b, dist = merge
        G.add_node(node_id, pos=((G.nodes[a]['pos'][0] + G.nodes[b]['pos'][0]) / 2,
                                 (G.nodes[a]['pos'][1] + G.nodes[b]['pos'][1]) / 2))
        G.add_edge(a, node_id, weight=dist)
        G.add_edge(b, node_id, weight=dist)
        node_id += 1
    
    # Draw the graph
    pos = nx.get_node_attributes(G, 'pos')
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=300, font_size=8, edge_color=weights,
            edge_cmap=plt.cm.Blues, width=2)
    plt.title("Hierarchical Clustering (Complete Linkage)")
    #plt.show()
    plt.savefig(output_file)
    plt.close()

@app.post("/hierarchical-linkage")
def calculo(n_points: int, n_clusters: int):
    output_file = 'hierarchical_clustering_complete_linkage.png'
    data = np.random.rand(n_points, n_clusters) 
    plot_hierarchical_clustering(data, output_file)
    
    j1 = {
        "Grafica": output_file
    }
    jj = json.dumps(str(j1))

    return jj

@app.get("/hierarchical-linkage-graph")
def getGraph(output_file: str):
    return FileResponse(output_file, media_type="image/png", filename=output_file)