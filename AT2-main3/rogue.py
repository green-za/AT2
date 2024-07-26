from character import Character

class Rogue(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Rogue", armour = 7)
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.dexterity = 15
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attacks = {
            "Basic Attack": {"method": self.attack, "stamina_cost": 10},
            "Backstab": {"method": self.backstab, "stamina_cost": 20},
            "Quick Strike": {"method": self.quick_strike, "stamina_cost": 30},
            "Multi Attack": {"method": self.multi_attack, "stamina_cost": 15},
            "Evade": {"method": self.evade, "stamina_cost": 5},
        }


def attack(self, target):
        damage = self.dexterity * self.level
        target.take_damage(damage)
        return damage

def backstab(self, target):
        print(f"{self.name} performs a backstab on {target.name}!")
        damage = self.dexterity * 3
        target.take_damage(damage)
        return damage

def quick_strike(self, target):
        print(f"{self.name} performs a quick strike on {target.name}!")
        damage = self.dexterity * 1.5
        target.take_damage(damage)
        return damage

def multi_attack(self, targets):
        total_damage = 0
        for target in targets:
            damage = self.dexterity * 2
            total_damage += damage
            print(f"{self.name} performs a multi-attack on {target.name} for {damage} damage!")
            target.take_damage(damage)
        print(f"{self.name} dealt a total of {total_damage} damage with multi-attack!")
        return total_damage

def evade(self):
        self.armor_class += 5
        print(f"{self.name} uses Evade, increasing armor class by 5!")
        return self.armor_class
