class Person:
    _id_counter = 1  

    def __init__(self, first_name, last_name):
        self.first_name = first_name  
        self.last_name = last_name   
        self._id = Person._id_counter
        Person._id_counter += 1

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if len(value) > 20:
            raise ValueError("نام بیش از حد طولانی است (حداکثر ۲۰ کاراکتر).")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 20:
            raise ValueError("نام خانوادگی بیش از حد طولانی است (حداکثر ۲۰ کاراکتر).")
        self._last_name = value

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"Person(ID={self.id}, First='{self.first_name}', Last='{self.last_name}')"
    
p1 = Person('amin','bajelan') 
p2 = Person('erfan','rovez')   
print(p1.id)
print(p2.id)