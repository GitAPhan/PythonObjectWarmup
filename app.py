import player as p
import computer as c

# greeting message
print('would you like to play a game?')

player = p.Player(10)
computer = c.Computer(10)

while True:
    try:
        # display health of player and computer
        print("Player's HP:", player.currentHp)
        print("Computer's HP:", computer.currentHp)
        # user attack prompt
        selection = input('Please select 1 for low attack and 2 for high attack: ')

        # player attack sequence
        damage = player.attack(selection)
        print('Player damages computer for', damage, "HP")
        computer.defend(damage)
        if(computer.currentHp < 1):
            print('Congrats you have won the game!')
            exit()

        #computer attack sequence
        damage = computer.attack()
        print('Computer damages Player for', damage, "HP")
        player.defend(damage)
        if(player.currentHp < 1):
            print('Oh no, looks like you lost the game!')
            exit()
    except TypeError:
        print('Please key in only 1 or 2 to represent your choice')