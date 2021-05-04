#This code adds the draw4 challenge functionality.

import random
from os import system

previous_card=""
deck=[]   
wild_draw4_flag=False
wild_flag=False
list_players=[]
reverse_flag=True
EFFECTIVE=True
EFFECTIVE_CARD=""
def create_deck():
    deck=[]
    colors=["RED-","BLUE-","GREEN-","YELLOW-"]
   
    for color in colors:
        
        
        #creating the number cards
        for i in range(10):
            deck.append(color+str(i))
        for i in range(1,10):
            deck.append(color+str(i))
        # creating draw2
        for i in range(2):
            deck.append(color+"DRAW2")
        #creating skips
        for i in range(2):
            deck.append(color+"SKIP")
        #creating reverse   
            deck.append(color+"REVERSE")
        
    #creating wild cards.
    for i in range(4):
        deck.append("WILD")
        deck.append("WILD-DRAW4")
    random.shuffle(deck)        
    return deck    
   

class player:
    def __init__(self,your_hand,name):
        self.hand=your_hand
        self.name=name
    
    def seperate(self,card):
        seperate_list=[[],[]]
        for i in range(int(len(card))):
            if(card[i]=="-"):
                seperate_list[0]=str(card[0:i])
                seperate_list[1]=str(card[i+1:])
        return seperate_list
            

    def check(self,card):
        global previous_card
        if(card=="WILD") or (card=="WILD-DRAW4" ):
            return True
        
        seperate_list=self.seperate(card)
        flag=previous_card.find(seperate_list[0])
        flag1=previous_card.find(seperate_list[1])
       
            
        if(flag==-1) and (flag1==-1):
            return False
        else:   
            return True
        
    
    def play(self,card):
        global previous_card
        global EFFECTIVE
        global wild_flag
        global wild_draw4_flag
        if(card in self.hand):
            if(self.check(card)):
                self.hand.remove(card)
                previous_card=card
                if(card=="WILD") or (card=="WILD-DRAW4"):
                    if(card=="WILD"):
                        wild_flag=True
                    else:
                        wild_draw4_flag=True
                        
                    while(True):
                        input1=input("Which color do you want to change to ?[YELLOW,GREEN,BLUE,RED]: ")
                        if(input1=="--help"):
                            system('cls')
                            print("Rules are pretty simple, this game is a 2+ player game. \n All players are given 7 cards.\n When your turn comes, play a card that is either of the same color or same number.\n Goal is to finish first.\n Draw2 cards allow you to ask the next player draw 2 cards and skip his turn.\nSkip is a card when played makes the next player skip his turn.\n Reverse card when played reverses the direction of players.\n Wild card can be played at any time irrespective of which color/number was played last, it allows the player to change color. The next player will have to play card of that color.\n Wild-draw4 is same in functionality except the fact that it also forces the next player to pick four cards and skip the his turn.\n If u dont have a card to play then you take a card from the pile and forfeit your turn.\n Note: REVERSE CARD IS USELESS IS 2 PLAYER MODE  ")
               
                            while(True):
                                try:
                                    input2=input("Type --resume here to resume: ")
                                    if(input2=="--resume"):
                                        system('cls')
                                        #input1=input("Which color do you want to change to ?[YELLOW,GREEN,BLUE,RED]")
                                        break
                                    else:
                                        raise Exception
                                except:
                                    print("Invalid Input")
                        else:
                            if((input1!="GREEN") and (input1!="RED") and (input1!="BLUE") and (input1!="YELLOW")):
                                print("INVALID")
                            else:    
                                previous_card=input1;
                                break
                else:
                    wild_flag=False
                    wild_draw4_flag=False
                EFFECTIVE=True
                return True
            else:
                return False
        else:
            return False
    def check_victory(self):
        if(len(self.hand)==0):
            return True
        else:
            return False
        
    def pick(self,number):
        global deck
        for i in range(number):
            try:
                self.hand.append(deck.pop())
            except:
                deck=create_deck()
                self.hand.append(deck.pop())
    
            
def my_find(i):
    global list_players
    global previous_card
    global EFFECTIVE_CARD
    global wild_draw4_flag
    global wild_flag
    if("SKIP" in previous_card):
        EFFECTIVE_CARD="SKIP"
        return True
    elif("REVERSE" in previous_card):
        EFFECTIVE_CARD="REVERSE"
        return True
    elif("DRAW2" in previous_card):
        EFFECTIVE_CARD="DRAW2"
        return True    
    else:
        if(wild_flag):
            EFFECTIVE_CARD="WILD"
            return False
        elif(wild_draw4_flag):
            EFFECTIVE_CARD="DRAW4"
            return True
        else:    
            return False
    
    
    
print("HELLO AND WELCOME TO UNO-VERSION-1")
print("type --help to find the rules page at any point in the game!!")
while(True):
    
    try:
        input1=input("So shall we start ???(y/n): ")
        if(input1=="--help"):
            system('cls')
            print("Rules are pretty simple, this game is a 2+ player game. \n All players are given 7 cards.\n When your turn comes, play a card that is either of the same color or same number.\n Goal is to finish first.\n Draw2 cards allow you to ask the next player draw 2 cards and skip his turn.\nSkip is a card when played makes the next player skip his turn.\n Reverse card when played reverses the direction of players.\n Wild card can be played at any time irrespective of which color/number was played last, it allows the player to change color. The next player will have to play card of that color.\n Wild-draw4 is same in functionality except the fact that it also forces the next player to pick four cards and skip the his turn.\n If u dont have a card to play then you take a card from the pile and forfeit your turn.\n Note: REVERSE CARD IS USELESS IS 2 PLAYER MODE ")
            
            while(True):
                
                try:
                    input2=input("Type --resume here to resume: ")
                    if(input2=="--resume"):
                        system('cls')
                        input1=input("So shall we start ???(y/n): ")
                        break
                    else:
                        raise Exception
                except:
                    print("Invalid Input")
                
        if(input1.upper()!="Y") and (input1.upper()!="N"):
            raise Exception
        if(input1.upper()=="Y"):
            break
    except:
        print("Invalid Input!! Try again!")
        
print("ALRIGHT!!!")
while(True):
    input1=input("HOW MANY PLAYERS ARE PLAYING? ")
    if(input1=="--help"):
        system('cls')
        print("Rules are pretty simple, this game is a 2+ player game. \n All players are given 7 cards.\n When your turn comes, play a card that is either of the same color or same number.\n Goal is to finish first.\n Draw2 cards allow you to ask the next player draw 2 cards and skip his turn.\nSkip is a card when played makes the next player skip his turn.\n Reverse card when played reverses the direction of players.\n Wild card can be played at any time irrespective of which color/number was played last, it allows the player to change color. The next player will have to play card of that color.\n Wild-draw4 is same in functionality except the fact that it also forces the next player to pick four cards and skip the his turn.\n If u dont have a card to play then you take a card from the pile and forfeit your turn.\n Note: REVERSE CARD IS USELESS IS 2 PLAYER MODE ")
       
        while(True):
            try:
                input2=input("Type --resume here to resume: ")
                if(input2=="--resume"):
                    system('cls')
                    #input1=input("HOW MANY PLAYERS ARE PLAYING?")
                    break
                else:
                    raise Exception
            except:
                print("Invalid Input")
                
    else:
        try:
            number1=int(input1)
            break
        except:
            print("Invalid input")

i=1;
while(i<number1+1):
    player_name=input("Enter name of player"+str(i)+": ")
    if(player_name=="--help"):
        system('cls')
        print("Rules are pretty simple, this game is a 2+ player game. \n All players are given 7 cards.\n When your turn comes, play a card that is either of the same color or same number.\n Goal is to finish first.\n Draw2 cards allow you to ask the next player draw 2 cards and skip his turn.\nSkip is a card when played makes the next player skip his turn.\n Reverse card when played reverses the direction of players.\n Wild card can be played at any time irrespective of which color/number was played last, it allows the player to change color. The next player will have to play card of that color.\n Wild-draw4 is same in functionality except the fact that it also forces the next player to pick four cards and skip the his turn.\n If u dont have a card to play then you take a card from the pile and forfeit your turn.\n Note: REVERSE CARD IS USELESS IS 2 PLAYER MODE ")
        
        while(True):
            try:
                input2=input("Type --resume here to resume:  ")
                if(input2=="--resume"):
                    system('cls')
                    #player_name=input("Enter name of player"+str(i))
                  
                    break
                else:
                    raise Exception
            except:
                print("Invalid Input")
             
    else:
        list_players.append(player([],player_name))
        list_players[i-1].pick(7)
        i+=1
    
    


previous_card=deck.pop()
while(True):
    if(previous_card=="WILD") or (previous_card=="WILD-DRAW4"):
        previous_card=deck.pop()
    else:
        break
i=1;
FLAGOMANIA=True
while(FLAGOMANIA):
 
    i=number1*100000
   
    while((i>=0)):
        #print(EFFECTIVE)
        if((EFFECTIVE==True)):
            #print(my_find(9))
            #print(EFFECTIVE_CARD + str("hiiiii"))
            if(my_find(i)):
                if(EFFECTIVE_CARD=="SKIP"):
                    EFFECTIVE=False
                    if(reverse_flag):
                        i+=1
                    else:
                        i-=1
                    
                elif(EFFECTIVE_CARD=="DRAW2"):
                   # print("im in draw2")
                    list_players[i%number1].pick(2)
                    EFFECTIVE=False
                    if(reverse_flag):
                        i+=1
                    else:
                        i-=1  
                elif(EFFECTIVE_CARD=="DRAW4"):
                    list_players[i%number1].pick(4)
                    EFFECTIVE=False
                    if(reverse_flag):
                        i+=1
                    else:
                        i-=1
                    #print(i)
                else:
                    EFFECTIVE=False
                    if(reverse_flag):
                        reverse_flag=False
                    else:
                        reverse_flag=True
                    
                    if(reverse_flag):
                        i+=1
                    else:
                        i-=1
                   
                
        #print(i)        
        print("\n\n")    
        system('cls')
        print("Previous played card is "+str(previous_card))
        print("It's "+list_players[i%number1].name+"'s turn")
        print(list_players[i%number1].hand)
        input1=input("What to play?(Type -1 if you want to pick a card.): ")
        if(input1=="--help"):
            system('cls')
            print("Rules are pretty simple, this game is a 2+ player game. \n All players are given 7 cards.\n When your turn comes, play a card that is either of the same color or same number.\n Goal is to finish first.\n Draw2 cards allow you to ask the next player draw 2 cards and skip his turn.\nSkip is a card when played makes the next player skip his turn.\n Reverse card when played reverses the direction of players.\n Wild card can be played at any time irrespective of which color/number was played last, it allows the player to change color. The next player will have to play card of that color.\n Wild-draw4 is same in functionality except the fact that it also forces the next player to pick four cards and skip the his turn.\n If u dont have a card to play then you take a card from the pile and forfeit your turn.\n Note: REVERSE CARD IS USELESS IS 2 PLAYER MODE ")
       
            while(True):
                try:
                    input2=input("Type --resume here to resume: ")
                    if(input2=="--resume"):
                        system('cls')
                        input1=input("What to play?(Type -1 if you want to pick a card.): ")
                        break
                    else:
                        raise Exception
                except:
                    print("Invalid Input")
        elif(input1=="-1"):
            list_players[i%number1].pick(1)  
            if(reverse_flag):
                i+=1
            else:
                i-=1    
        
        else:
            flag=list_players[i%number1].play(input1)
            FINAL_FLAG=list_players[i%number1].check_victory()
            #print(EFFECTIVE)
            if(FINAL_FLAG):
                print(" "+str(list_players[i%number1].name)+" "+"is the winner!!!!!!!!!")
                FLAGOMANIA=False
                break
            if(flag):
                if(reverse_flag):
                    i+=1
                else:
                    i-=1
            
                
            else:
                print("INVALID INPUT")
                
            
    
    
print("CONGRATS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")    
        
