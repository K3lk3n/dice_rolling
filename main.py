import random
class Player:
    dice_numbers = [1, 2, 3, 4, 5, 6]
    def __init__ (self, name):
        self.name = name 
        self.score = 0 
    @staticmethod

    def roll():
        x = random.choice(Player.dice_numbers)
        return x 

    def play_again(self):
        choice  = input('Play again: ').upper()
        if choice  == "Y":
            self.play_against_computer()
        elif choice  == "N":
            print('logging off.......')
        else:
            self.play_again()    

    def play_against_computer(self):

        self.score = Player.roll()
        print(F'You rolled a {self.score}.')
        comp_score = random.choice(Player.dice_numbers)
        if self.score > comp_score:
            print(f'YOU WIN!!')
        elif self.score < comp_score:
            print(f'Computer WINS!!')
        else:
            print(f'TIE!!')
        print(f'Computer rolled a {comp_score}')
        print('----------------------------------')
        self.play_again()

    def mode(self):

        rounds = input('Enter amount of rounds:')
        rounds = int(rounds)
        rounds_won = 0 
        rounds_lost = 0 
        rounds_tied = 0 

        for i in range(1, rounds + 1):
            
            print('') 
            print(f'Round {i}') 
            self.score = Player.roll()
            print(F'You rolled a {self.score}.')
            comp_score = random.choice(Player.dice_numbers)
            if self.score > comp_score:
                rounds_won = rounds_won + 1
                print(f'YOU WIN!!, Computer rolled a {comp_score}')
                print(f'Round {i} goes to You')
            elif self.score < comp_score:
                rounds_lost = rounds_lost + 1
                print(f'Computer WINS!!, Computer rolled a {comp_score}')
                print(f'Round {i} goes to computer.')
            else:
                rounds_tied = rounds_tied + 1 
                print(f'TIE!!, Computer rolled a {comp_score} as well.')
            print(f'Score:{rounds_won}-{rounds_tied}-{rounds_lost}')
            print('----------------------------------')
        grand_finale_Score = [rounds_won, rounds_lost]
        if grand_finale_Score[0] > grand_finale_Score[1]:
            print(f'Grand Finale Score: {rounds_won}-{rounds_tied}-{rounds_lost}')
            print(f'YOU WIN!!!!')
        elif grand_finale_Score[0] == grand_finale_Score[1]:
            print(f'Grand Finale Score: {rounds_won}-{rounds_tied}-{rounds_lost}')
            print('Its a TIEBREAKER')
        else:
            print(f'Grand Finale Score:{rounds_won}-{rounds_tied}-{rounds_lost}')
            print('YOU LOST!!!')
        

p1 = Player('Raj')
p1.mode()