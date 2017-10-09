class Piece:
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self, startpos, endpos, Color, gameboard):
        if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def availableMoves(self, x, y, gameboard):
        print("ERROR: no movement for base class")

    def AdNauseum(self, x, y, gameboard, Color, intervals):
        """repeats the given interval until another piece is run into. 
        if that piece is not of the same color, that square is added and
         then the list is returned"""
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.isInBounds(xtemp, ytemp):
                # print(str((xtemp,ytemp))+"is in bounds")

                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def isInBounds(self, x, y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def noConflict(self, gameboard, initialColor, x, y):
        "checks if a single position poses no conflict to the rules of chess"
        if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor): return True
        return False

class Knight(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in knightList(x, y, 2, 1) if self.noConflict(gameboard, Color, xx, yy)]

class Rook(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)

class Bishop(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)

class Queen(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals + chessDiagonals)

class King(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in kingList(x, y) if self.noConflict(gameboard, Color, xx, yy)]

class Pawn(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.Color = color
        # of course, the smallest piece is the hardest to code. direction should be either 1 or -1, should be -1 if the pawn is traveling "backwards"
        self.direction = direction

    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        answers = []
        if (x + 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x + 1,
                                                                        y + self.direction): answers.append(
            (x + 1, y + self.direction))
        if (x - 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x - 1,
                                                                        y + self.direction): answers.append(
            (x - 1, y + self.direction))
        if (x, y + self.direction) not in gameboard and Color == self.Color: answers.append((x,
                                                                                             y + self.direction))  # the condition after the and is to make sure the non-capturing movement (the only fucking one in the game) is not used in the calculation of checkmate
        return answers