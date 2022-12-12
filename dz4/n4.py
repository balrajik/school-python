class inventory:
    items = []
    current_weight = 0


    def __init__(self,max_weight):
        self.max_weight = max_weight
    

    def add_item(self):
        name = input("Введите имя: ")
        weight = float(input("Введите вес: "))
        if self.current_weight + weight <= self.max_weight:
            self.items.append(item(name,weight))
            self.current_weight +=weight
            self.show_inventory()
        else:
            print("Слишком большой вес")
            self.show_inventory()


    def remove_item(self):
        index = int(input("Введите номер предмета: "))
        if index-1 >= len(self.items):
            print("Предмета с таким номером не существует")
            self.show_inventory()
        else:
            self.items.pop(index-1)
            self.show_inventory()


    def sort_inventory(self):
        choice = input("1 - Сначала лёгкие.\n2 - сначала тяжёлые.\n3 - назад.\n Ввод:") 
        if choice == '1':
            for i in range(len(self.items)-1):
                for j in range (len(self.items)-i-1):
                    if self.items[j].get_weight() > self.items[j+1].get_weight():
                        self.items[j], self.items[j+1] = self.items[j+1], self.items[j]
            self.show_inventory()
        elif choice == '2':
            for i in range(len(self.items)-1):
                for j in range (len(self.items)-i-1):
                    if self.items[j].get_weight() < self.items[j+1].get_weight():
                        self.items[j], self.items[j+1] = self.items[j+1], self.items[j]
            self.show_inventory()
        elif choice == '3':
            self.show_inventory()
        else:
            print("Неверный ввод")


    def show_inventory(self):
        print(f"Вес инвентаря: {self.current_weight}/{self.max_weight}\n____________________________")
        if len(self.items) is 0:
                print("Инвентарь пуст")
        for i in self.items:      
                print(f"{self.items.index(i)+1}. Название: {i.get_name()}, Вес: {i.get_weight()}")
        print("____________________________")
        choice = input("1 - Добавить предмет.\n2 - Удалить предмет.\n3 - сортировка\n4 - Выход\nВвод: ")
        if choice == '1':
            self.add_item()
        elif choice == "2":
            self.remove_item()
        elif choice == "3":
            self.sort_inventory()
        else:
            print("Неверный ввод")
            self.show_inventory()

class item:

    def __init__(self,name,weight) :
        self.name = name
        self.weight = weight
        

    def get_name(self):
        return self.name


    def get_weight(self):
        return self.weight


def main():
    inv = inventory(50.0)
    inv.show_inventory()

if __name__ == "__main__":
    main()