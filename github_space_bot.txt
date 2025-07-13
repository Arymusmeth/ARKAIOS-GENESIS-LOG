import requests
import base64

GITHUB_TOKEN = "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"
REPO_OWNER = "Arymusmeth
REPO_NAME = "ARKAIOS-GENESIS-LOG"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

def list_repo_files(path=""):
    url = f"{API_URL}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    return r.json()

def get_file_content(path):
    url = f"{API_URL}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        content = r.json()["content"]
        return base64.b64decode(content).decode('utf-8')
    return None

def create_or_update_file(path, content, message="Automated commit"):
    url = f"{API_URL}/contents/{path}"
    get_resp = requests.get(url, headers=HEADERS)
    sha = None
    if get_resp.status_code == 200:
        sha = get_resp.json()["sha"]
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }
    if sha:
        data["sha"] = sha
    r = requests.put(url, headers=HEADERS, json=data)
    return r.json()

def delete_file(path, message="Automated delete"):
    url = f"{API_URL}/contents/{path}"
    get_resp = requests.get(url, headers=HEADERS)
    if get_resp.status_code == 200:
        sha = get_resp.json()["sha"]
        data = {
            "message": message,
            "sha": sha,
            "branch": "main"
        }
        r = requests.delete(url, headers=HEADERS, json=data)
        return r.json()
    return None

# Ejemplo de uso:
# files = list_repo_files()                  # Listar archivos raíz del repo
# content = get_file_content("archivo.txt")  # Leer archivo
# create_or_update_file("nuevo.txt", "Hola ChatGPT!")  # Crear o actualizar archivo
# delete_file("viejo.txt")                   # Eliminar archivo