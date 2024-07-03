from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._flights = DAO.getAllFlights()
        self._rotte = DAO.getAllRotte()
        # creazione grafo
        self._grafo = nx.Graph()
        self._idMap = {}
        for airport in self._airports:
            self._idMap[airport.id] = airport
        self._mappa_rotte = {}

    def crea_mappa_rotte(self):
        """
        self._mappa_rotte = {}
        for flight in self._flights:
            if (flight.origin_airport_id, flight.destination_airport_id) in self._mappa_rotte
                or (flight.destination_airport_id, flight_origin_id) in self._mappa_rotte:
        """

    def buildGraph(self, distance):
        self._grafo = nx.Graph() # azzero il grafo ogni volta che chiamo la funzione
        self._grafo.add_nodes_from(self._airports)
        # terzo modo (più veloce) per popolare il grafo con i voli
        # allFlights = DAO.getAllFlights()
        for rotta in self._rotte:
            if rotta.distance >= distance:
                #partenza = self._idMap[flight.origin_airport_id]
                #destinazione = self._idMap[flight.destination_airport_id]
                self._grafo.add_edge(rotta.id_aeroporto_partenza, rotta.id_aeroporto_arrivo, rotta=rotta)
                print(f"Added edge between {rotta.id_aeroporto_partenza} and {rotta.id_aeroporto_arrivo}")

    @property
    def airports(self):
        return self._airports

    def getNumNodes(self): # restituisce il numero di nodi NON ISOLATI (con almeno un collegamento)
        contatore = 0
        for nodo in nx.degree(self._grafo):
            if nodo[1] != 0: # nodo è una tupla che ha aeroporto e grado
                contatore += 1
        return contatore

    def getNumEdges(self):
        return len(self._grafo.edges)

    @property
    def grafo(self):
        return self._grafo

