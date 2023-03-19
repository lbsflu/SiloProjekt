import random
from silo import Silo
from siloVerwaltung import SiloVerwaltung

if __name__ == '__main__':
    silo_verwaltung = SiloVerwaltung

    silo_list = []
    number = 1
    while number < 3:
        globals()['silo_%s' % number] = Silo(number, round(random.uniform(80.00, 100.00)))

        print(f"Silo Nummer: {globals()['silo_%s' % number].get_silonummer()}")
        print(f"Silo Kapazitat: {globals()['silo_%s' % number].get_kapazitat()}")
        globals()['silo_%s' % number].einlagern(round(random.uniform(10.00, 80.00)))
        globals()['silo_%s' % number].einlagern(round(random.uniform(10.00, 80.00)))
        print(f"Silo Bestand: {globals()['silo_%s' % number].get_bestand()}")

        silo_list.append(globals()['silo_%s' % number])

        number += 1

    siloVerwaltung = SiloVerwaltung(silo_list)

    print(f" Gesamt kapazitat:{siloVerwaltung.get_silo_gesamt_kapazitat()}")

    print(f" Gesamt bestand:{siloVerwaltung.get_silo_gesamt_bestand()}")

    print(f" Gesamt Silos:{siloVerwaltung.get_silo_total()}")
