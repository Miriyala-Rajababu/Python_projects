import random
def Random_Guesing_game():
    user=0
    computer=0
    print("Wel come to game😍")
    while True:
        userguess=int(input('Guess the number 0 to 9'))
        if userguess<10:
            if userguess==random.randint(0,10):
                print("Super guess again😍😍😍")
                user+=1
            else:
                print("wrong Guess again'😪")
                computer+=1
        else:
            break
        
    return f'Thank You 😍 Game is Over =======User score:{user} Computer score: {computer}'



print(Random_Guesing_game())