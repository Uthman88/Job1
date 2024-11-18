import tkinter as tk
from tkinter import ttk


# Fonction pour réinitialiser la partie
def recommencer():
    global tour, grille, joueur_x, joueur_o
    # Réinitialisation de la grille
    grille = []
    for i in range(3):
        ligne = ["", "", ""]
        grille.append(ligne)
    tour = "X"  # Le premier tour commence avec le joueur X
    for i in range(3):
        for j in range(3):
            boutons[i][j].config(text="", state=tk.NORMAL, bg="SystemButtonFace", fg="black")
    label_tour.config(text="Tour de X")
    label_gagnant.config(text="")
    update_score()


# Fonction pour vérifier si quelqu'un a gagné
def verifier_victoire():
    global joueur_x, joueur_o
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "":
            colorier_gagnants([(i, 0), (i, 1), (i, 2)])
            return grille[i][0]
        if grille[0][i] == grille[1][i] == grille[2][i] != "":
            colorier_gagnants([(0, i), (1, i), (2, i)])
            return grille[0][i]

    if grille[0][0] == grille[1][1] == grille[2][2] != "":
        colorier_gagnants([(0, 0), (1, 1), (2, 2)])
        return grille[0][0]

    if grille[0][2] == grille[1][1] == grille[2][0] != "":
        colorier_gagnants([(0, 2), (1, 1), (2, 0)])
        return grille[0][2]

    return None


# Fonction pour colorier les boutons gagnants
def colorier_gagnants(cells):
    for i, j in cells:
        boutons[i][j].config(bg="lightgreen")


# Fonction pour vérifier si le jeu est en égalité
def verifier_egalite():
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "":
                return False
    return True


# Fonction pour mettre à jour le score et l'affichage du tour
def update_score():
    label_score_x.config(text=f"Joueur X\n  {joueur_x}")
    label_score_o.config(text=f"Joueur O\n  {joueur_o}")


# Fonction qui est appelée quand un bouton est cliqué
def jouer(i, j):
    global tour, joueur_x, joueur_o
    if grille[i][j] == "" and label_gagnant.cget("text") == "":
        # Mettre à jour la grille et le bouton
        grille[i][j] = tour
        # Définir la couleur en fonction du joueur
        couleur_texte = "red" if tour == "X" else "blue"

        # Mettre à jour le texte et la couleur du bouton sans le désactiver
        boutons[i][j].config(text=tour, fg=couleur_texte, font=("Arial", 40))

        # Vérifier la victoire
        gagnant = verifier_victoire()
        if gagnant:
            if gagnant == "X":
                joueur_x += 1
                label_gagnant.config(text="Félicitations, X a gagné!", fg="green")
            else:
                joueur_o += 1
                label_gagnant.config(text="Félicitations, O a gagné!", fg="green")
        elif verifier_egalite():  # Si égalité
            for i in range(3):
                for j in range(3):
                    boutons[i][j].config(bg="yellow")  # Colorier tous les boutons en jaune
            label_gagnant.config(text="Égalité !")
        else:
            # Changer le tour
            tour = "O" if tour == "X" else "X"
            label_tour.config(text=f"Tour de {tour}")

        update_score()


# Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Tic-Tac-Toe")

# Logo de la fenêtre
logo = tk.PhotoImage(file="tic-tac-toe.png")
fenetre.iconphoto(True, logo)

# Taille de la fenêtre
fenetre.geometry("400x500")
fenetre.resizable(False, False)  # Interdire le redimensionnement

# Variables globales
joueur_x = 0
joueur_o = 0
tour = "X"
grille = []
for i in range(3):
    ligne = ["", "", ""]
    grille.append(ligne)

# Interface graphique
frame_score = tk.Frame(fenetre)
frame_score.grid(row=0, column=0, columnspan=3, pady=10)

label_score_x = tk.Label(frame_score, text=f"Joueur X\n  {joueur_x}", font=("Arial", 16), fg="black")
label_score_x.grid(row=0, column=0, padx=20, sticky="w")

label_tour = tk.Label(frame_score, text=f"Tour de {tour}", font=("Arial", 20, "bold"), fg="black")
label_tour.grid(row=0, column=1)

label_score_o = tk.Label(frame_score, text=f"Joueur O\n  {joueur_o}", font=("Arial", 16), fg="black")
label_score_o.grid(row=0, column=2, padx=20, sticky="e")

label_gagnant = tk.Label(fenetre, text="", font=("Arial", 18, "italic"), fg="green")
label_gagnant.grid(row=1, column=0, columnspan=3, pady=10)

# Création des boutons pour la grille
boutons = [[None for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        boutons[i][j] = tk.Button(fenetre, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda i=i, j=j: jouer(i, j))
        boutons[i][j].grid(row=2 + i, column=j, padx=0, pady=0, sticky="nsew")  # Pas d'espaces entre les boutons

# Configurer la grille pour occuper toute la fenêtre
for i in range(3):
    fenetre.grid_rowconfigure(i + 2, weight=1)  # Les lignes pour la grille
    fenetre.grid_columnconfigure(i, weight=1)  # Les colonnes pour la grille

# Bouton pour recommencer la partie
button_recommencer = tk.Button(fenetre, text="Recommencer", font=("Arial", 14, "bold"), command=recommencer)
button_recommencer.grid(row=5, column=0, columnspan=3, pady=10)

# Lancement de l'application
fenetre.mainloop()
