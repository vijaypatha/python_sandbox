keep_looping = True
while keep_looping = True:
    user_input = input("Enter a city or q")
    if user_input !="q":
        for city in clean_city:
            if user_input = city:
                print("Good choice")
                break
    else:
        keep_looping = False