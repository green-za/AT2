from character import Character

class Mage(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Mage", armor = 5)
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.intelligence = 15
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attacks = {
            "Basic Attack": {"method": self.attack, "stamina_cost": 10},
            "Fireball": {"method": self.fireball, "stamina_cost": 20},
            "Arcane Blast": {"method": self.arcane_blast, "stamina_cost": 30},
            "Frost Nova": {"method": self.frost_nova, "stamina_cost": 15},
            "Magic Shield": {"method": self.magic_shield, "stamina_cost": 5},
        }

    def choose_attack(self, target):
        print(f"Choose an attack (Current stamina: {self.current_stamina}):")
        attack_list = list(self.attacks.items())
        for i, (attack, info) in enumerate(attack_list):
            print(f"{i + 1}. {attack} (Stamina cost: {info['stamina_cost']})")
        chosen_attack = int(input("Enter the number of the attack: "))
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
            else:
                print("Not enough stamina for this attack.")
        else:
            print("Invalid attack.")

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)


def attack(self, target):
        damage = self.intelligence * self.level * 1.5
        target.take_damage(damage)
        return damage

def fireball(self, target):
        print(f"{self.name} casts Fireball at {target.name}!")
        damage = self.intelligence * 2
        target.take_damage(damage)
        return damage

def arcane_blast(self, target):
        print(f"{self.name} casts Arcane Blast at {target.name}!")
        damage = self.intelligence * 1.2
        target.take_damage(damage)
        return damage

def frost_nova(self, targets):
        total_damage = 0
        for target in targets:
            damage = self.intelligence * 1.5
            total_damage += damage
            print(f"{self.name} casts Frost Nova on {target.name} for {damage} damage!")
            target.take_damage(damage)
        print(f"{self.name} dealt a total of {total_damage} damage with Frost Nova!")
        return total_damage

def magic_shield(self):
        self.armor_class += 10
        print(f"{self.name} casts Magic Shield, increasing armor class by 10!")
        return self.armor_class