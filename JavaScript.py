My_Details={
    "name":"ranjith",
    "age":21,
    "address":"L/57 phase-4 sathuvachari",
    "phone_no":8056868646
    }
print(My_Details)

my_name=[
    {
        "name":"roy","address":"unknown","phone_no":8056868646,
        "name":"kumar","address":"h43","pn_no":453947889
    }
]
print(my_name)

My_Details.values()
try:
    print(values)
except:
    print("hello ur result is wrong")


def my_function(x): #using functions
 return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

#another example
ranjith=[]

def get_ranjith_kumar():
    ranjith_kumar=[]    
    for address in ranjith:
        ranjith_kumar=ranjith.title()
        return ranjith_kumar

    def print_ranjith_kumar():
        ranjith_kumar = []
        for address in ranjith:
            ranjith_kumar = ranjith.title()
            return ranjith_kumar

        def add_ranjith_kumar(phoneno):
            ranjith_kumar.append(phoneno)
            ranjith_kumar=get_ranjith_kumar()
            add_ranjith_kumar(8056868646)
