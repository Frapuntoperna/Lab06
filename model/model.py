from model.strumento import Strumento
from model.prestito import Prestito
import mysql.connector
from database.DB_connect import get_connection

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        connettore_database= mysql.connector.connect(option_files="database/connector.cnf")

        query=("SELECT *"
               " FROM STRUMENTO AS S"
               " WHERE S.tipo = %s")

        cursore = connettore_database.cursor()
        cursore.execute(query, (tipo,))
        output_strumenti=[]

        for riga in cursore:
            s = Strumento(codice=riga[0], tipo=riga[1], marca=riga[2], anno_acquisto=riga[3], valore=riga[4], disponibile=riga[5])
            output_strumenti.append(s)

        cursore.close()
        connettore_database.close()
        return output_strumenti
