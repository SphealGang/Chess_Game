import pygame
from piece_functionality import pawn_AI

pygame.init()
pygame.font.init()

class Square():
    def create_square(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.square = pygame.Rect(self.pos.x * square_size, self.pos.y * square_size, square_size, square_size)
        color = 'white' if (self.pos.x + self.pos.y) % 2 == 0 else "black"
        pygame.draw.rect(screen, color, self.square)

def create_board(square_init):
    for x in range(1,9):
        for y in range(1,9):
            square_init.create_square(x,y)


class Pieces():
    def __init__(self):
        self.pieces = []
        self.turn = 0

    def create_pieces(self,pieces):
        for key,value in pieces.items():
            piece_pos = value
            piece_name = key
            piece_rect = pygame.Rect(piece_pos.x * 100 + 20, piece_pos.y * 100 + 20, 60, 60)   
            self.pieces.append((piece_name,piece_pos,piece_rect))

    def draw_pieces(self):
        for name,vector,rect in self.pieces:
            color = 'yellow' if name[0] == 'w' else 'red'
            pygame.draw.rect(screen, color, rect)
            name = font.render(name, True, 'black')
            name_rect = name.get_rect(center=rect.center)
            screen.blit(name, name_rect)

    def update_piece(self,rect,vector):
        rect.x = vector.x * square_size + 20
        rect.y = vector.y * square_size + 20

    def move_piece(self):
        mouse_pos = pygame.mouse.get_pos()
        for name, vector, rect in self.pieces:
            if self.turn == 0:
                if rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0] == 1:
                        vector.y -= 1
                        self.update_piece(rect,vector)



screen = pygame.display.set_mode((1500,1000))
clock = pygame.time.Clock()
board_square = pygame.math.Vector2(1,1)
square_size = 100
font = pygame.font.Font(None, 20)


square_init = Square()
pieces_init = Pieces()
create_board(square_init)

white_pieces = {'w_pawn1': pygame.Vector2(1, 7)}

pieces_init.create_pieces(white_pieces)
print(pieces_init.pieces)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pieces_init.move_piece()

    screen.fill('green')
    create_board(square_init)
    pieces_init.draw_pieces()


    pygame.display.update()
    clock.tick(60)