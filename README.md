
# IA-LLM-Hetic

## Description
Ce projet permet de télécharger un fichier PDF depuis Dropbox, d'en extraire le texte, puis de l'utiliser pour répondre à des questions via un modèle de langage basé sur RAG (Retrieval-Augmented Generation). Le texte est d'abord extrait à l'aide de `pdfplumber`, puis sauvegardé localement. Ensuite, les utilisateurs peuvent poser des questions sur le contenu extrait et obtenir des réponses générées via un modèle d'IA.

## Fonctionnalités
- Téléchargement de fichiers depuis Dropbox.
- Extraction de texte à partir de fichiers PDF.
- Utilisation de l'IA (modèle de langage) pour répondre à des questions basées sur le texte extrait du PDF.
- Sauvegarde du texte extrait dans un fichier local.
- Interface en ligne de commande pour interagir avec le système.

## Prérequis
- Python 3.x
- Un compte Dropbox avec un token d'accès API valide
- Les bibliothèques Python suivantes :
  - `dropbox`
  - `pdfplumber`
  - `python-dotenv`
  - `subprocess` (inclus par défaut)
  
## Installation

### 1. Cloner le dépôt

 
git clone https://github.com/JoeLeDev/hetic-Ia.git
cd IA-LLM-Hetic


### 2. Créer un environnement virtuel et l'activer


python3 -m venv venv
source venv/bin/activate  
venv\Scripts\activate   


### 3. Installer les dépendances


pip install -r requirements.txt


### 4. Configuration de l'API Dropbox

Crée un fichier `.env` dans le répertoire racine du projet et ajoute-y votre `ACCESS_TOKEN` Dropbox.

 
ACCESS_TOKEN=your_dropbox_access_token


### 5. Lancer le programme

Pour télécharger un fichier depuis Dropbox, extraire le texte et poser une question sur le contenu extrait, lancez le script principal :

 
python main.py
python3 main.py #sur mac



### 6. Exemple d'utilisation

Une fois que le programme est lancé, vous pourrez poser une question sur le contenu extrait du fichier PDF, comme suit :


What do you want to know? : Quelle est la profession de Sanji ?
Réponse générée avec RAG: Sanji est un cuisinier.


## Structure des fichiers
- `main.py` : Contient la logique principale du programme.
- `requirements.txt` : Liste des dépendances Python.
- `.env` : Fichier de configuration pour l'API Dropbox (ne pas partager ce fichier en ligne).
- `pdf/` : Dossier contenant les fichiers PDF téléchargés.
- `filespdf/` : Dossier où le texte extrait des fichiers PDF est sauvegardé.


