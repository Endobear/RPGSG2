from Creatures.Creature import Creature
from Creatures.Player import Player

player = Player();
creature = Creature(strenght=6,maxHealth = 3, name="AAAAAAAAAAAAA");

batalha = True;

while batalha:
    print("escolha uma opção");
    comando = input();

    if(comando == "atacar"):
        player.Attack(creature)

    if(comando == "observar"):
        print(creature.ShowStats())


    creature.Attack(player);

    if(player.health <= 0):
        print("perdeu")
        batalha = False
    elif(creature.health <= 0):
        print("ganhou")
        batalha = False
        


