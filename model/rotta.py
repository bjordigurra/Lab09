from dataclasses import dataclass

@dataclass
class Rotta:
    _id_aeroporto_partenza: int
    _id_aeroporto_arrivo: int
    _distance: float

    """
    def calcola_distanza(self):
        distanza = 0
        count = 0
        allFlights = DAO.getAllFlights()
        for flight in allFlights:
            if flight.origin_airport_id == self._id_aeroporto_partenza and flight.destination_airport_id == self._id_aeroporto_arrivo:
                distanza += flight.distance
                count += 1
                
    """

    def __str__(self):
        return f"Partenza: {self._id_aeroporto_partenza} - Destinazione: {self.id_aeroporto_arrivo} (distanza {self._distance})"

    @property
    def distance(self):
        return self._distance

    @property
    def id_aeroporto_partenza(self):
        return self._id_aeroporto_partenza

    @property
    def id_aeroporto_arrivo(self):
        return self._id_aeroporto_arrivo
