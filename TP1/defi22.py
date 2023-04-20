def guess_number():
    min_num = 1
    max_num = 100
    num_guesses = 0
    
    while True:
        guess = (min_num + max_num) // 2
        num_guesses += 1
        response = input(f"Est-ce que ton nombre est égal à {guess}? (oui/non) ")
        if response.lower() == "oui":
            print(f"J'ai trouvé le nombre en {num_guesses} essais!")
            break
        elif response.lower() == "non":
            response = input("Est-ce que ton nombre est plus petit ou plus grand? ")
            if response.lower() == "plus petit":
                max_num = guess - 1
            elif response.lower() == "plus grand":
                min_num = guess + 1
            else:
                print("Je n'ai pas compris ta réponse. Veuillez répondre 'plus petit' ou 'plus grand'.")
        else:
            print("Je n'ai pas compris ta réponse. Veuillez répondre 'oui' ou 'non'.")
guess_number()
