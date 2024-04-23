from objects import Board

board1 = Board("X,O,X,#,O,X,O,#,X")
board2 = Board("X,X,X,#,O,O,O,#,X")
board3 = Board("#,#,X,#,X,#,X,O,O")
board4 = Board("X,O,#,#,O,#,X,O,X")
board5 = Board("O,O,O,#,X,#,X,#,X")
board6 = Board("O,X,X,#,O,#,X,#,O")
board7 = Board("X,#,X,#,O,#,O,#,X")
board8 = Board("X,O,X,X,O,O,O,X,X")
board9 = Board("X,#,#,O,O,#,X,X,X")
board10 = Board("X,#,#,O,O,#,X,#,0")

testBoards =  [board1, board2, board3, board4, board5, board6, board7, board8, board9, board10]

for board in testBoards:
    print(board)
    results = board.checkWin()
    if results[0] == True:
        print(f"{'X' if results[1] == 1 else 'O'} wins through {results[2]}.\n")
    else:
        print(f"{results[2]}.\n")

