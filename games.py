import random
class Player(object):
    """A player for a game"""
    def __init(self,name):
        self.name = name
        self.hand = cards.Hand()
    def __str__(self):
        rep = self.name
        rep = rep +" "+str(self.hand.cards[0])
        return rep

def ask_num(question, low, high):
    while True:
        num = input("enter how many people are playing: (1-4)")
        try:
            num = int(input(question))
            if num in range(low, high):
                return num
            else:
                print("that is out of range")
        except:
            print("that was not a number")
def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y","n"):
          response = input(question).lower()
    return response
def switch_turn(num_players, turn):
    turn = turn
    if turn < num_players:
        turn += 1
    else:
        turn = 0
    return turn
def roll(self):
    die1 = random.randrange(1,6)
    die2 = random.randrange(1,6)
    roll = die1 + die2
    print("you rolled a",die1,"and a",die2 )
    return roll
def winner_grats():
    print("Congrats, you won")


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit")