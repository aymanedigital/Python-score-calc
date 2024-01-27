while True:
    print("Welcome to our app , calculate your score! :")
    x = input("click 'enter' to start or type 'exit' to exit : ")
    if x.lower() == "exit":
        break

    math = input("Math : ")
    french = input("French : ")
    arab = input("Arab : ")
    physics = input("Physics : ")
    svt = input("SVT : ")
    histoire_geo = input("Histoire geo : ")
    Edu_Islamique = input("Education islamique : ")
    sport = input("Sport : ")
    english = input("English : ")
    informatique = input("Informatique : ")
    total = float(math)+float(french)+float(arab)+float(physics)+float(svt)+float(histoire_geo)+float(Edu_Islamique)+float(sport)+float(sport)+float(english)+float(informatique)
    score = total/11
    print("Your Score is : "+str(score))