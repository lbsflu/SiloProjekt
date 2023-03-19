class SiloVerwaltung:
    _silo_gesamt_kapazitat = 0.0
    _silo_gesamt_bestand = 0.0
    _silo_list = []

    def __init__(self, silo_list: list):

        self._set_silo_list(silo_list)

    def set_silo_gesamt_kapazitat(self):
        for silo in self.get_silo_list():
            self._silo_gesamt_kapazitat += silo.get_kapazitat()

    def get_silo_gesamt_kapazitat(self) -> float:
        return self._silo_gesamt_kapazitat

    def set_silo_gesamt_bestand(self):
        for silo in self.get_silo_list():
            self._silo_gesamt_bestand += silo.get_bestand()

    def get_silo_gesamt_bestand(self):
        return self._silo_gesamt_bestand

    def _set_silo_list(self, silo_list: list):
        self._silo_list = silo_list

    def get_silo_list(self):
        return self._silo_list
