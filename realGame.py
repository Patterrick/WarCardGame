class my_class(object):
    pass

    print ("Hello, and welcome to text_based_game!");
    
def question_1():
    print ("    You are in a dark room, you see a candle. What do you do?");
    print ("A) Pick up the candle.");
    print ("B) Blow out the candle.");
    print ("C) Eat the candle.");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("	You pick up the candle and walk forward. You hit a wall. It is the wall part of a hall. Which way do you go?")
        print ("")
        print ("")
        question_2()

    elif answer == "B" or answer == "b":
        print ("    You blow out the candle and die from insanity.")
        print ("")
        print ("")
        question_1()

    elif answer == "C" or answer == "c":
        print ("    You are poisoned by the candle and die.")
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
        question_3()

    elif answer == "B" or answer == "b":
        print ("    You walk to the left and fall into a hole full of rusty spikes and die instantly.")
        print ("")
        print ("")
        question_1()

def question_3():
    print ("A) Try to smash the lock.");
    print ("B) Try to open the door.");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("    You smash the lock and a sharp part impales your foot through your shoe and you die of tetanus.")
        print ("")
        print ("")
        question_1()

    elif answer == "B" or answer == "b":
        print ("The door opens easily with a small squeek. You walk through and you end up in a small room. There is a mouse on the ground in the middle of the room. What do you do?")
        print ("")
        print ("")
        question_4()

def question_4():
    print ("A) Kill the mouse.");
    print ("B) Touch the mouse.");
    print ("C) Place the candle in front of the mouse.");
    print ("D) Take a nap.");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("	You kill the mouse and suddenly more mice crawl through the cracks of the stone walls and eat you alive.")
        print ("")
        print ("")
        question_2()

    elif answer == "B" or answer == "b":
        print ("    You touch the mouse and die from disease.")
        print ("")
        print ("")
        question_1()

    elif answer == "C" or answer == "c":
        print ("    You place the candle in front of the mouse and it eats the candle. You die from insanity.")
        print ("")
        print ("")
        question_1()

    elif answer == "D" or answer == "d":
        print ("    You take a nap. You wake up a short while later and notice that the mouse is gone. In its place is a man facing away from you. What do you do?")
        print ("")
        print ("")
        question_5()

def question_5():
    print ("A) Kill the man.");
    print ("B) Talk to the man.");

    answer = input("");
    if answer == "A" or answer == "a":
        print ("    You killed the man. The walls collapse. You are in a wheat field. You have won text_based_game.")
        print ("")
        print ("")


    elif answer == "B" or answer == "b":
        print ("    You attempt to talk to the man, he turns around and his face is covered in blood. He lunges at you and kills you.")
        print ("")
        print ("")
        question_1()


question_1()
