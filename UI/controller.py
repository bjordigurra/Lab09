import flet as ft
import networkx as nx
import operator


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        # controllo dato in input
        if self._view._txtIn.value == "" or self._view._txtIn.value.isdigit() is False:
            self._view.create_alert("Inserire un numero valido!")
            return

        # creazione grafo con i voli già filtrati
        self._model.buildGraph(int(self._view._txtIn.value)) # passo il parametro della distanza
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi (non isolati)."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nEdges} archi."))
        # .values() restituisce una lista di flights a partire dal grafo (oggetto Flight è attributo dell'edge)
        # altrimenti è solo un dizionario con tupla (partenza, destinazione) e value il volo
        rotte = list(nx.get_edge_attributes(self._model.grafo, "rotta").values())
        # senza list() è un "dict_values", che non ha il sort

        rotte.sort(key=operator.attrgetter("_distance"))

        for rotta in rotte:
            self._view._txt_result.controls.append(ft.Text(f"{self._model.airports[rotta.id_aeroporto_partenza].airport} - "
                                                           f"{self._model.airports[rotta.id_aeroporto_arrivo].airport} - "
                                                           f"Distanza media: {rotta.distance}"))

        self._view.update_page()
