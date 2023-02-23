import pandas as pd
import igraph as ig
import matplotlib.pyplot as plt

import json


def prepareData(file = "les_miserables.json"):
    
    data = pd.read_json(file)
    g = ig.Graph(data.graph.nodes.__len__())
    

    # Node Attribute Setup
    nodes = []
    groups = []
    namenumlist = {}
    for i in (data.graph.nodes):
        nodes.append(data.graph.nodes[i].get("label"))
        groups.append(data.graph.nodes[i].get("metadata").get("group"))
        namenumlist[data.graph.nodes[i].get("label")] = (nodes.__len__()-1)
    g.vs["label"] = nodes
    g.vs["group"] = groups
    # g.vs["weight"] = str(groups)



    # Edge Attribute Setup
    edges = []
    weight = []
    for i in (data.graph.edges):
        weight.append(str((i.get("metadata").get("value"))))
        # Search the node names and add if
        edges.append((namenumlist.get(i.get("source")), namenumlist.get(i.get("target"))))
    g.vs['weight'] = weight  
    g.add_edges(edges)


    # Group Clustering
    cl = g.community_fastgreedy()
    membership = cl.as_clustering().membership
    membership = groups

    gcopy = g.copy()
    edges = []
    edges_colors = []
    for edge in g.es():
        if membership[edge.tuple[0]] != membership[edge.tuple[1]]:
            edges.append(edge)
            edges_colors.append("gray")
        else:
            edges_colors.append("black")
    gcopy.delete_edges(edges)
    
    layout = gcopy.layout("kk")
    g.es["color"] = edges_colors

    

    return g

def visualstyle(g):

    
    return visual_style


def plotGraph(g):
    partition = ig.VertexClustering.FromAttribute(g, 'weight', '1, 2, 3')
    
    
    visual_style = {}
    visual_style["vertex_label_dist"] = 0
    visual_style["vertex_shape"] = "circle"
    visual_style["edge_color"] = g.es["color"]
    visual_style["vertex_size"] = 0.1
    visual_style["layout"] = "kk"
    visual_style["margin"] = 40
    visual_style["mark_groups"] = partition


    fig, ax = plt.subplots(figsize=(10,10))
    ig.plot(
    g,
    layout = "kk",
    target=ax,
    )

    plt.show()    

# def prepareDataV2(file):

#     # data = pd.read_json(file)
#     f = open(file)
#     data = json.load(f)

#     # Callitself2(data)
#     Callitself(data)



def main():
    g = prepareData("les_miserables.json")

    plotGraph(g)


if __name__ == "__main__":
    main()