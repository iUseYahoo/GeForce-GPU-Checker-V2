import os
from columnar import columnar
from modules import handler as handler

class tools:
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def printTable(data, header):
        table = columnar(data, header, no_borders=True)
        print(table + '\n')

    def printCheckingTitle(gpuname):
        print(f"==== {gpuname} Checker ====")

    def showGpuPrice(price):
        print(f"{tools.bcolors.WARNING}{price}{tools.bcolors.ENDC}")

    def nogpustock(gpuname):
        print(f"{tools.bcolors.BOLD}{tools.bcolors.FAIL}{gpuname.upper()} IS OUT OF STOCK{tools.bcolors.ENDC}")

    def hasgpustock(gpuname):
        print(f"{tools.bcolors.BOLD}{tools.bcolors.OKGREEN}{gpuname.upper()} IS IN STOCK{tools.bcolors.ENDC}")

def main():
    tools.clear()

    # Get the list of all the available tools
    headername = ["Number", "GPU (Sorts by recently added last)"]
    gpunames = [
        ["1", "Nvidia GeForce RTX 3070 Ti"],
        ["2", "Nvidia GeForce RTX 3090 Ti"],
        ["3", "Nvidia GeForce RTX 3090"],
        ["4", "Nvidia GeForce RTX 3080 Ti"],
        ["5", "Nvidia GeForce RTX 3080"],
        ["6", "Nvidia GeForce RTX 3070 Ti"],
    ]

    # shows the table
    tools.printTable(gpunames, headername)
    getnum = int(input("Enter the number of the GPU you want to check: "))
    handler.main(getnum)


if __name__ == '__main__':
    main()
