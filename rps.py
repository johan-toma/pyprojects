import random

#value >= 0 och <= 5000 blir sten
#value >=5001 och <= 6500 blir paper
#value >=6501 <=10000 blir sax

def ai_move():
    start = 0.0
    end = 10000.0
    rand_num = random.uniform(start, end)
    
    if start >= rand_num and rand_num <= 5000:
        choice = "Rock"
        return choice
    elif 5001 >= rand_num and rand_num <= 6500:
        choice = "Paper"
        return choice
    else:
        choice = "Scissors"
        return choice

#move 1 ai choice
#move 2 player choice
#if mp move1 player 1 choice and move2 player 2 choice
def win_logic(move1, move2):
    rock = "Rock"
    paper = "Paper"
    scissor = "Scissor"
    
    if move1.lower() == rock.lower():
        if move2.lower() == rock.lower():
            return 3
        elif move2.lower() == paper.lower():
            return 2
        else:
            return 1
    elif move1.lower() == paper.lower():
        if move2.lower() == paper.lower():
            return 3
        elif move2.lower() == rock.lower():
            return 1
        else:
            return 2
    else:
        if move2.lower() == scissor.lower():
            return 3
        elif move2.lower() == rock.lower():
            return 2
        else:
            return 1
    pass

def play_sp():
    valid_choices = ["Paper", "Scissor", "Rock"]
    isValid = False
    player_wins = 0
    ai_wins = 0
    quit = "Q"
    while True:
        ai_choice = ai_move()
        print("Make your Choice: (ROCK), (PAPER), (SCISSOR)")
        print("To Quit Press Q")
        player_choice = input(">> ")
        
        if player_choice.lower() == quit.lower():
            print("You have decided to QUIT")
            exit()
        
        for valid in valid_choices:
            if valid.lower() == player_choice.lower():
                isValid = True
        
        if isValid == False:
            print("Try Again, Enter a valid choice!")
        elif isValid == True:
            #2, player wins or 1 ai wins, 3 draw
            check_winner = win_logic(ai_choice, player_choice)
            if check_winner == 2:
                player_wins = player_wins + 1
                print(f"You WIN!!!\nAI had selected {ai_choice.upper()} and you had {player_choice.upper()}\nAI: WINS {ai_wins}\t\tPlayer: WINS {player_wins}")
            elif check_winner == 1:
                ai_wins = ai_wins + 1
                print(f"You LOST :(\nAI had selected {ai_choice.upper()} and you had {player_choice.upper()}\nAI: WINS {ai_wins}\t\tPlayer: WINS {player_wins}")
            elif check_winner == 3:
                print(f"ITS A DRAW!!\nAI SELECTED {ai_choice.upper()} AND YOU HAD {player_choice.upper()}\nAI: WINS {ai_wins}\t\tPlayer: WINS {player_wins}")
    return

if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors Game!!")
    while True:
        play_sp()