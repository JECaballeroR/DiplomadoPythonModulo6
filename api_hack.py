import subprocess
import requests

api_port = 8000
api_url = f"http://0.0.0.0:{api_port}"

try:
    r = requests.get(api_url)
    if r.ok:
        print("La API ya esta corriendo :)")
except requests.exceptions.ConnectionError:
    print("Inicializando la API...")
    cmd = ["uvicorn", "api:app"]
    subprocess.Popen(cmd, close_fds=True)
