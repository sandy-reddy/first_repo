### create a class to define the board

class Board:

    def __init__(self, turn, diffc):
        pass



#   |  |
# --------
#   |  |
# --------
#   |  |
# 


def board(x,y):
    assert x>=1
    assert y>=1
    print("  "* x + "|" + "  "* x + "|")
        # try:
        #     print(" "* (y-1) + | + " "* (y-1) + |)
        # else:
        #     pass
    print("___" * (3*x))
    print("  "* x + "|" + "  "* x + "|")
    print("___" * (3*x))
    print("  "* x + "|" + "  "* x + "|")

board(2,1)
board(1,1)
