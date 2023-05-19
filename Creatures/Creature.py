from Items.Item import Item;



# Creature of steel
class Creature():
    def __init__(self,name = "", health = 0, maxHealth = 0,strenght = 0, dexterity = 0, perception = 0, intelligence = 0, toughness = 0):
        self.name = name
        self.maxHealth = maxHealth;
        self.health = int(health if health > 0 else self.maxHealth);
        self.strenght = strenght;
        self.dexterity = dexterity;
        self.perception = perception;
        self.intelligence = intelligence;
        self.toughness = toughness;

        self.inventory = Item();

        self.tempDefence = 0;
        self.tempAttack = 0;

   
    def __str__(self) -> str:
        return f"Name: {self.name}\nLife: {self.health}"

    def Attack(self, creature):
        damage = self.strenght - creature.toughness;
        if (damage < 0):
            damage = 0; 
        creature.health -= damage;
        print(f"{self.name} atacou {creature.name} causando {damage} de dano")

    def AddHealth(self,health):
        if(self.health + health >= self.maxHealth): 
            self.health = self.maxHealth;
        else:
            self.health += health;

    def ShowStats(self):
        return f"Name: {self.name}\nLife: {self.health}"
    


