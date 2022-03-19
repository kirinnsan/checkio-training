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


class Vampire(Warrior):
    def __init__(self, health=40, attack=4) -> None:
        super().__init__(health=health, attack=attack)
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self, health=50, attack=6) -> None:
        super().__init__(health=health, attack=attack)
        self.penetration_attack_rate = 0.5


class Army:
    def __init__(self) -> None:
        self.fighter_list = []

    def add_units(self, fighter, fighter_number):
        for _ in range(fighter_number):
            self.fighter_list.append(fighter())

    def pop_next_unit(self):
        if self.fighter_list:
            return self.fighter_list.pop(0)
        return None

    def get_next_unit(self):
        if self.fighter_list:
            return self.fighter_list[0]
        return None

    def update_next_unit_parameter(self, next_unit):
        self.fighter_list[0] = next_unit


class Battle:
    def fight(self, army1, army2):
        unit_1 = army1.pop_next_unit()
        unit_2 = army2.pop_next_unit()
        while True:
            is_win_unit_1 = fight(unit_1, unit_2, army1, army2)
            if is_win_unit_1:
                unit_2 = army2.pop_next_unit()
            else:
                unit_1 = army1.pop_next_unit()

            if unit_2 is None:
                return True
            elif unit_1 is None:
                return False


def fight(unit_1, unit_2, army1=None, army2=None):
    while True:
        # 1人目の攻撃
        damage = 0
        if isinstance(unit_2, Defender):
            damage = (unit_1.attack -
                      unit_2.defense) if unit_1.attack > unit_2.defense else 0
            unit_2.health -= damage
        else:
            damage = unit_1.attack
            unit_2.health -= damage
        if isinstance(unit_1, Vampire):
            unit_1.health += damage * unit_1.vampirism
        # ランサーの場合
        elif isinstance(unit_1, Lancer):
            if army2:
                next_unit_2 = army2.get_next_unit()
                # 2体目の敵がディフェンダーの場合
                if isinstance(next_unit_2, Defender):
                    damage = damage * unit_1.penetration_attack_rate
                    damage = (damage - next_unit_2.defense) if \
                        damage > next_unit_2.defense else 0
                    next_unit_2.health -= damage
                elif isinstance(next_unit_2, Warrior):
                    next_unit_2.health -= damage * unit_1.penetration_attack_rate
                # 2体目の敵のパラメータ更新
                if next_unit_2:
                    army2.update_next_unit_parameter(next_unit_2)
        if not unit_2.is_alive:
            return True

        damage = 0
        # 2人目の攻撃
        if isinstance(unit_1, Defender):
            damage = (unit_2.attack -
                      unit_1.defense) if unit_2.attack > unit_1.defense else 0
            unit_1.health -= damage
        else:
            damage = unit_2.attack
            unit_1.health -= damage
        if isinstance(unit_2, Vampire):
            unit_2.health += damage * unit_2.vampirism
        # ランサーの場合
        elif isinstance(unit_2, Lancer):
            if army1:
                next_unit_1 = army1.get_next_unit()
                # 2体目の敵がディフェンダーの場合
                if isinstance(next_unit_1, Defender):
                    damage = damage * unit_2.penetration_attack_rate
                    damage = (damage - next_unit_1.defense) if \
                        damage > next_unit_1.defense else 0
                    next_unit_1.health -= damage
                elif isinstance(next_unit_1, Warrior):
                    next_unit_1.health -= damage * unit_2.penetration_attack_rate
                # 2体目の敵のパラメータ更新
                if next_unit_1:
                    army1.update_next_unit_parameter(next_unit_1)
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
