x = input("hey! this is the chatbot for the MLC, please enter which part of the club you are from?")
if  x.lower() == "technical team":
    y = input("hey! have you completed your assignment for the friday?")
    if y.lower() == "yes":
        print("goojob, make sure to join the meet at friday! ")
    elif y.lower() == "no":
        print("goodluck with rahul ")
    else:
        print("its a yes or no question retard")
else:
    print("please contact the other chatbot, this bot is built for Technical team members only! <3")