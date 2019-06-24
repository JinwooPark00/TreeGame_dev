import sys, pygame
from board import Board

print("hi")

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    players = {}
    board = Board(players)
    x = 0
    y = 0
    once = True

    # pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, 100, 100), 0)
    # for index, tile in enumerate(board.board):
    #     print("drawing board")
    #     # pygame.draw.rect(screen, tile.color, pygame.Rect(x, y, 20, 20), 0)
    #     # if index < 13:
    #     #     x += 20
    #     # elif index < 25:
    #     #     y += 20
    #     # elif index < 37:
    #     #     x -= 20
    #     # else:
    #     #     y -= 20

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if once:
            for index, tile in enumerate(board.board):
                print("drawing board")
                pygame.draw.rect(screen, tile.color, pygame.Rect(x, y, 100, 100), 5)
                if index < 13:
                    x += 20
                elif index < 25:
                    y += 20
                elif index < 37:
                    x -= 20
                else:
                    y -= 20
            once = False

# if __name__ == '__main__':
#     board = Board()
#     for i in board.board:
#         print(i)
#
#     tree = Tree()
#     player = Player(tree, 0)
