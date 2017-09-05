class my_class(object):
    pass



    print ("Hello, and welcome to text_based_game!");
def question_1():
    print ("You are in a dark room, you see a candle. What do you do?");
    print ("A) Pick up the candle");
    print ("B) Blow out the candle");
    print ("C) Eat the candle");

    answer = input("");
    if answer == "A" or "a":
        print ("You pick up the candle.")
        print ("")
        print ("")

    elif answer == "B" or "b":
        print ("You blow out the candle and die from insanity")
        print ("")
        print ("")
        question_1()

    elif answer == "C" or "c":
        print ("You are poisoned by the candle and die.")
        print ("")
        print ("")
        question_1()

question_1()