# IA Q-learning - Jeu de nim

Ce projet implémente une intelligence artificielle basée sur l'algorithme de **Q-learning** pour jouer au jeu des allumettes. L'objectif est d'entraîner un robot à jouer de manière optimale en apprenant à partir de nombreuses parties simulées.

## Principe du jeu

Le jeu des allumettes est un jeu à deux joueurs où chacun retire entre 1 et 3 allumettes d'un tas commun. Le joueur qui prend la dernière allumette perd la partie.

## Algorithme utilisé : Q-learning

L'algorithme de **Q-learning** est une méthode d'apprentissage par renforcement qui permet au robot d'améliorer sa stratégie en mettant à jour une table de valeurs **Q** associée aux états du jeu.

### Paramètres d'apprentissage
- **Alpha (taux d'apprentissage)** : 0.1
- **Gamma (facteur de récompense)** : 0.8
- **Récompense de victoire** : +1
- **Récompense de défaite** : -1
- **Épsilon (exploration vs exploitation)** : diminue progressivement pour favoriser l'exploitation à mesure que l'agent apprend.

## structure du projet

- `main.py` : Code principal contenant l'implémentation du Q-learning et l'entraînement du robot.
- `README.md` : Ce fichier décrivant le projet.

## Exécution du programme

1. Assurez-vous d'avoir **Python** installé sur votre machine.
2. Créer un environnement virtuel (venv) :
   ```bash
   python3 -m venv venv
   ```
3. Activer l'environnement virtuel :

   pour windows:
   ```bash
   .\venv\Scripts\activate  
   ```
   pour linux:
   ```bash
   ./venv/bin/activate
   ```

4. Installer les differents packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Lancer le programme :

   pour windows:
   ```bash
   python3 .\main.py
   ```
   pour linux:
   ```bash
   python3 ./main.py
   ```

6. Quitter l'environnement :
   ```bash
   deactivate
   ```

## Phases du programme

1. **Entraînement du robot** :
   - Un grand nombre de parties sont simulées (20 000 par défaut).
   - La table **Q** est mise à jour après chaque partie pour améliorer les décisions du robot.
2. **Phase de jeu** :
   - Le joueur humain affronte le robot entraîné.
   - Le robot applique la meilleure stratégie apprise pour maximiser ses chances de gagner.

## Résultats et statistiques

À la fin de l'entraînement, le programme affiche des statistiques sur les performances du robot et sa probabilité de victoire en fonction du nombre d'allumettes restantes.

## Améliorations possibles

- Ajouter une interface graphique pour rendre le jeu plus interactif.
- Expérimenter avec d'autres méthodes d'apprentissage par renforcement.
- Affiner les hyperparamètres pour améliorer l'efficacité de l'entraînement (alpha & gamma).

## Auteur

Projet développé par Louis Verbrugge

