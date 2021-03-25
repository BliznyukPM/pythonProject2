class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualification = q

    def info(self):
        print('имя -', self.name, 'фамилия -', self.surname, 'квалификация', self.qualification)

    def __del__(self):
        print('Досвидание мистер', self.name, ' ', self.surname)


a = Person('Сергей', 'Близнюк', 5)
b = Person('Павел', 'Близнюк', 4)
c = Person('Александра', 'Близнюк')
a.info()
b.info()
c.info()

spis_object=[a,b,c,b,c,c] #список объектов
spis_etalon=spis_object[0].qualification #эталон для сравнения
spis_weak_link=[] #список слабого звена
for i in spis_object:
    #определение и заполнение списка слабого звена
    if i.qualification < spis_etalon:
        spis_weak_link.clear()
        spis_etalon=i.qualification
        spis_weak_link.append(i)
    elif i.qualification == spis_etalon:
        spis_weak_link.append(i)
    continue
def del_weak_link():
    for k in spis_weak_link:
        k.__del__()
del_weak_link()

input()