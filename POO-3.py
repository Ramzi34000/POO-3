class Voiture:

    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInfo(self):
        print("Matricule:", self.matricule)
        print("Marque:", self.marque)
        print("Couleur:", self.couleur)


class Parc:

    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listedesVoitures = []

    def entrerVoiture(self, voiture):

        if voiture in self.listedesVoitures:
            print("La voiture existe déjà")
        else:
            if len(self.listedesVoitures) < self.capacite:
                self.listedesVoitures.append(voiture)
                print("Voiture ajoutée")
            else:
                print("Parc plein")



    def sortirVoiture(self, voiture):

        if voiture in self.listedesVoitures:
            self.listedesVoitures.remove(voiture)
            print("Voiture retirée du parc")
        else:
            print("La voiture n'est pas dans le parc")

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.listedesVoitures)

parc1 = Parc(1, "Montreal", 10)
parc2 = Parc(2, "TORONTO", 3)
parc3 = Parc(5, "ALGERIA", 7)


v1 = Voiture("AA212W1", "DODGE", "Noir")
v2 = Voiture("BC12S12", "TOYOTA", "Blanc")
v3 = Voiture("CC333", "BMW", "Rouge")

parc1.entrerVoiture(v1)
parc2.entrerVoiture(v2)
parc3.entrerVoiture(v3)
parc2.sortirVoiture(v2)

print("Places libres:", parc1.calculerNbrPlacesLibres())


