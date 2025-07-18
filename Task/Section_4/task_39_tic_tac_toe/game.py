from player import get_move
from board import draw_board

state = [[" "]*3 for _ in range(3)]
draw_board(state)
move = get_move("Player 1")
print(f"Player 1 chose {move}")
