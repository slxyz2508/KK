class Charecter:
    def __init__(self,name) :
        self.name = name
        self.level = 1
        self.exp = 0
        self.max_exp = 0
        self.hp = 0
        self.max_hp = 0
        self.role = 0
        self.attack = 0
        self.potion = 0
        self.money = 0 
        self.item = []
    def __str__(self)  :
        return (
            f'Your Hero Status Is:\n'
            f'Name: {self.name}\n'
            f'Role: {self.role}\n'
            f'Level: {self.level}\n'
            f'Exp: {self.exp}/{self.max_exp}\n'
            f'Hp : {self.hp}/{self.max_hp}\n'
            f'Attck: {self.attack}\n'
            f'Money: {self.money}\n'
            f'Potion: {self.potion}'
            
        )
    
    def roleplay(self,roleplay):
        if self.role != 0:
            print('You cant change your role please make new charecter')
            
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
                print('This role does not exit')
                
    def huntlv1(self,):
        if self.hp <= 0:
            print('You already death Pls make new Charecter')
        damage = 20 / self.attack
        self.hp -= damage
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
    def shop(self):
        if self.role == 'Swordman':
            print(
                'All Item You can Buy:\n'
                'Chestplate : 1000 $\n'
                'Better Sword : 500 $\n'
                'Potion : 300$')
        elif self.role == 'Archer':
            print(
                'All Item You can Buy:\n'
                'Scout Suit : 1000 $\n'
                'New Bow: 500 $\n'
                'Potion : 300$')
    def Buy(self,item):
        if self.role == 'Swordman':
            if item == 'Chestplate':
                if self.money < 1000:
                    print('You Dont have Enough Money')
                else:
                    if item in self.item:
                        print('You already own this item!')
                    else :
                        self.max_hp += 50
                        self.money -= 1000
                        self.item.append(item)
                        print(f"You have successfully purchased {item}!")
            
            elif item == 'Better Sword':
                if self.money < 500:
                    print('You Dont have Enough Money')
                else:
                    if item in self.item:
                        print('You already own this item!')
                    else :
                        self.attack += 10
                        self.money -= 500
                        self.item.append(item)
                        print(f"You have successfully purchased {item}!")
            elif item == 'Potion':
                if self.money < 300 :
                    print('You Dont have Enough Money')
                else :
                    self.potion += 1
                    self.money -= 300
                    print(f"You have successfully purchased {item}!")
            
            else : 
                print("This item is not available for purchase.")
        elif self.role == 'Archer':
            if item == 'Scout Suit':
                if self.money < 1000:
                    print('You Dont have Enough Money')
                else:
                    if item in self.item:
                        print('You already own this item!')
                    else :
                        self.max_hp += 30
                        self.attack += 5
                        self.money -= 1000
                        self.item.append(item)
                        print(f"You have successfully purchased {item}!")
            
            elif item == 'New Bow':
                if self.money < 500:
                    print('You Dont have Enough Money')
                else:
                    if item in self.item:
                        print('You already own this item!')
                    else :
                        self.attack += 13
                        self.money -= 500
                        self.item.append(item)
                        print(f"You have successfully purchased {item}!")
            elif item == 'Potion':
                if self.money < 300 :
                    print('You Dont have Enough Money')
                else :
                    self.potion += 1
                    self.money -= 300
                    print(f"You have successfully purchased {item}!")
            
            else : 
                print("This item is not available for purchase.")
    def UsePotion(self):
        if self.potion == 0:
            print('You Dont Have Potion')
        else:
            self.hp += 20
            if self.hp >= self.max_hp:
                self.hp = self.max_hp
            self.potion -= 1

        
player1 = Charecter('Ton')
player1.roleplay('Swordman')
