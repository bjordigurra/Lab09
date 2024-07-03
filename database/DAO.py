from database.DB_connect import DBConnect
from model.flight import Flight
from model.airport import Airport
from model.rotta import Rotta


class DAO():

    @staticmethod
    def getAllFlights():  # prende tutti i voli, ci lavoro dopo con python
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from flights """
        cursor.execute(query)

        for row in cursor:
            result.append(Flight(row["ID"], row["AIRLINE_ID"], row["FLIGHT_NUMBER"],
                                 row["TAIL_NUMBER"], row["ORIGIN_AIRPORT_ID"],
                                 row["DESTINATION_AIRPORT_ID"], row["SCHEDULED_DEPARTURE_DATE"],
                                 row["DEPARTURE_DELAY"], row["ELAPSED_TIME"], row["DISTANCE"],
                                 row["ARRIVAL_DATE"], row["ARRIVAL_DELAY"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from airports "
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"],
                                  row["CITY"], row["STATE"], row["COUNTRY"], row["LATITUDE"],
                                  row["LONGITUDE"], row["TIMEZONE_OFFSET"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRotte():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
        select ORIGIN_AIRPORT_ID , DESTINATION_AIRPORT_ID , avg(DISTANCE) as media
        from flights 
        group by concat(least(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID), '|', greatest(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID))
        order by ORIGIN_AIRPORT_ID
        """
        cursor.execute(query)
        # la query raggruppa i voli con partenza e destinazione scambiate creando una stringa a p
        # partire dagli id degli aeroporti di partenza e destinazione, in modo che sia la stessa per
        # voli con partenza e destinazione scambiati

        for row in cursor:
            result.append(Rotta(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["media"]))
        cursor.close()
        conn.close()
        return result
