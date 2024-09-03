import pygame
from pieces import *
from piece_functionality import *

pygame.init()
pygame.font.init()

class BoardManager():
    def __init__(self):
        self.square_list = []

    def create_square(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.square = pygame.Rect(self.pos.x * square_size, self.pos.y * square_size, square_size, square_size)
        color = 'white' if (self.pos.x + self.pos.y) % 2 == 0 else "black"
        pygame.draw.rect(screen, color, self.square)
        self.square_list.append(self.square)

    def create_board(self):
        for x in range(1,9):
            for y in range(1,9):
                board_init.create_square(x,y)

class PieceManager():
    def __init__(self,pieces):
        self.pieces = pieces

    def create_pieces(self):
        for x in self.pieces:
            piece_pos = x['position']
            piece_rect = pygame.Rect(piece_pos.x * square_size + padding, piece_pos.y * square_size + padding, 60, 60)

            x.update({'rect': piece_rect})

    def create_possible_moves(self):
        for x in self.pieces:
            x.update({'possible_moves': available_moves(x['position'],self.pieces)})
            x.update({'possible_move_square':available_moves_rect(x['possible_moves'])})

    def draw_pieces(self):
        for x in self.pieces:
            color = x['color']
            rect = x['rect']
            name = x['name']
            position = x['position']
            pygame.draw.rect(screen, color, rect)
            name = font.render(name, True, 'black')
            name_rect = name.get_rect(center=rect.center)
            screen.blit(name, name_rect)
            available_moves(x['position'],self.pieces)

def select_piece():
    global turn_manager
    mouse_pos = pygame.mouse.get_pos()
    if turn_manager == 1:
        for x in pieces_init.pieces:
            if x['rect'].collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print(x['possible_moves'])
                    if len(x['possible_moves']) > 0:
                        display_possible_moves(x,screen)
                        turn_manager = 3
                        global selected_piece
                        selected_piece = x
                        break
                    else:
                        turn_manager = 1

    elif turn_manager == 3:
            for y in selected_piece['possible_move_square']:
                if y.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0] == 1:
                        selected_piece.update({'position':pygame.Vector2(y.x/100,y.y/100)})
                        main_game()
                        turn_manager = 1
                        break

def main_game():
    screen.fill('green')
    pieces_init.create_pieces()
    pieces_init.create_possible_moves()
    board_init.create_board()

turn_manager = 1
screen = pygame.display.set_mode((1500,1000))
clock = pygame.time.Clock()
square_size = 100
padding = 20
font = pygame.font.Font(None, 20)

board_init = BoardManager()
pieces_init = PieceManager(pieces)


main_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            select_piece()

    pieces_init.draw_pieces()

    pygame.display.update()
    clock.tick(60)