import networkx as nx

from model.model import Model

mymodel = Model()
mymodel.buildGraph(977)

print(f"The graph has {mymodel.getNumNodes()} nodes.")
print(f"The graph has {mymodel.getNumEdges()} edges.")

edges = nx.get_edge_attributes(mymodel.grafo, "volo").values()

for nodo in nx.degree(mymodel.grafo):
    print(nodo)

