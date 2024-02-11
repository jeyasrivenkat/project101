import random
response=input("do you want to roll dice?")

while response=="y":
    no=random.randint(1,6)
    print(no)
    if no == 1:
        print("[-----]") 
        print("[     ]")   
        print("[  1  ]")
        print("[     ]")
        print("[-----]") 
    if no == 2:
        print("[-----]") 
        print("[     ]")   
        print("[  2  ]")
        print("[     ]")
        print("[-----]") 
    if no == 3:
        print("[-----]") 
        print("[     ]")   
        print("[  3  ]")
        print("[     ]")
        print("[-----]") 
    if no == 4:
        print("[-----]") 
        print("[     ]")   
        print("[  4  ]")
        print("[     ]")
        print("[-----]") 
    if no == 5:
        print("[-----]") 
        print("[     ]")   
        print("[  5  ]")
        print("[     ]")
        print("[-----]") 
    if no == 6:
        print("[-----]") 
        print("[     ]")   
        print("[  6  ]")
        print("[     ]")
        print("[-----]") 
    response=input('enter y if you want to continue or n if you dont ')