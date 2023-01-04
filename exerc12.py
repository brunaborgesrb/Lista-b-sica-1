'''programa que peça uma nota, entre 0 e 10. Mostre uma mensagem caso o valor seja inválido e
 continue pedindo até que o usuário informe um valor válido.'''

 
while True:
  n = int (input ("digite um numero de 0 a 10: "))
  if n >= 0 and n <=10:
      print("numero valido")
      break
  else:
      print ("numero invalido. tente novamente.")'''