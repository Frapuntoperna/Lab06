from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

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
        lista_strumenti_2 = []
        cnx=get_connection()
        if cnx is not None:
            cursor=cnx.cursor()
            query='SELECT * FROM STRUMENTO'
            cursor.execute(query)

            for riga in cursor:
                lista_parti_strumenti=[]
                lista_parti_strumenti.append(riga[0])
                lista_parti_strumenti.append(riga[1])
                lista_parti_strumenti.append(riga[2])
                lista_parti_strumenti.append(riga[3])
                lista_parti_strumenti.append(riga[4])
                lista_parti_strumenti.append(riga[5])
                lista_strumenti_2.append(lista_parti_strumenti)

        return lista_strumenti_2



    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        lista_strumenti_ricerca=[]
        for lista in self.get_strumenti():
            for i in lista:
                if lista[1]==tipo:
                    lista_strumenti_ricerca.append(lista)

        return lista_strumenti_ricerca
