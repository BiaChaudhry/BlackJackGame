import random
# function for user turns in game
def game(myFirstCard,mySecondCard,myCardsTotal,computerFirstCard,computerHiddenCard,computerCardTotal):
	
	 
	for choice in range(1,16):
		choice = input("\nDO YOU WANT TO 'HIT' or 'STAY'\n")
		choice = choice.upper()


		if choice == "STAY" :
			print("\nOK THEN ! computer's turn" )
			#function call for computer's turn as the user stays so this is computer's turn
			computerTurn(computerCardTotal,computerHiddenCard,myCardsTotal)
			break

		elif choice == "HIT":
			
			newCard01 =  random.randint(2,11) 
			print("\nOK THEN take this:\n",newCard01)
			myCardsTotal = (myCardsTotal +  newCard01)
			print("\nyour total now is",myCardsTotal)
			if myCardsTotal <= 21:
				continue
			elif myCardsTotal > 21:
				print("\nyou bust ! computer wins")
				break

	
		
		if myCardsTotal == computerCardTotal:
			print("\n computer wins as this is tie :)\n")
		elif myCardsTotal > 21:
			print("\nyou Bust!\n computer wins \n ")
		elif  myCardsTotal > computerCardTotal :
			print("\nYou win \n ")
		elif  myCardsTotal < computerCardTotal and computerCardTotal <= 21 :
			print("\ncomputer wins \n ")
			
		elif myCardsTotal > computerCardTotal :
			print("\nyou win \n ")
		elif myCardsTotal < computerCardTotal :
			print("\nYou lose computer wins\n")

		elif (myCardsTotal == computerCardTotal) or myCardsTotalNew == computerCardTotal:
			print("\ncomputer wins as this is tie :)\n")

		

#function defined for computer's turn in game
def computerTurn(computerCardTotal,computerHiddenCard,myCardsTotal):
				for i in range(1,16):
					if computerCardTotal <= 16:
						num01 = random.randint(2,11)

						print("\nComputer choses to hit , Computer draws ",num01)
						computerCardTotal = computerCardTotal + num01
						print("\ncomputer total card:",computerCardTotal)
						if computerCardTotal> 21:
							print("\ncomputer Busts!\n you win \n")
							break

					else:
						
						print("\ncomputer choses to stay so computer's hidden card is",computerHiddenCard,"\n as computer Cards' Total is:",computerCardTotal,"so")


						if computerCardTotal > myCardsTotal :
							print("\ncomputer wins!\n")

						elif computerCardTotal < myCardsTotal:
							print("\nyou win!\n")
						break
# main function  for the generation of random numbers as cards' nummbers 
def main():
	print("\n ******* WELCOME TO BLACKJACK GAME ******* \n ")

	myFirstCard = random.randint(2,11)
	mySecondCard = random.randint(2,11)
	print("\nyou get ",myFirstCard , "and", mySecondCard,"\n")


	myCardsTotal = myFirstCard + mySecondCard

	print("\nyour total is:",myCardsTotal,"\n")
	if myCardsTotal > 21: #initially checking user cards' total
		print("\nyou bust!")
		exit()


	computerFirstCard = random.randint(2,11)
	computerHiddenCard = random.randint(2,11)
	print("\nThe dealer has ",computerFirstCard ,"and a hidden Card too\n")


	computerCardTotal = computerFirstCard + computerHiddenCard

	print("\nhis total is also hidden\n")
	#function call
	game(myFirstCard,mySecondCard,myCardsTotal,computerFirstCard,computerHiddenCard,computerCardTotal)



	
main()









     
