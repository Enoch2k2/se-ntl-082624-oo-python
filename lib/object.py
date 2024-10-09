
class Actor():
  def __init__(self, name):
    self.name = name
    type(self).all.append(self)

  def attack(self, target):
      print(f'{self.name} attacks {target.name}')

  @classmethod
  def print_names(cls):
    for obj in cls.all:
      print(obj.name)

class Player(Actor):

  all = []

  def __init__(self, name, experience):
    super().__init__(name)
    self.experience = experience
    self.items = []

  @property
  def experience(self):
    return self._experience

  @experience.setter
  def experience(self, experience):
    if (experience < 0):
      raise ValueError("Oops... Experience can't be less than 0")
    self._experience = experience

  def wave_emote(self, target):
    print(f'{self.name} waves to {target.name}')

  def attack(self, target):
    super().attack(target)
    print("this would be the difference")

  

  def addItem(self, item):
    self.items.append(item)

  def print_items(self):
    for item in self.items:
      print(item.name)

  
  def __repr__(self):
    return f'<Player name={self.name} experience={self.experience}>'
  
class Enemy(Actor):

  all = []

  def __repr__(self):
    return f'<Enemy name={self.name}>'
  

class Item():
  def __init__(self, name):
    self.name = name

try:
  player_1 = Player(experience=50, name="Bob")
  player_2 = Player(name="Sam", experience=0)
  enemy_1 = Enemy(name="Darth Bob")
  enemy_2 = Enemy(name="Karen")
  weapon = Item("Sword of a thousand truths")
  # player_1.wave_emote(player_2)
  # player_1.addItem(weapon)
  # player_1.print_items()
  player_1.attack(enemy_1)
  enemy_1.attack(player_1)

  # Player.print_names()
except ValueError as error:
  print(f"Error: {str(error)}")