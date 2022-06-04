import modules.checkers
from modules.checkers import rtx3090ti
from modules.checkers import rtx3090
from modules.checkers import rtx3080ti
from modules.checkers import rtx3080
from modules.checkers import rtx3070ti
from modules.checkers import rtx3070
from modules.checkers import rtx3060ti
from modules.checkers import rtx3060


def main(num):
    if num == 1:
        rtx3090ti.main()
    elif num == 2:
        rtx3090.main()
    elif num == 3:
        rtx3080ti.main()
    elif num == 4:
        rtx3080.main()
    elif num == 5:
        rtx3070ti.main()
    elif num == 6:
        rtx3070.main()
    elif num == 7:
        rtx3060ti.main()
    elif num == 8:
        rtx3060.main()
    else:
        print("Invalid number")