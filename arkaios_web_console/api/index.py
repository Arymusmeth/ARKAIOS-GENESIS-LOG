from flask import Flask, render_template, request
import os, json, toml

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        command = request.form.get("command", "").lower()
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
    return render_template("index.html", result=result)

# Exportar como handler para Vercel
handler = app
