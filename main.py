import random

winning_boards = [
    
    # Rows
    
    [[1, 1, 1], 
     [0, 0, 0], 
     [0, 0, 0]],
    
    [[0, 0, 0], 
     [1, 1, 1], 
     [0, 0, 0]],
    
    [[0, 0, 0], 
     [0, 0, 0], 
     [1, 1, 1]],
    
    # Columns
    
    [[1, 0, 0], 
     [1, 0, 0], 
     [1, 0, 0]],
    
    [[0, 1, 0], 
     [0, 1, 0], 
     [0, 1, 0]],
    
    [[0, 0, 1], 
     [0, 0, 1], 
     [0, 0, 1]],
    
    # Diagonals
    
    [[1, 0, 0], 
     [0, 1, 0], 
     [0, 0, 1]],
    
    [[0, 0, 1], 
     [0, 1, 0], 
     [1, 0, 0]]
    
]

class Player:
    def __init__(self, team):
        self.team = team           

def display_board(board):
    
    print("")
    
    for row in board:
        
        print(" | ".join("•" if cell == 0 else str(cell) for cell in row))
        print("-" * 9)

    print("")

        
def select_coord(board, player):
    
    while True:
        
        display_board(board)
        
        try:
            
            x, y = map(int, input(f"Player '{player.team}', select the x and y co-ordinate for your placement (leave space in-between): ").split())
            x -= 1
            y -= 1
            
            if 0 <= x <= 2 and 0 <= y <= 2:
                
                if board[y][x] == 0:
                    
                    board[y][x] = player.team
                    break
                
                else:
                    
                    print("Position already occupied, enter another co-ordinate.")
                    
            else:
                
                print("Either x or y are out of the boundaries of the 3x3 board, please re-select values between 1 and 3.")
                
        except ValueError:
            
            print("Invalid input, please enter two integers separated by space.")

def bot_move(board, bot):
    
    while True:
        
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        
        if board[y][x] == 0:
            
            board[y][x] = bot.team
            break

def check_winner(board, player):
    
    player_symbol = 'x' if player.team == 'x' else 'o'
    
    for winning_board in winning_boards:
        
        is_winner = True
        
        for i in range(3):
            
            for j in range(3):
                
                if winning_board[i][j] == 1 and board[i][j] != player_symbol:
                    is_winner = False
                    break
                
                elif winning_board[i][j] == -1 and board[i][j] != player_symbol:
                    is_winner = False
                    break
                
            if not is_winner:
                break
            
        if is_winner:
            return True
        
    return False

def play():
    
    teams = ['x', 'o']
    
    while True:
        
        user_team = input("Input 'x' or 'o': ").lower()
        
        if user_team in teams:
            break
        
        print("Invalid input, please try again.")

    user = Player(user_team)
    bot_team = 'o' if user_team == 'x' else 'x'
    bot = Player(bot_team)

    print(f"Your team: {user.team} | Bot's team: {bot.team}")

    tic_tac_toe_board = [
        
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        
    ]

    while True:
        
        select_coord(tic_tac_toe_board, user)
        
        if check_winner(tic_tac_toe_board, user):
            
            display_board(tic_tac_toe_board)
            
            print("Congratulations! You win!")
            break
        
        if all(0 not in row for row in tic_tac_toe_board):
            
            display_board(tic_tac_toe_board)
            
            print("It's a tie!")
            break

        bot_move(tic_tac_toe_board, bot)
        
        if check_winner(tic_tac_toe_board, bot):
            
            display_board(tic_tac_toe_board)
            
            print("Bot wins!")
            break

play()
