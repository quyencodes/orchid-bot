# initialize JSON blob
maplestory_classes = {}

# initialize class to create JSON blob properties
class Archetype:
  def __init__(self, warriors, magicians, archers, thieves, pirates):
    self.classes = set(['warrior', 'magician', 'archer', 'thief', 'pirate'])
    self.warriors = warriors or []
    self.magicians = magicians or []
    self.archers = archers or []
    self.thieves = thieves or []
    self.pirates = pirates or []

  def __str__(self):
    if self.warriors:
      print('The warrior(s) in this archetype are:', ','.join(self.warriors))

    if self.magicians:
      print('The magician(s) in this archetype are:', ','.join(self.magician))

    if self.archers:
      print('The archer(s) in this archetype are:', ','.join(self.archer))

    if self.thieves:
      print('The thief(s) in this archetype are:', ','.join(self.thief))

    if self.pirates:
      print('The pirate(s) in this archetype are:', ','.join(self.pirate))

  def get_archetype(self, choice):
    if choice not in self.classes:
      return f"You inputted {str(choice)}. Please select a valid class."

    return self.choice

explorer_warriors = ['hero', 'paladin', 'dark knight']
explorer_magicians = ['bishop', 'ice / lightning mage', 'fire / poison mage']
explorer_archers = ['bowmaster', 'marksman', 'pathfinder']
explorer_thieves = ['night lord', 'shadower', 'dual blade']
explorer_pirates = ['buccaneer', 'cannoneer', 'corsair']



explorers = Archetype(explorer_warriors, explorer_magicians, explorer_archers, explorer_thieves, explorer_thieves)