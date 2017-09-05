class my_class(object):
    pass

    print ("Hello, and welcome to text_based_game!");
    
def question_1():
    print ("You are in a dark room, you see a candle. What do you do?");
    print ("A) Pick up the candle");
    print ("B) Blow out the candle");
    print ("C) Eat the candle");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("	You pick up the candle and walk forward. You hit a wall. It is the wall part of a hall. Which way do you go?")
        print ("")
        print ("")
        question_2()

    elif answer == "B" or answer == "b":
        print ("You blow out the candle and die from insanity")
        print ("")
        print ("")
        question_1()

    elif answer == "C" or answer == "c":
        print ("You are poisoned by the candle and die.")
        print ("")
        print ("")
        question_1()

def question_2():
    print ("A) Right.");
    print ("B) Left.");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("	You walk to the right and are greeted with a door with a rusty lock. What do you do?")
        print ("")
        print ("")

    elif answer == "B" or answer == "b":
        print ("You walk to the left and fall into a hole full of rusty spikes and die instantly.")
        print ("")
        print ("")
        question_1()


question_1()
