print("Welcome to Quiz game Time!!")


play = input("Do you want to play ?  (yes/no ) : ")
score = 0
Totalquestions = 8
try:
    if play.lower() == "yes":
        print("Lets Begin!!")
    
        ans = input(" 1 .  what is the name of the largest continent in the world ? : ")
        while ans == "":
            print (input(" 1 .  what is the name of the largest continent in the world ? : "))
        if ans.capitalize() == "Asia":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")

        ans = input(" 2 . what is the name of the founder of Tesla ? : ")
        while ans == "":
            print (input(" 2 . what is the name of the founder of Tesla ? : "))
        if ans.capitalize()== "Elon Musk":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")
        
        ans = input(" 4 . The year Nigeria gained independence is  ? : ")
        while ans == "":
            print (input(" 4 . The year Nigeria gained independence is  ? : "))
        if ans.lower()== "1960":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")
        
        ans = input(" 5 . what is the name of America's president is ? : ")
        while ans == "":
            print (input(" 5 . what is the name of America's president is ? : "))
        if ans.capitalize()== "JoeBiden":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")

        ans= input(" 6. How Many Wonders of the world are there ? : ")
        while ans == "":
            print (input(" 6. How Many Wonders of the world are there ? : "))
        if ans == "7":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")

        ans = input(" 7. what is the name of the coldest continent in the world ? : ")
        while ans == "":
            print (input(" 7. what is the name of the coldest continent in the world ? : "))
        if ans.capitalize()== "Antartica":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")
        
        ans = input(" 8 .what is the name of China's currency ? : ")
        while ans == "":
            print (input(" 8 .what is the name of China's currency ? : "))
        if ans.capitalize()== "Yen":
            score += 1
            print("Correct!!")
        else:
            print("Incorrect!")

        print("Thank you for playing you got ", score , "Questions correctly")
        mark = (score/Totalquestions)*100/1
        print("your Total mark is ", mark)
        if mark >= 50:
            print("you passed!!   Weldone")
        elif mark <= 0:
            print("you failed!")
        
    else:
        print("Bye")
except:
    print("There is an Error")
