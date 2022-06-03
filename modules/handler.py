import modules.checkers
from modules.checkers import rtx3060ti, rtx3090ti

def main(num):
    if num == 1:
        rtx3060ti.main()
    elif num == 2:
        rtx3090ti.main()
    else:
        print("Invalid number")