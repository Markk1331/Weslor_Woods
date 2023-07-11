dic = {'alex': 5, "bob":-2, "Charles":100}

def named(*arges,**kwargs):
    print(kwargs)
    print(arges)

#named('people','alex', name=5,people="very gamer")

def addon(**kwargs):
    for k,v in kwargs.items():
        print(f'\tthe fruits: {k} has {v} amount in the store')

#addon(banana=5, apple=10, orange=2,grape=10)

def scores(v,*arges,store):
    for i in arges:
        i += 2
    print(f'{v} is the test, the scores are {arges} that take place in {store}')
#scores('english',100,300,200,500,50, store = "Pekka_city")


def people(race,age,origin):
    print (f'the race is {race}, the prospect is {age}, who comes from {origin}')

suspect = [('black',24,'Africa')]
suspect_1 = {"race":'white','age':31,"origin":"South Africa"}

#people(race=suspect[0][0],age=suspect[0][1],origin=suspect[0][2])
#people(**suspect_1)



def criminal(*awrgs, **kwargs):
    s = "'"
    for i in awrgs:
        if i[2] =="M":
            gender = "his"
        else:
            gender = "her"
        print(f'the people are {i[0]}, and {gender} age is {i[1]}')
        
    for k,v in kwargs.items():
        print(f'the bad person{s}s name is {k}, and the age is {v}')

bad_guys = [("John",35,"M"),("Sam",25,"M"),("Marry",71,"F")]
bad_people = {"John":35,"Sam":26,"Marry":71}

criminal(*bad_guys)
#criminal(**bad_people)




