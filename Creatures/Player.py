from Creatures.Creature import Creature


class Player(Creature):
    def __init__(self):
        super().__init__(strenght=1,dexterity=1,name="PLAYER",maxHealth="10",intelligence=1,perception=1,toughness=2)
        self.level = 1;
        self.xp = 0;
        self.nextLevel = 15;

    def Attack(self, creature):
        damage = self.strenght - creature.toughness;
        if (damage < 0):
            damage = 0; 
        creature.health -= damage;
        print(f"Você atacou {creature.name} causando {damage} de dano")