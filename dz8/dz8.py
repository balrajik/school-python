class Animals():
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height
    
    def walk():
        print("walking")

class Mammals(Animals):
    def __init__(self, age, weight,height, presence_of_wool):
        super().__init__(age,weight,height)
        self.presence_of_wool = presence_of_wool

    def drink_milk():
        print("drinking")

class Human(Mammals):
    def __init__(self, age, weight, height, presence_of_wool,iq,name):
        super().__init__(age, weight, height, presence_of_wool)
        self.iq = iq
        self.name = name

    def think():
        print("thinking")

class Cat(Mammals):
    def __init__(self, age, weight, height, presence_of_wool,breed,whisker_length):
        super().__init__(age, weight, height, presence_of_wool)
        self.breed = breed
        self.whisker_length = whisker_length
    def meow():
        print("meow")

class Dog (Mammals):
    def __init__(self, age, weight, height, presence_of_wool,breed):
        super().__init__(age, weight, height, presence_of_wool)
        self.breed = breed
    def bark():
        print("bark")


class Student(Human):
    def __init__(self, age, weight, height, presence_of_wool, iq, name, amount_of_completed_homeworks):
        super().__init__(age, weight, height, presence_of_wool, iq, name)
        self.amount_of_completed_homeworks = amount_of_completed_homeworks
        self.can_say = True

    def __eq__(self, __o: object) -> bool:
        return  self.amount_of_completed_homeworks.__eq__(__o.amount_of_completed_homeworks)

    def __ne__(self, __o: object) -> bool:
        return self.amount_of_completed_homeworks.__ne__(__o.amount_of_completed_homeworks)
    
    def __lt__(self, __o: object) -> bool:
        return  self.amount_of_completed_homeworks.__lt__(__o.amount_of_completed_homeworks)

    def __gt__(self, __o: object) -> bool:
        return  self.amount_of_completed_homeworks.__gt__(__o.amount_of_completed_homeworks)

    def __le__(self, __o: object) -> bool:
        return  self.amount_of_completed_homeworks.__le__(__o.amount_of_completed_homeworks)

    def __ge__(self, __o: object) -> bool:
        return  self.amount_of_completed_homeworks.__ge__(__o.amount_of_completed_homeworks)

    def logging(function):
        def wrapper(self,text):
                function(self,text)
                with open('log.txt','a') as file:
                    import datetime
                    file.write(f"{datetime.datetime.now()} | {self.name}: {text}\n")
        return wrapper

    def execution_time(function):
        def wrapper(self,text):
            import time
            start_time = time.time()
            function(self,text)
            print(f"Времы выполнения - {time.time() - start_time}")
        return wrapper

    def slower(function):
        def wrapper(self,text):
            import time
            time.sleep(1)
            function(self,text)
        return wrapper
    
    def change_status(self):
        self.can_say = True

    def time_required(function):
        def wrapper(self,text):
            if self.can_say == True:
                function(self,text)
                self.can_say = False
                from threading import Timer
                tm = Timer(interval=4.0,function= self.change_status)
                tm.start()
            else:
                print("Подождите прежде чем говорить снова")
        return wrapper

    @execution_time
    @logging
    @slower
    @time_required
    def say(self, text):
        print(f'{text}')





    
Dmitry = Student(18,56,150,'no',200,'Dmitry',7)
Alex = Student(18,56,150,'no',200,'Alex',9)
print(Dmitry <= Alex)
#from time import sleep
#while True:
#    Alex.say("hello")
#    sleep(1)