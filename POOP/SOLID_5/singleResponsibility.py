# After: Focused classes with single responsibilities

class SuperHero:
    def __init__(self, name):
        self.name = name
    
    def save_civilian(self):
        print(f"{self.name} is saving a civilian!")
    
    def fight_villain(self):
        print(f"{self.name} is fighting a villain!")

class MissionReporter:
    def __init__(self, hero):
        self.hero = hero
    
    def write_report(self):
        print(f"{self.hero.name} is writing a mission report.")

class CostumeManager:
    def __init__(self, hero):
        self.hero = hero
    
    def repair_costume(self):
        print(f"{self.hero.name} is repairing their costume.")

# Usage
batman = SuperHero("Batman")
reporter = MissionReporter(batman)
costume_manager = CostumeManager(batman)

batman.save_civilian()
batman.fight_villain()
reporter.write_report()
costume_manager.repair_costume()