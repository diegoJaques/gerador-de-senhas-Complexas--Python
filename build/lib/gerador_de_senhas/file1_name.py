import random
import string

tamanho = int(input(" Digite o tamanho de senha desejado: "))
chars = string.ascii_letters + string.digits + "!@#$%&*()+_,Ç;"  # Letters permite car maiuscolo ou minusculo
# digits pega numero de 0 até 0

rnd = random.SystemRandom() # os.urandom  gera numero aleatorio

print("".join(rnd.choice(chars) for i in range(tamanho)))

# .Choise pega caracteres aleatorio