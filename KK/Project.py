from typing import List, Optional

class Character:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.level: int = 1
        self.exp: int = 0
        self.max_exp: int = 0
        self.hp: int = 0
        self.max_hp: int = 0
        self.role: Optional[str] = None  
        self.attack: int = 0
        self.potion: int = 0
        self.money: int = 0
        self.item: List[str] = []  

    def __str__(self) -> str:
        return (
            f"Your Hero Status Is:\n"
            f"Name: {self.name}\n"
            f"Role: {self.role}\n"
            f"Level: {self.level}\n"
            f"Exp: {self.exp}/{self.max_exp}\n"
            f"Hp : {self.hp}/{self.max_hp}\n"
            f"Attck: {self.attack}\n"
            f"Money: {self.money}\n"
            f"Potion: {self.potion}\n"
            ":------------------:"
        )

    def roleplay(self, roleplay: str) -> None:
        if self.role is not None:
            print("You can't change your role. Please make a new character.\n"
                  ":-------------:")
        elif roleplay == 'Swordman':
            self.max_exp = 100
            self.hp = 20
            self.max_hp = 20
            self.attack = 5
            self.role = 'Swordman'
            print(self)
        elif roleplay == 'Archer':
            self.max_exp = 100
            self.hp = 15
            self.max_hp = 18
            self.attack = 7
            self.role = 'Archer'
            print(self)
        else:
            print("This role does not exist.")

    def huntlv1(self) -> None:
        if self.hp <= 0:
            print("You are already dead. Please make a new character.\n"
                  ":-------------:")
            return
        damage: float = 20 / self.attack
        self.hp -= int(damage)
        self.money += 100
        self.exp += 20

        if self.exp >= self.max_exp:
            self.level += 1
            self.max_exp += 20
            self.exp = 0
            if self.role == 'Swordman':
                self.max_hp += 5
                self.attack += 3
            elif self.role == 'Archer':
                self.max_hp += 3
                self.attack += 4

    def shop(self) -> None:
        if self.role == 'Swordman':
            print(
                "All Items You Can Buy:\n"
                "Chestplate: 1000 $\n"
                "Better Sword: 500 $\n"
                "Potion: 300 $\n"
                ":-------------:"
            )
        elif self.role == 'Archer':
            print(
                "All Items You Can Buy:\n"
                "Scout Suit: 1000 $\n"
                "New Bow: 500 $\n"
                "Potion: 300 $\n"
                ":-------------:"
            )

    def Buy(self, item: str) -> None:
        if self.role == 'Swordman':
            if item == 'Chestplate':
                if self.money < 1000:
                    print("You don't have enough money.\n"
                          ":-------------:")
                elif item in self.item:
                    print("You already own this item!\n"
                          ":-------------:")
                else:
                    self.max_hp += 50
                    self.money -= 1000
                    self.item.append(item)
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            elif item == 'Better Sword':
                if self.money < 500:
                    print("You don't have enough money.\n"
                          ":-------------:")
                elif item in self.item:
                    print("You already own this item!\n"
                          ":-------------:")
                else:
                    self.attack += 10
                    self.money -= 500
                    self.item.append(item)
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            elif item == 'Potion':
                if self.money < 300:
                    print("You don't have enough money.\n"
                          ":-------------:")
                else:
                    self.potion += 1
                    self.money -= 300
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            else:
                print("This item is not available for purchase.\n"
                      ":-------------:")
        elif self.role == 'Archer':
            if item == 'Scout Suit':
                if self.money < 1000:
                    print("You don't have enough money.\n"
                          ":-------------:")
                elif item in self.item:
                    print("You already own this item!\n"
                          ":-------------:")
                else:
                    self.max_hp += 30
                    self.attack += 5
                    self.money -= 1000
                    self.item.append(item)
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            elif item == 'New Bow':
                if self.money < 500:
                    print("You don't have enough money.\n"
                          ":-------------:")
                elif item in self.item:
                    print("You already own this item!\n"
                          ":-------------:")
                else:
                    self.attack += 13
                    self.money -= 500
                    self.item.append(item)
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            elif item == 'Potion':
                if self.money < 300:
                    print("You don't have enough money.\n"
                          ":-------------:")
                else:
                    self.potion += 1
                    self.money -= 300
                    print(f"You have successfully purchased {item}!\n"
                          ":-------------:")
            else:
                print("This item is not available for purchase.\n"
                      ":-------------:")

    def UsePotion(self) -> None:
        if self.potion == 0:
            print("You don't have any potions.\n"
                  ":-------------:")
        else:
            self.hp += 20
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.potion -= 1

def text_based_ui():
    print("Jaywalk RPG")
    name = input("What's your name: ")
    player = Character(name)

    while True:
        print("\nMain Menu:")
        print("1. Choose Role")
        print("2. Go Hunting")
        print("3. Visit Shop")
        print("4. Use Potion")
        print("5. Show Status")
        print("6. Exit Game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Roles: Swordman, Archer")
            role = input("Choose your role: ")
            player.roleplay(role)
        elif choice == "2":
            player.huntlv1()
            print("EXP Gain!:")
            print(player)
        elif choice == "3":
            print("Visiting the shop...")
            player.shop()
            item = input("What do you want to buy: ")
            player.Buy(item)
        elif choice == "4":
            print("Using a potion...")
            player.UsePotion()
            print("Potion used! Your current status is:")
            print(player)
        elif choice == "5":
            print(player)
        elif choice == "6":
            break
        else:
            print("Don't break the matrix!!")


text_based_ui()
