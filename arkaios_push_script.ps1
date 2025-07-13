# arkaios_push_script.ps1
# Script de carga inicial para el repositorio arkaios‑genesis‑log
# ⚠️ Contiene PAT en texto plano. Úsalo solo localmente y bórralo después.

cd C:\repos\arkaios-genesis-log
git init

# Configura el remoto con autenticación PAT incrustada
git remote add origin https://Arymusmeth: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@github.com/Arymusmeth/arkaios-genesis-log.git

# Añade todos los archivos (incluido el MANIFIESTO)
git add .

# Commit firmado por Arkaios Bot
git commit -m "🔖 ARKAIOS génesis – manifiesto inicial" --author "Arkaios Bot <arkaios@localhost>"

# Asegura rama principal llamada main
git branch -M main

# Sube a GitHub
git push -u origin main
