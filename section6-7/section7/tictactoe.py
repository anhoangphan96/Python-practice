import random
#làm sạch terminal
def clear_input():
  print("\n"*100)
test_board = ['#','X','O','X','O','X','O','X','X','X']


#hiển thị bàn cờ
def display_board(board):
  print(board[7] + "|" + board[8] + "|" + board[9] )
  print("-----")
  print(board[4] + "|" + board[5] + "|" + board[6] )
  print("-----")
  print(board[1] + "|" + board[2] + "|" + board[3] )


#Setup game giúp user chọn dấu của mình là X hay O
def player_input():
  player1 = input("Player 1 please choose your mark X or O: ")
  while player1 != "X" and player1 != "O":
    print("Please choose valid mark X or O only! ")
    player1 = input("Player 1 please choose your mark X or O: ")
  if player1 == "X":
    player2 = "O"
  else:
    player2 = "X"
  return (player1, player2)

#thực hiện lượt đánh dấu
def place_marker(board, marker, position):
  board[position] = marker

#kiểm tra xem đã có người thắng chưa
def win_check(board, mark):
  if board[7] == board[8] == board[9] == mark or board[4] == board[5] == board[6] == mark or board[1] == board[2] == board[3] == mark or board[1] == board[4] == board[7] == mark or board[1] == board[4] == board[7] == mark  or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
    return True
  else:
    return False  

#Chọn user chơi trước
def choose_first():
  rand_int = random.randint(0,1)
  if(rand_int ==0):
    return "Player1"
  else:
    return "Player2"

#Check xem vị trí đánh cờ rổng hay không
def space_check(board, position):
  print(board[position] == " ")
  return board[position] == " "

#Check xem toàn bộ bàn cờ còn chổ không:
def full_board_check(board):
  return not " " in board

#hỏi vị trí tiếp theo của người chơi (dưới dạng số 1-9) rồi sử dụng hàm từ bước 6 để kiểm tra xem đó có phải là vị trí trống hay không. Nếu có thì trả lại vị trí để sử dụng sau.
def player_choice(board):
  position = int(input("Please choose the position from 1-9 you would like to mark: "))
  while not (position in range(1,10) and space_check(board,position)):
    print("Please choose valid number from 1-9! and make sure it is empty")
    position = int(input("Please choose the position from 1-9 you would like to mark: "))
  else:
    return position

#function để chơi lại:
def replay():
  choice = input("Play again? Enter Yes or No: ")
  clear_input()
  return choice == "Yes"


#Welcome và sử dụng while loop để tiếp tục trò chơi
clear_input()
print('Welcome to Tic Tac Toe!')
while True:
  #setup bàn cờ, ký hiệu của 2 người chơi, chọn người chơi đi trước:
  the_board = [" "]*10
  the_board[0] = "#"
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn + " will go first")
  #Hỏi user sẳn sàn chơi chưa
  play_game = input("Ready to play? y or n: ")

  if play_game == "y":
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn =="Player 1":
      #hiển thị bàn cờ để người chơi 1 chọn vị trí
      display_board(the_board)
      #chọn vị trí muốn đánh
      position = player_choice(the_board)
      #Đánh dấu vào bàn cờ
      place_marker(the_board, player1_marker, position)
      #Check xem người chơi có win không
      if win_check(the_board,player1_marker):
        display_board(the_board)
        print("Player 1 has won!")
        game_on = False
        
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print("Tie Game!")
          game_on =False
        else:
          turn = "Player 2"
    else: 
      #hiển thị bàn cờ để người chơi 1 chọn vị trí
      display_board(the_board)
      #chọn vị trí muốn đánh
      position = player_choice(the_board)
      #Đánh dấu vào bàn cờ
      place_marker(the_board, player2_marker, position)
      #Check xem người chơi có win không
      if win_check(the_board,player2_marker):
        display_board(the_board)
        print("Player 2 has won!")
        game_on = False
      else:
        print(full_board_check(the_board))
        if full_board_check(the_board):
          display_board(the_board)
          print("Tie Game!")
          game_on =False
        else:
          turn = "Player 1"
  if not replay():
    break
  









#--------------Các function riêng lẻ để test logic từng function ở trên
# place_marker(test_board , "K", 2)
# display_board(test_board) 
# print(win_check(test_board,"O"))
# clear_input()
# print( choose_first())
# print(space_check(test_board, 8))
# print(full_board_check(test_board))
#print(player_choice(test_board))
