import subprocess
import dropbox
import pdfplumber
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
print("Token chargé : ", ACCESS_TOKEN)

file_path = './pdf/Sanji.pdf'
extracted_text_path = './filespdf/downloaded-file.txt'

def download_file_from_dropbox(dropbox_path, local_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            metadata, res = dbx.files_download(path=dropbox_path)
            f.write(res.content)
        print(f"Fichier téléchargé avec succès : {local_path}")
    except dropbox.exceptions.ApiError as e:
        print(f"Erreur lors du téléchargement : {e}")

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_extracted_text(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def ask_with_rag(question):
    with open(extracted_text_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    prompt = f"Voici un texte sur une personne : \n{file_content}\n\nQuestion : {question}\nRéponds uniquement à la question, sans aucun texte supplémentaire."

    command = ['ollama', 'run', 'llama3.2', prompt]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Erreur : {result.stderr.strip()}"

def main():
    download_file_from_dropbox("/Sanji.pdf", file_path)
    document_text = extract_text_from_pdf(file_path)
    save_extracted_text(document_text, extracted_text_path)

    question = input("What do you want to know? : ")
    response_with_rag = ask_with_rag(question)
    print(f"Réponse générée avec RAG: {response_with_rag}")

if __name__ == "__main__":
    main()
