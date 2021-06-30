

def score(nice,mean,name):
    # score function is bieng passed the values stored within the 3 variables
    if nice > 2: # if condition is vaild, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them.
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name) :
    # Substitute  the () wildcards with our variable values
    print("\nNice job (), you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)




def again(nice,mean,name) :
    stop = True
    while stop:
        choice = input("nDo you want to play again? (y/n) :
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")                                                             nb 


def reset(nice,mean,name            



if __name__ == "__main__":
    start()

    






    
