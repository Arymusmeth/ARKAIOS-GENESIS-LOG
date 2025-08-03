from flask import Flask, render_template, request
import json, os, toml

app = Flask(__name__, template_folder="../arkaios_web_console/templates")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        command = request.form.get("command", "").lower()
        try:
            if command == "manifest":
                with open("ARKAIOS_SYMBIOTIC_STARTER_v1/symbiotic_manifest.json") as f:
                    result = json.dumps(json.load(f), indent=2)
            elif command == "env":
                with open("ARKAIOS_SYMBIOTIC_STARTER_v1/config.env") as f:
                    result = f.read()
            elif command == "estructura":
                with open("ARKAIOS_SYMBIOTIC_STARTER_v1/estructura.toml") as f:
                    result = toml.dumps(toml.load(f))
            else:
                result = "Comando no reconocido."
        except FileNotFoundError:
            result = "Archivo no encontrado. Verifica que todos los archivos estén incluidos."
    return render_template("index.html", result=result)

# Importante: esta función expone el app para Vercel
def handler(request, response):
    return app(request.environ, response.start_response)
