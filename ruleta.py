import random
from random import randint


money = 1000
continueGame= True
print ("Hola ! Tienes", money, "euros.")
print ("Buena suerte!!")
color=["Rojo","Negro"]


  


while continueGame :        
  print("____________________")
  reponse=int(input("A que quieres jugar? Introduce 1 (numero), 2 (color) o 3(Par o impar)"))
  
  if reponse==1:
    number= int(input("A que numero quieres apostar?"))
    while number > 49 or number < 0 :
      print ("Tiene que ser un numero entre 0 y 49")
      number= int(input("Entonces, a que numero quieres apostar?"))
    bet= int(input("Cuanto quieres apostar?"))
    while bet > money or bet < 1 :
      print("No tienes esa cantidad de dinero")
      bet= int(input("Entonces, cuanto?"))
    R= randint(0,49)
    print("Ha salido el numero: ", R)
    if number == R :
      money += 50*bet
      print("Ganaste", 50*bet, "€")
    else :
      money -= bet
      print ("Perdiste, vuelve a intentarlo!")
      print ("Ahora tienes", money , "euros")
     
  if reponse==2:
    color=["Rojo","Negro"]
    col=(input("A que color quieres apostar? (Rojo o Negro)  "))
    while col not in color:
      print("Solo puedes apostar a Rojo o Negro")
      col=input("Entre rojo o negro, a que quieres apostar? (1: Rojo ; 2: Negro" )
    bet= int(input("Cuanto quieres apostar?"))
    while bet > money or bet < 1 :
      print("No tienes esa cantidad de dinero")
      bet= int(input("Entonces, cuanto?"))
    C= random.choice(color)
    print( "Ha salido el color: ", C)
    if col == C :
      money += bet
      print("Ganaste", bet, "€")
    else :
      money -= bet
      print ("Perdiste, vuelve a intentarlo!")
    print ("Ahora tienes", money , "euros")
  if reponse==3:
    P=["Par", "Impar"]
    par=(input("Par o Impar: "))
    while par not in P:
      print("Tienes que apostar Par o Impar")
      par=(input("Par o Impar: "))
    bet= int(input("Cuanto quieres apostar? "))
    while bet > money or bet < 1 :
      print("No tienes esa cantidad de dinero")
      bet= int(input("Entonces, cuanto?"))
    PI=randint(0,49)
    print(" Ha salido el numero: ", PI)
    if PI%2==0 and par=="Par":
      money += bet
      print("Ganaste", bet, "€")
    elif PI%2==1 and par=="Impar":
      money += 2*bet
      print("Ganaste", bet, "€")
    else:
      money -= bet
      print ("Perdiste, vuelve a intentarlo!")
    print ("Ahora tienes", money , "euros")




  if money == 0 :
      continueGame = False
      print ("Lo siento, perdiste todo tu dinero")
      print ("Abandone el juego")
