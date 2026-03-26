class GameCharacter:
  def __init__(self, health, mana):
    self.health = health
    self.mana = mana

  def attack(self):
    print("Attacking with basic attack!")

  def heal(self):
    print("Healing with basic heal!")

c1 = GameCharacter(100, 50)
c2 = GameCharacter(80, 30)
print(f"Character 1 - Health: {c1.health}, Mana: {c1.mana}")
print(f"Character 2 - Health: {c2.health}, Mana: {c2.mana}") 
c1.attack()
c1.heal()
c2.attack()
c2.heal()
  