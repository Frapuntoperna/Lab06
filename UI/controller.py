import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def funzione_tasto_mostra_sezione_3(self, e):

        self._view.lista_strumenti.controls.append(ft.Text(f'{self._model.get_strumenti()}'))

        return self._view.lista_strumenti

    def funzione_tasto_cerca_sezione_4(self, e):
        self._view.lista_strumenti_ricerca.controls.append(ft.Text(f'{self._model.cerca_strumenti_per_tipo()}'))
        self._model.tipo=self._view.casella_testo_tipo_sezione_4.value

        return self._view.lista_strumenti_ricerca


        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(
                    ft.Text(f"Codice: {s.codice} - Tipo: {s.tipo} - Marca: {s.marca}")
                )
        self._view.update()
