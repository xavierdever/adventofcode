# #specs = [("A",1), ("B",2), ("C", 3), ("X",1), ("Y",2), ("Z",3)]
specs = {'A' : 1, 'B': 2, 'C' : 3, 'X' : 1, 'Y' : 2, 'Z' : 3}
# gameresults=[("0","0",0)]
# list=[("0","0",0)]
# for k, v in specs.items(): 
#     print(k,"=", v)
score = 0
with open('input3.txt') as gamelist :
    for game in gamelist:
        result=0
        player1 = game[0]
        player2 = game[2]
        if(player2 == 'X'):
            if (player1 == 'A'):
                result=3
            elif(player1=='B'):
                result=1
            elif(player1=='C'):
                result=2
        elif(player2 == 'Y'):
            if (player1=='A'):
                result=4
            elif(player1=='B'):
                result=5
            elif(player1=='C'):
                result=6
        elif(player2 =='Z'):
            if(player1=='A'):
                result=8
            elif(player1=='B'):
                result=9
            elif(player1=='C'):
                result=7
        #gameresults.append((player1,player2,result))
        #list.append((specs.get(player1), specs.get(player2), result))
        score += result


        
print(score)
#print(gameresults)