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

        if voiture in self.listeVoitures:
            print("La voiture existe déjà")
        else:
            if len(self.listeVoitures) < self.capacite:
                self.listeVoitures.append(voiture)
                print("Voiture ajoutée")
            else:
                print("Parc plein")



    def sortirVoiture(self, voiture):

        if voiture in self.listedesVoitures:
            self.listedesVoitures.remove(voiture)
            print("Voiture retirée du parc")
        else:
            print("La voiture n'est pas dans le parc")