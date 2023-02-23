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



    # Edge Attribute Setup
    edges = []
    for i in (data.graph.edges):
        edges.append((namenumlist.get(i.get("source")), namenumlist.get(i.get("target"))))
    g.add_edges(edges)



    return g



def plotGraph(g):
    fig, ax = plt.subplots(figsize=(10,10))
    ig.plot(
    g,
    layout = "kk",
    target=ax,
    )    
    plt.show()    

def prepareDataV2(file):

    # data = pd.read_json(file)
    f = open(file)
    data = json.load(f)

    # Callitself2(data)
    Callitself2(data)


temparrnodes = []
temparredges = []
def Callitself2(object, nodes = [], edges = []):
    
    for i in (object):
        
        if loopCall(object):

            # if (type(object[i]) == list):
                # for metadata in i.get("metadata"):
                    # print(object[i])

            if (i == "metadata"):
                for metadata in object[i]:
                    if (metadata not in temparrnodes):
                        temparrnodes.append(metadata)
            if (i == "label"):
                if (i not in temparrnodes):
                    temparrnodes.append(i)
            Callitself2(object[i])
 

    
        if (type(i) == dict):
            if ("metadata" in i):
                for metadata in i.get("metadata"):
                    if (metadata not in temparredges):
                        temparredges.append(metadata)

        # if (type(i) == dict and "metadata" not in i):
            # print(i)
            # for attributes in i:
                # if (attributes != "source" and attributes != "target" and attributes not in temparredges):
                    # print(attributes)
                    # temparredges.append(i)
fakearray = []
hasname = False
def Callitself(object):

    # print(*object, " " + str(type(object)))
    # for *x, in (object):
        # print(x)

    for i in (object):
        if loopCall(object):
            if(type(object[i]) != str):
                Callitself(object[i])
        # if loopCall(i):
            # print(i)
            # Callitself(data[i])


    # print(type(data))
    # print(*data)

    # Callitself(data)


def loopCall(object):
    for i in object:
        # if (type(object) == dict and type(object[i]) != int and object[i].__len__()):
        if (type(object) == dict and type(object[i]) != int):           
            return True
        else:
            return False


def main():
    # g = prepareData("les_miserablesv2.json")
    # plotGraph(g)
    # testing = []
    # prepareDataV2("les_miserablesv2.json")
    prepareDataV2("les_miserables.json")
    print("Edges: "+str(temparredges))
    print("Nodes: "+str(temparrnodes))

if __name__ == "__main__":
    main()