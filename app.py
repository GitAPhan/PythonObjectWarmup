import random
import player as p
import computer as c
import inputexception as ie
import dbi


# greeting message
print('would you like to play a game?')
print('------------------------------')
dbi.DbInteraction.display_scoreboard()
print('------------------------------')



player = p.Player(10)
computer = c.Computer(random.randint(7, 14))

while True:
    try:
        # display health of player and computer
        print("Player's HP:", player.currentHp)
        print("Computer's HP:", computer.currentHp)
        # user attack prompt
        selection = input(
            'Please select 1 for low attack and 2 for high attack: ')

        # player attack sequence
        damage = player.attack(selection)
        print('Player damages computer for', damage, "HP")
        computer.defend(damage)
        if(computer.currentHp < 1):
            print('Congrats you have won the game!')
            dbi.DbInteraction.add_win_loss_to_db(1)
            exit()

        # computer attack sequence
        damage = computer.attack()
        print('Computer damages Player for', damage, "HP")
        player.defend(damage)
        if(player.currentHp < 1):
            print('Oh no, looks like you lost the game!')
            dbi.DbInteraction.add_win_loss_to_db(0)
            exit()

        print('------------------------------')
    except TypeError:
        print('Please key in only 1 or 2 to represent your choice')
