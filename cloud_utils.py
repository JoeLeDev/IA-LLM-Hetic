import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

if not ACCESS_TOKEN:
    print("Erreur : Le token d'accès n'est pas défini dans le fichier .env")
    exit(1)



def download_file_from_dropbox(dropbox_path, local_path):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    try:
        with open(local_path, "wb") as f:
            metadata, res = dbx.files_download(path=dropbox_path)
            f.write(res.content)
        print(f"Fichier téléchargé avec succès : {local_path}")
    except dropbox.exceptions.ApiError as e:
        print(f"Erreur lors du téléchargement : {e}")
        if e.error.is_path() and e.error.get_path().is_conflict():
            print("Conflit de fichiers : le fichier existe déjà.")
        else:
            print("Erreur spécifique de l'API Dropbox :", e.error)

dropbox_path = "/Sanji.pdf"  
local_path = "pdf/Sanji.pdf"  

download_file_from_dropbox(dropbox_path, local_path)
