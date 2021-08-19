print("                                                         WELCOME TO  GAMING ARCADE                                                          ")
print("Welcome to GAMING ARCADE where we offer you a wide variety of games for all gaming lovers!")
print("Divulge into these exciting games where we have multiplayer and singleplayer!")
def Football1():
    def habibi():
        print("Enter your choice as follows.")
        print("Enter 1 to play Football Auction")
        print("Enter 2 to play Odd Or Even")
        print("Enter 3 to play Football")
        print("Enter 4 to exit")
        choice_top=int(input("Enter your choice="))
        if choice_top==1:


            print("                                                        GAMING ARCADE!                                                                        ")
            print("                                                     FOOTBALL AUCTION GAME                                                                      ")
            #Rules for the game
            print("Rules:\n1.Players to enter their name in order\n2.Agree on a budget\n3.Select the theme for your game\n4.Enter your players,bid for them and append them into their suitable positions\n5.In case you use more money than your budget, you will lose automatically\nTHANK YOU")
            def FootballAuction():
                #Player1 should enter his/her name
                Player1=input("Enter Player1 Name:")
                #Player2 should enter his/her name
                Player2=input("Enter Player2 Name:")
                #Players need to play according to the amount of money they hold, else they would automatically lose the game.
                Budget=int(input("Enter Budget"))
                #A theme is what suggests which footballers, the players need to focus on buying for their team.
                #The theme suggests which footballers are better.
                #For example, if the theme is "Legends", all the footballers from the past are also up for grabs.
                Theme=input("Decide on the theme of this auction(All time,Prime,Season,etc.)")
                #Bye default, player1 starts.
                print("Team 1 starts")
                #The football pitch is in the following list format.


                #Full Forms for various Positions on the field are given below.
                #GK:Goalkepper
                #LB:Left Back
                #LCB:Left Centre Back
                #CB:Centre Back
                #RCB:Right Centre Back
                #RB:Right Back
                #LWB:Left Wing Back
                #LCDM:Left Centre Defensive Midfield
                #CDM:Centre Defensive Midfield
                #RCDM:Right Centre Defensive Midfield
                #RWB:Right Wing Back
                #LM:Left Midfield
                #LCM:Left Centre Midfield
                #CM:Centre Midfield
                #RCM:Right Centre Midfield
                #RM:Right Midfield
                #LCAM:Left Centre Attacking Midfield
                #CAM:Centre Attacking Midfield
                #RCAM:Right Centre Attacking Midfield
                #LW:Left Wing
                #CF:Centre Forward
                #RW:Right Wing
                #LF:Left Forward
                #ST:Striker
                #RF:Right Forward
                
                GK1line=["  x    ","  x      ","  GK   ","  x     ","  x    "]
                Def1line=["  RB   ","  RCB    ","  CB   ","  LCB   ","  LB   "]
                DefMid1line=["  RWB  ","  RCDM   ","  CDM  ","  LCDM  ","  LWB  "]
                Mid1line=["  RM   ","  RCM    ","  CM   ","  LCM   ","  LM   "]
                AttackMid1line=["  x    ","  RCAM   ","  CAM  ","  LCAM  ","  x    "]
                CF1line=["  RW   ","  x      ","  CF   ","  x     ","  LW   "]
                Attack1line=["  x    ","  RF     ","  ST   ","  LF    ","  x    "]
                 
                GK2line=["  x    ","  x      ","  GK   ","  x     ","  x    "]
                Def2line=["  LB   ","  LCB    ","  CB   ","  RCB   ","  RB   "]
                DefMid2line=["  LWB  ","  LCDM   ","  CDM  ","  CDM  ","  RWB  "]
                Mid2line=["  LM   ","  LCM    ","  CM   ","  RCM   ","  RM   "]
                AttackMid2line=["  x    ","  LCAM   ","  CAM  ","  RCAM  ","  x    "]
                CF2line=["  LW   ","  x      ","  CF   ","  x     ","  RW   "]
                Attack2line=["  x    ","  LF     ","  ST   ","  RF    ","  x    "]
                LB1=[]
                LB2=[]
                
                

                
                 
                
                print("In this Game of Auction, your pitch will look like this:")

                print("                        Player1                        ")
                print(GK1line)
                print(Def1line)
                print(DefMid1line)
                print(Mid1line)
                print(AttackMid1line)
                print(CF1line)
                print(Attack1line)
                print("                            V.S                   ")
                print(Attack2line)
                print(CF2line)
                print(AttackMid2line)
                print(Mid2line)
                print(DefMid2line)
                print(Def2line)
                print(GK2line)
                print("                        Player2                        ")


                #After buying the players can assign the following positions to their footballers
                print("Your options for types of positions are GK,D,DM,M,AM,F and A")
                #Both teams are allowed 11 footballers each.
                for p in range(0,22):
                    #Name of footballer to be bought by team 1.
                    Player=input("Enter player")
                    while True:
                        #Bid for the first team.
                        Bid1=int(input("Team1s bid:"))
                        #Bid for the second team.
                        Bid2=int(input("Team2s bid:"))
                        if Bid2<Bid1:
                            #For if Team2 wishes to sell, they can.
                            x=input("Does Team2 wish to sell?")
                            #If they do, Team1 can assign positions.
                            if x=="yes":
                                Position=input("which position will you play him")
                                #GK: Goalkeeper
                                if Position=="GK":
                                    GK1line[2]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    #To show how much money Player1 has left.
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    #To show how much money Player2 has left.
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #D:Defence
                                elif Position=="D":
                                    #To choose exact position on the Defensive line.
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Def1line[n]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #DM:Defensive Midfield
                                elif Position=="DM":
                                    #To choose exact position on the Defensive Midfield line.
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    DefMid1line[n]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #M:Midfield
                                elif Position=="M":
                                    #To choose exact position on the Midfield line.
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Mid1line[n]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #AM:Attacking Midfield
                                elif Position=="AM":
                                    #To choose exact position on the Attacking Midfield line.
                                    AttackMid1line[2]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #F:Forward
                                elif Position=="F":
                                    #To choose exact position on the Forward line.
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    CF1line[n]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                #A:Attack
                                elif Position=="A":
                                    #To choose exact position on the Attacking line.
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Attack1line[n]=Player
                                    LB1.append(Bid1)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                else:
                                    habibi()
                                
                                
                            else:
                                print("Go on then")

                            

                        elif Bid2>Bid1:
                            x=input("Does Team1 wish to sell?")
                            #For if Team1 wishes to sell, they can.
                            if x=="yes":
                                #If they do, Team2 can assign positions.
                                Position=input("which position will you play him")
                                if Position=="GK":
                                    GK2line[2]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="D":
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Def2line[n]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="DM":
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    DefMid2line[n]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="M":
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Mid2line[n]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="AM":
                                    AttackMid2line[2]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="F":
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    CF2line[n]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                elif Position=="A":
                                    n=int(input("enter 0,1,2,3,4 according to which postion you want"))
                                    Attack2line[n]=Player
                                    LB2.append(Bid2)
                                    print(GK1line)
                                    print(Def1line)
                                    print(DefMid1line)
                                    print(Mid1line)
                                    print(AttackMid1line)
                                    print(CF1line)
                                    print(Attack1line)
                                    print("                    V.S                   ")
                                    print(Attack2line)
                                    print(CF2line)
                                    print(AttackMid2line)
                                    print(Mid2line)
                                    print(DefMid2line)
                                    print(Def2line)
                                    print(GK2line)
                                    print(Player1,"has",Budget-sum(LB1),"left")
                                    print(Player2,"has",Budget-sum(LB2),"left")
                                    break
                                else:
                                    habibi()
                                
                                
                            else:
                                print("Go on then")

                           

                
                        
                        
                            
                        

                

                            


                #The final roster is shown to the Judge(s)
                print("Team1 vs Team2:")
                
                print("                        Player1                        ")
                print(GK1line)
                print(Def1line)
                print(DefMid1line)
                print(Mid1line)
                print(AttackMid1line)
                print(CF1line)
                print(Attack1line)
                print("                    V.S                   ")
                print(Attack2line)
                print(CF2line)
                print(AttackMid2line)
                print(Mid2line)
                print(DefMid2line)
                print(Def2line)
                print(GK2line)
                print("                        Player1                        ")

                #In case, Players decide to go over the budget.
                if sum(LB1)>Budget:
                    print(Player1,"is broke. They lose")
                  
                elif sum(LB2)>Budget:
                    print(Player2,"is broke. They lose")
                    
                else:
                    print(Player1,"has",Budget-sum(LB1),"left")
                    print(Player2,"has",Budget-sum(LB2),"left")

                #Judge enters scores for both players
                J=input("Enter name of the judge")
                JsA=int(input("Enter Score for Team1")) 
                JsB=int(input("Enter Score for Team2"))

                print(J," Score for Team1 is:",JsA)
                print(J," Score for Team2 is:",JsB)

                #If Team1 gets a higher score.
                if JsA>JsB:
                    print(Player1,"wins")

                #If Team2 gets a higher score.
                elif JsA<JsB:
                    print(Player2,"wins")

                #If Team1 and Team2 get an equal score.
                else:
                    print("match is a draw")


            FootballAuction()
                
            
            

        elif choice_top==2:
                #To make Odd or Even game


            def OOE():
                import random
                import datetime
                import time
                l=[]
                l_comp=[]
                #To make sure the input is between 1 and 6        
                def inpt1():
                    r=int(input("Enter run between 0-6="))
                    assert r in range(1,7),'Please enter a valid input'
                    return r
                 #To remove the assertion error
                def exc1():
                    try:
                        return inpt1()
                    except Exception as e:
                        print(e)
                        return exc1()
                #User batting     
                def u_bat():
                    global a
                    global n
                    global l
                    wickets=10
                    #Commentary list
                    commentary_batting=["The ball rattles the stump.BOWLED!","Poor shot by the batsman and he/she has given away a good start","The batsman has hit it high up in the air.......AND ITS CAUGHT!","The batsman is trapped in front of the wickets giving a simple L.B.W decision for the umpire!","Bit of hesitation between the batsmen and its RUN OUT!","That is a lightning quick stumping from the keeper!","Oh no!The batsman has lost his balance and fallen onto the stumps!he is HITWICKET!"] 
                    wickets_gone=0
                    four=0
                    six=0
                    for x in range(a):
                        run=exc1()
                        r=random.randint(1,6)
                        if run>4:
                            r=random.randint(4,6)
                        if run==r:
                            wickets-=1
                            wickets_gone+=1
                            com=random.choice(commentary_batting)
                            print(com)
                            print("Its OUT!")
                            print('You have lost',wickets_gone,'wicket')
                            print('your score is ',sum(l),"For",wickets_gone,"Wickets")
                        else:
                            l.append(run)
                            print('your score is ',sum(l),"For",wickets_gone,"Wickets")
                            print("Balls bowled is",len(l)+wickets_gone)
                        if wickets==0:
                            print('You are allout')
                            break
                    for i in l:
                        if i==4:
                            four+=1
                        elif i==6:
                            six+=1
                    #Strike rate variable
                    strike_rate=(sum(l)/a)*100
                    #Runs per ball bowled excluding wickets
                    print('Runs per ball is',l)
                    #INNINGS SUMMARY
                    print('Your total score is',sum(l),"/",wickets_gone,"For",len(l)+wickets_gone,"balls")
                    #Run rate of the user
                    print('Your run rate is=',(sum(l)/n))
                    #Strike rate of the user
                    print('Your strike rate is=',round(strike_rate,2))
                    #Number of sixes hit by the user
                    print("No. of six is=",six)
                    #Number of fours hit by the user
                    print("No. of fours is=",four)
                    
                #To make sure the input is between 1-6
                def inpt2():
                    r=int(input("Enter ball between 0-6="))
                    assert r in range(1,7),'Please enter a valid input'
                    return r
                #To remove assertion error
                def exc2():
                    try:
                        return inpt2()
                    except Exception as e1:
                        print(e1)
                        return exc2()
                #User's Bowling
                def c_bat():
                    global a
                    global n
                    global l_comp
                    global l
                    wickets_comp=10
                    p_comp=0
                    six_comp=0
                    four_comp=0
                    #Commentary list
                    commentary_bowl=["The ball has edged and caught by the keeper. FANTASTIC BALL!","The bowls goes through the bat and pad gap....CLEAN BOWLED!","The ball is hit straight to the fielder and he is gone!","Steps out and completely misses the ball resulting in stumping! WHAT A BEAUTY!","Confusion between the batsmen and the have both run to the same end.........RUN OUT!"]
                    for x in range(a):
                        ball=exc2()
                        ball_list=[]
                        ball_list.append(ball)
                        k=random.randint(1,6)
                        if (sum(l)/a)*100>250:
                            k=random.randint(3,6)
                        print("Computer has scored",k)
                        if ball==k:
                            wickets_comp-=1
                            p_comp+=1
                            com2=random.choice(commentary_bowl)
                            print('You have taken a wicket')
                            print(com2)
                            print('Computer score is ',sum(l_comp),"For",p_comp,"Wickets")
                        else:
                            l_comp.append(k)
                            print('Computer score is ',sum(l_comp),"For",p_comp,"Wickets")
                            print("Balls bowled is",len(l_comp)+p_comp)
                        if wickets_comp==0:
                            print('Opponent is allout!')
                            print('Good job')
                            break
                    for i in l_comp:
                        if i==6:
                            six_comp+=1
                        elif i==4:
                            four_comp+=1
                    #Strike rate variable
                    comp_strike_rate=(sum(l_comp)/a)*100
                    #Runs per every ball bowled. Only wickets are excluded
                    print('Runs per ball is',l_comp)
                    #INNINGS SUMMARY
                    print('Computers total score is',sum(l_comp),"/",p_comp,"For",len(l_comp)+p_comp,"balls")
                    #Run rate of computer
                    print('Computers run rate is=',(sum(l_comp)/n))
                    #Strike rate of computer
                    print('Computers strike rate is=',round(comp_strike_rate,2))
                    #No. of sixes hit by computer
                    print("No. of sixes hit is=",six_comp)
                    #No. of fours hit by the computer
                    print("No. of fours hit is=",four_comp)       
                   
                #Heading for the game
                print("                                                        GAMING ARCADE!                                                                        ")
                print("                                                     ODD OR EVEN GAME                                                                      ")

                #Help for user to understand the game
                def instructions():
                    print("1.About the game")
                    print("2.Controls for the game.")
                    how_play=int(input("Enter your choice="))
                    if how_play==1:
                        #Info on the game
                        print("Odd or even is a game based on cricket where two players battle for victory.The game is simple. You have to score more than your opponent and try to make him all out or finish the given overs inorder to win. In this game, you compete against the computer in an exciting duel. All the best!")
                    elif how_play==2:
                        #Info on the features of the game
                        #To settle which team bats or bowls first.
                        print("Toss:-")
                        print("Select what you want to do wether bat or ball. Remember toss is very important and it decides your further strategy in the game.")
                        print("Batting:-")
                        print("Enter a number between 0 and 6. Whatever you put will be counted as your score. All the numbers will be added to make the total score. If your number and computer's number matches, that means you have lost a wicket! You have 10 wickets per game, try to score as much as possible without losing wickets mate!")
                        print("Bowling:-")
                        print("Enter a number between 0 and 6. If yours and computers number matches, you have taken a wicket mate! Try to take as many wickets as possible to gain advantage in the game.")



                #Menu Driven programme
                n=0
                a=1
                def menu99():
                    #Importing all variables globally for data storage,display and defining
                    global l_comp, p_comp, six_comp, four_comp
                    global a, n, l
                    p_comp = six_comp = four_comp = 0
                    l_comp = []
                    l=[]
                    #If the user wants to play.
                    print("Enter 1 to play game.")
                    #If the user wants to view the scoreboard.
                    print("Enter 2 to open scoreboard.")
                    #If the player needs to see the instructions.
                    print("Enter 3 for help with the game.")
                    #For the user to choose from the above options.
                    menu=int(input("Enter your choice="))
                    if menu==1:
                        #Toss
                        toss=input("Do you wish to bat first or bowl?[bat/bowl]=").lower()
                        #Number of overs. Each over has 6 balls
                        n=int(input("Enter no. of overs match you want to play="))
                        a=n*6
                        #Asserting the toss to avoind invalid input
                        assert toss=='bat' or toss=='bowl','Invalid Input'
                        if toss=='bat':
                            u_bat()
                            #Giving target
                            print("The target for the opponent is=",sum(l)+1)
                            #Making the game realistic with commentary
                            print("COMMENTATORS=> Players are walking off the field. Both the sides look satisfied with their performance but what is important is the fact which side will emerge victorious. I can feel that this is going to be a nail biting finish by either team. Anything can happen as in cricket, IT'S JUST A MATTER OF ONE BALL!")
                            #Emphasizing on important aspects of the game
                            time.sleep(5)
                            print("Fielders are coming out in the hope of vanquishing the other side.")
                            time.sleep(5)
                            print("Fielders are set")
                            print("Get ready to ball.")
                            c_bat()
                        elif toss=="bowl":
                            c_bat()
                            print("Target for you is", sum(l_comp)+1)
                            print("COMMENTATORS=> Players are walking off the field. Both the sides look satisfied with their performance but what is important is the fact which side will emerge victorious. I can feel that this is going to be a nail biting finish by either team. Anything can happen as in cricket, IT'S JUST A MATTER OF ONE BALL!")
                            time.sleep(5)
                            print("Fielders are coming out in the hope of vanquishing the other side.")
                            time.sleep(5)
                            print("Fielders are set")
                            print("Get ready to bat.")
                            u_bat()
                        #Final match result

                        #If computer wins
                        if sum(l_comp)>sum(l):
                            print("You have lost! \nYou have lost by",sum(l_comp)-sum(l)-1,"Runs")
                            print("Better luck next time")
                            print("Train harder!")

                        #If user wins
                        elif sum(l_comp)<sum(l):
                            print("You have won! \nYou have beaten the opponent by",sum(l)-sum(l_comp)-1,"Runs")
                            print("Good game")

                        #If it is a draw
                        elif sum(l_comp)==sum(l):
                            print("Its a draw")

                    

                #Making a scoreboard.

                        f=open("LEADERBOARD.txt","a")
                        name_sb=input('Enter your name=')
                        entry=datetime.datetime.now()
                        #Making variable to store entry time,bame,score
                        user=str(entry)+"////"+name_sb+" "+str(sum(l))+":"+"Computer"+" "+str(sum(l_comp))+"\n"
                        f.write(user)
                        f.close()
                        print("Your game data is stored.")
                    elif menu==2:
                        example=open("LEADERBOARD.txt","a")
                        example.close()
                        f=open("LEADERBOARD.txt","r")
                        score1=f.read()
                        print(score1)
                        f.close()
                    elif menu==3:
                        instructions()
                    else:
                        print('invalid input')
                menu99()

                #If the user wants to play again
                def tRy():
                    while True:
                        tRy=(input("Do you want to play again?[Y,N]=")).lower()
                        assert tRy=='y' or tRy=='n','Invalid input'
                        if tRy=='y':
                            menu99()
                        elif tRy=='n':
                            print("Thank you for playing!")
                            break
                tRy()
            OOE()
        elif choice_top==3:
            #Football game
            import time
            import random
            import datetime
            p=0
            p_comp=0
            print("                                                       Welcome to GAMING ARCADE!                                                   ")
            print("                                                                    FOOTBALL!                                                                               ")

            def attack():
                #Attacking plays by user
                print("Time to create winning plays!")
                for i in range(3):
                    n2=int(input("Enter a no. between 4-6="))
                    k2=random.randint(4,6)
                    if n2==k2:
                        print("You have lost possession.")
                        comp_mid()
                else:
                    print("Time to score!")
                    scoring()
            def scoring():
                #Scoring for user
                n=int(input("Enter no. between 7-9="))
                k=random.randint(7,9)
                if n==k:
                    print("Whatta beautiful save by the goalie!")
                    attack()
                else:
                    print("AND ITS A GOOOALLLLL!")
                    p+=1
                    print("Score is ",p,"-",p_comp)
                    print("Beautiful goal and the players are celebrating.")
                    print("Truly exceptional I must tell you!")
                    print("They have put all their might into this one!")
                    time.sleep(5)
                    print("Players are getting back to their positions!")
                    if p>p_comp:
                            print("You are beating the computer!")
                    elif p<p_comp:
                            print("Hurry! you are losing!")
                    elif p==p_comp:
                            print("Both players are tied!")
                    comp_mid()

            def comp_mid():
                #Ball in compters defence
                global menu99
                print("Computer has the possesion of the ball!")
                try:
                    for i in range(3):
                        n=int(input("Enter no. between 1-3="))
                        k=random.randint(1,3)
                        if n==k:
                            print("You have got the possession")
                            attack()
                        else:
                            print("The ball is in the your side.")
                            print("TIME TO DEFEND!")
                            comp_attack()
                except:
                    ex=(input("Do you want to quit?[y/n]=")).lower()
                    if ex=='y':
                        f=open("Football_Scoreboard.txt","a")
                        name=input("Enter your name=")
                        enTry=datetime.datetime.now()
                        entry=str(enTry)+'////'+name+":"+str(p)+'::::'+"Computer"+":"+str(p_comp) +"\n"
                        f.write(entry)
                        f.close()
                        print("Your game data is stored")
                        menu99()
                    else:
                        print("Okay continure!")
                        comp_mid()
            def comp_attack():
                #Computer making atacking plays
                print("Can the computer create winning plays?")
                for i in range(3):
                    n2=int(input("Enter a no. between 4-6="))
                    k2=random.randint(4,6)
                    if n2==k2:
                        print("You have got the possession.")
                        mid()
                else:
                    print("Time for the goalie to do a wonder!")
                    comp_scoring()
            def comp_scoring():
                #Scoring for Computer
                print("You must stop this shot or else the comp will score!!!")
                for i in range(3):
                    n=int(input("Enter no. between 7-9="))
                    k=random.randint(7,9)
                    if n==k:
                        print("Whatta beautiful save by the goalie!")
                        comp_attack()
                    else:
                        print("AND ITS A GOOOALLLLL!")
                        print("COMPUTER SCORES A BEAUTY!")
                        p_comp+=1
                        print("Score is ",p,"-",p_comp)
                        print("What an intense game this is!")
                        print("The computer is ruthless dribbling and passing through the player's defense as if it were a joke!")
                        time.sleep(5)
                        print("Yes! truly spectacular. This battle between these two teams will be remembered for ages!")
                        if p>p_comp:
                            print("You are beating the computer!")
                        elif p<p_comp:
                            print("Hurry! you are losing!")
                        elif p==p_comp:
                            print("Both players are tied!")
                        mid()
                    
            def mid():
                #Ball in defence area for user
                print("To exit the game just press enter without entering anything!")
                
                try:
                    for i in range(0,3):
                        n=int(input("Enter no. between 1-3="))
                        k=random.randint(1,3)
                        if n==k:
                            print("You have lost possession.")
                            comp_attack()
                    else:
                        print("The ball is in the opponent side.")
                        print("TIME TO ATTACK!")
                        attack()
                except:
                    ex=(input("Do you want to quit?[y/n]=")).lower()
                    if ex=='y':
                        f=open("Football_Scoreboard.txt","a")
                        name=input("Enter your name=")
                        enTry=datetime.datetime.now()
                        #Storage of data for the game
                        entry=str(enTry)+'////'+name+":"+str(p)+'::::'+"Computer"+":"+str(p_comp) +"\n"
                        f.write(entry)
                        f.close()
                        print("Your game data is stored")
                    else:
                        print("Okay continue!")
                        mid()
        
            def Instructions():
                #To help user
                print("Enter 1 to know about the game!")
                print("Enter 2 to learn the controls!")
                h=int(input("Enter your choice="))
                if h==1:
                    #Info on the game
                    print("Football is a game between two teams. In our case, the player and computer. Aim is simple, whoever scores most goals wins! Do not underestimate the computer!This game is derived from the origins of Odd Or Even but with slightly different rules.")
                elif h==2:
                    #Info on aspects of game
                    print("You have the ball in starting. You have three chances to get past your side of the court and into the midfield to create attacking chances. Beware, computer also has some tricks up its sleeve! If the computer gets the ball from you in your defense area, it has chances to create winning plays and score! But you always have a chance to win the ball back. Keep dribbling and going through the computers attack,midfield and defense to score against the goalie! But let me warn you again, Computer has some really good tricks up it's sleeve! ")
                    print("MAY THE ODDS EVER BE IN YOUR FAVOUR!")
                        
             #Menu for the code   
            def menu199():
                print("Enter 1 to play the game!")
                print("Enter 2 to open the Scoreboard!")
                print("Enter 3 for help")
                print("Enter 4 to exit to Main Menu")

                choice_menu=int(input("Enter your choice="))
                if choice_menu==1:
                    mid()
                elif choice_menu==2:
                    f=open("Football_Scoreboard.txt","r")
                    read1=f.read()
                    print(read1)
                elif choice_menu==3:
                    Instructions()
                else:
                    return
            menu199()
            #If the user wants to play again
            def TRY():
                while True:
                    tRy=(input("Do you want to play again?[Y,N]=")).lower()
                    assert tRy=='y' or tRy=='n','Invalid input'
                    if tRy=='y':
                        menu199()
                    elif tRy=='n':
                        print("Thank you for playing!")
                        print("Please play again!")
                        habibi()
                    else:
                        break
            TRY()
    habibi()
    #Code for running the whole code again
    def final():
        while True:
            p=(input("Do you want to play again?[y/n]")).lower()
            if p=='y':
                habibi()
            else:
                break
    final()
Football1()
