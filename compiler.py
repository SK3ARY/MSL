def run(fileLoc):
    with open(f'{fileLoc}.msl', 'r') as f:
        pointPos = 0

        ps = f.read().split(' ')
        position = 0

        # Tokens
        TOKENS = ["<+>","<+>\n","<->","<->\n","<*>","<*>\n","</>","</>\n","<?>","<?>\n","<!>","<!>\n"] # Up, Down, Doubup, Doubdown, Log, Reset
        UP = [TOKENS[0], TOKENS[1]]
        DOWN = [TOKENS[2], TOKENS[3]]
        DOUBUP = [TOKENS[4], TOKENS[5]]
        DOUBDOWN = [TOKENS[6], TOKENS[7]]
        LOG = [TOKENS[8], TOKENS[9]]
        RESET = [TOKENS[10], TOKENS[11]]

        for i in ps:
            if ps[position] in TOKENS:
                if ps[position] in UP: # Up
                    pointPos += 1
                elif ps[position] in DOWN: # Down
                    pointPos -= 1
                elif ps[position] in DOUBUP: # Doubup
                    pointPos *= 2
                elif ps[position] in DOUBDOWN: # Doubdown
                    pointPos /= 2
                elif ps[position] in LOG: # Log
                    print(pointPos)
                elif ps[position] in RESET: # Reset
                    pointPos = 0
            else:
                print("ERROR: Unknown object inside of file")
                exit()
            position += 1