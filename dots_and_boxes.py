# dots and boxes

class Player(object):
    
    def __init__(self, position, modifier, name):
        self.pos = position
        self.mod = modifier
        self.name = name

class Board(object):

    swap = False

    def __init__(self, board, p1, p2):
        self.b = board
        self.p1 = p1
        self.p2 = p2
        self.cur_p = self.p1

    def swap_cur_p(self):
        if self.cur_p == self.p1:
            self.cur_p = self.p2
        else:
            self.cur_p = self.p1

    def simulate_play(self, turns):
        i = 0
        while i < turns:
            if self.swap:
                self.swap_cur_p()
            self.cur_p.pos = (self.cur_p.pos + self.cur_p.mod) % 36 # move te player to next position
            print self.cur_p.name
            print self.cur_p.pos
            self.play_next_turn()
            print "".join(self.b[self.cur_p.pos])
            i += 1
        self.print_board()

        ##########self.print_board()

    def play_next_turn(self):
        
        if self.cur_p == self.p1:
            # player one checks above then clockwise
            if self.b[self.cur_p.pos][0] == "0" and self.cur_p.pos > 5:
                #print "making connection above"
                # we can connect to the square above
                self.b[self.cur_p.pos][0] = "1"
                self.b[self.cur_p.pos - 6][2] = "1"
                
                
            elif self.b[self.cur_p.pos][1] == "0" and self.cur_p.pos % 6 < 5:
                #print "making connection to right"
                self.b[self.cur_p.pos][1] = "1"
                self.b[(self.cur_p.pos + 1)][3] = "1"
                

            elif self.b[self.cur_p.pos][2] == "0" and self.cur_p.pos < 30:
                #print "making connection below"
                self.b[self.cur_p.pos][2] = "1"
                self.b[self.cur_p.pos + 6][0] = "1"
                

            elif self.b[self.cur_p.pos][3] == "0" and self.cur_p.pos % 6 > 1:
                #print "making connection to left"
                self.b[self.cur_p.pos][3] = "1"
                self.b[self.cur_p.pos - 1][1] = "1"
                
            else:
                # all options are taken, move position by one and try again
                self.cur_p.pos += 1
                self.play_next_turn()
                
        else:
            # player two checks above then anti-clockwise
            if self.b[self.cur_p.pos][0] == "0" and self.cur_p.pos > 5:
                #print "making connection above"
                # we can connect to the square above
                self.b[self.cur_p.pos][0] = "2"
                self.b[self.cur_p.pos - 6][2] = "2"
                

            elif self.b[self.cur_p.pos][3] == "0" and self.cur_p.pos % 6 > 1:
                #print "making connection to left"
                self.b[self.cur_p.pos][3] = "2"
                self.b[self.cur_p.pos - 1][1] = "2"
                
            

            elif self.b[self.cur_p.pos][2] == "0" and self.cur_p.pos < 30:
                #print "making connection below"
                self.b[self.cur_p.pos][2] = "2"
                self.b[self.cur_p.pos + 6][0] = "2"
                
            
            elif self.b[self.cur_p.pos][1] == "0" and self.cur_p.pos % 6 < 5:
                #print "making connection to right"
                self.b[self.cur_p.pos][1] = "2"
                self.b[(self.cur_p.pos + 1)][3] = "2"
                r
            
            else:
                # all options are taken, move position by one and try again
                self.cur_p.pos += 1
                self.play_next_turn()

        ## check if need to swap player!
        self.check_swap()

    def check_swap(self):
        # look at cur_p position and check if it is part of an adjacent square??
        # need to differentiate between a new square and a previously made square

        ## look in my CS book for idea of how to do this
        self.swap = True

    def print_board(self):
        i = 0
        while i < 36:
            if i % 6 == 0:
                print
            print "".join(self.b[i])
            i += 1


def create_board():
    l = []
    
    for i in range(36):
        inner = ["0", "0", "0", "0"]
        l.append(inner)
        inner = []
    return l

def main():
    input_arr = raw_input().split(" ")
    p1 = Player(int(input_arr[0]), int(input_arr[1]), "p1")
    p2 = Player(int(input_arr[2]), int(input_arr[3]), "p2")
    turns = int(input_arr[4])

    board = Board(create_board(), p1, p2)
    # board explanation:
    ##  each square is a 4 digit string
    ##  the first digit represents a connection to the dot above, then in order, right, below, left
    ##  "1" for player one owning the connection
    ##  "2" for player two owning the connection

    board.simulate_play(turns)


main()
