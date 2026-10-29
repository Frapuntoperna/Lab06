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
    def bottone_interfaccia_cerca_sezione_4(self, e):
        tipo = self._view.testo_tipo_strumento_view.value
        strumenti = self._model.cerca_strumenti_per_tipo(tipo)
        self._view.lista_strumenti_ricerca.controls.clear()
        if not strumenti:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text("Nessuno strumento trovato.")
            )
        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(
                    ft.Text(f"Codice: {s.codice} - Tipo: {s.tipo} - Marca: {s.marca}")
                )
        self._view.update()