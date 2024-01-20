import os
import requests

# Recebe a variável de ambiente test_tok
access_token = os.environ.get('test_tok')

# Substitua 'YOUR_MESSAGE' pela mensagem que você deseja postar
post_message = 'Bocchi'

# Substitua 'https://i.redd.it/5508wlhpleja1.jpg' pela URL da imagem
image_url = 'https://i.redd.it/5508wlhpleja1.jpg'

# URL da API do Facebook Graph para postar uma foto
api_url = 'https://graph.facebook.com/v18.0/me/photos'

# Parâmetros da postagem (mensagem, URL da imagem e token de acesso)
data = {
    'message': post_message,
    'url': image_url,
    'access_token': access_token
}

# Faça a solicitação POST
response = requests.post(api_url, data=data)

# Verifica a resposta
if response.status_code == 200:
    print("Postagem com imagem da internet realizada com sucesso!")
else:
    print(f"Erro {response.status_code}: {response.json()}")
