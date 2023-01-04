'''programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. '''

usuario = str(input ("digite seu usario: "))
while True:
  senha = str (input ("digite a sua senha: "))
  if usuario == senha:
      print("troque sua senha.")
     
  else:
    print("tudo certo.")
    break