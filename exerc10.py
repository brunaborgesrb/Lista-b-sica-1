'''ler o nome e a idade de um indivíduo e imprimir “criança”, se a idade for menor ou igual a 13 anos, 
“adolescente”, '''

idade = int (input ("digite a sua idade: "))
if idade >= 13 and idade <=17:
  print("adolescente")
elif idade >= 18:
  print("adulto")
else:
  print("criança")