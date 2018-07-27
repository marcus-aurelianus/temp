class People:
    all_people={}
    def __init__(self, uid, age):
        self.uid = uid
        self.age = age
        People.all_people[uid]=age

    @classmethod 
    def get_nonage(self):
        return {uid:age for (uid,age) in People.all_people.items() if age<18}
    
p1 = People(1, 11)
p2 = People(2, 20)
p3 = People(3, 15)

print(People.get_nonage())
