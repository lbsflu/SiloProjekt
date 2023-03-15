from silo import Silo
from siloVerwaltung import SiloVerwaltung
if __name__ == '__main__':
    silo = Silo(1, 50.0)

    print(silo.einlagern(20.0))
    print(silo.einlagern(5.0))
    #print(silo.auslagern(10.0))











