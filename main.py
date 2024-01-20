import os
import requests

# Recebe a variável de ambiente test_tok
access_token = os.environ.get('fb_tok')

# Substitua 'YOUR_MESSAGE' pela mensagem que você deseja postar
post_message = 'Bocchi'

# Caminho para a imagem local
local_image_path = 'image\sabado.jpg'

# URL da API do Facebook Graph para postar uma foto
api_url = 'https://graph.facebook.com/v18.0/me/photos'

# Abre o arquivo da imagem local
with open(local_image_path, 'rb') as image_file:
    # Parâmetros da postagem (mensagem, arquivo da imagem e token de acesso)
    data = {
        'message': post_message,
        'access_token': access_token
    }

    # Arquivo da imagem é enviado como um arquivo
    files = {
        'source': image_file
    }

    # Faça a solicitação POST com os parâmetros e o arquivo
    response = requests.post(api_url, data=data, files=files)

# Verifica a resposta
if response.status_code == 200:
    print("Postagem com imagem local realizada com sucesso!")
else:
    print(f"Erro {response.status_code}: {response.json()}")

