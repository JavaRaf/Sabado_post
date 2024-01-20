import os

# Recebe a variável de ambiente MY_SECRET
my_secret = os.environ.get('test_tok')

# Verifica se a variável de ambiente foi definida
if my_secret:
    print(f"O valor da variável de ambiente MY_SECRET é: {my_secret}")
else:
    print("A variável de ambiente MY_SECRET não está definida.")
