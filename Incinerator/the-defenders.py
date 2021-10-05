class Warrior:
    def __init__(self, health=50, attack=5) -> None:
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    def __init__(self, health=50, attack=7) -> None:
        super().__init__(health=health, attack=attack)


class Defender(Knight):
    def __init__(self, health=60, attack=3) -> None:
        super().__init__(health=health, attack=attack)
        self.defense = 2


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Army:
    def __init__(self) -> None:
        self.fighter_list = []

    def add_units(self, fighter, fighter_number):
        for _ in range(fighter_number):
            self.fighter_list.append(fighter())

    def get_next_figher(self):
        if self.fighter_list:
            return self.fighter_list.pop(0)
        return None


class Battle:
    def fight(self, army1, army2):
        unit_1 = army1.get_next_figher()
        unit_2 = army2.get_next_figher()
        while True:
            is_win_unit_1 = fight(unit_1, unit_2)
            if is_win_unit_1:
                unit_2 = army2.get_next_figher()
            else:
                unit_1 = army1.get_next_figher()

            if unit_2 is None:
                return True
            elif unit_1 is None:
                return False


def fight(unit_1, unit_2):
    while True:
        # 1人目の攻撃
        if isinstance(unit_2, Defender):
            unit_2.health -= (unit_1.attack -
                              unit_2.defense) if unit_1.attack > unit_2.defense else 0
        else:
            unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            return True
        # 2人目の攻撃
        if isinstance(unit_1, Defender):
            unit_1.health -= (unit_2.attack -
                              unit_1.defense) if unit_2.attack > unit_1.defense else 0
        else:
            unit_1.health -= unit_2.attack
        if not unit_1.is_alive:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
