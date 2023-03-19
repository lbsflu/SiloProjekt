from silo import Silo
from siloVerwaltung import SiloVerwaltung

if __name__ == '__main__':
    silo_list = []

    silo = Silo(1, 50)
    silo2 = Silo(2, 100)
    silo3 = Silo(3, 10)

    silo_list.append(silo)
    silo_list.append(silo2)
    silo_list.append(silo3)

    silo.einlagern(20)
    silo.einlagern(20)

    silo2.einlagern(20)
    silo2.einlagern(80)

    silo3.einlagern(5)
    silo3.einlagern(4)

    siloVerwaltung = SiloVerwaltung(silo_list)

    print(f" Gesamt kapazitat:{siloVerwaltung.get_silo_gesamt_kapazitat()}")

    print(f" Gesamt bestand:{siloVerwaltung.get_silo_gesamt_bestand()}")

    print(f" Gesamt Silos:{siloVerwaltung.get_silo_total()}")
