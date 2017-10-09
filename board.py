class Board:

    def __init__(self,shape=[8,8]):
        self.board = self.create_board()

    def create_board(self,shape):
        board_x=[]

        for x in range(shape[0]):
            board_y =[]
            for y in range(shape[1]):

                board_y.append('.')

            board_x.append(board_y)

        return board_x