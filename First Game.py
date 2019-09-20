#!/usr/bin/python3
# Alex Jordan
# 9/6/19

'''Building a game with Python'''


game_running = True 


while game_running == True:
    new_round = True
    player = {'name': 'Alex', 'attack': 13, 'heal': 16, 'health': 100}
    monster = {'name': 'Brian', 'attack': 12, 'health': 100}  
    
    print('---' * 7)
    player['name'] = input("Enter Player name ")
    
    while new_round == True:
    
        player_won = False
        monster_won = False
        
    
    print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        
        player_choice = str(input())
        
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack'] 
            if monster['health'] <= 0:
                player_won = True
            
            else: 
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True
            
            print(monster['health'])
            print(player['health'])
        
            
        elif player_choice == '2':
            print('Heal player')
            
        elif player_choice == '3':
            new_round = False
            game_running = False
            
        else:
            print('Invalid Input')
            
        if player_won == True or monster_won == True:
            new_round = False
                