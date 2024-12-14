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
            piece_rect = pygame.Rect(piece_pos.x * square_size + padding, piece_pos.y * square_size + padding, 80, 80)
            x.update({'rect': piece_rect})

    def create_possible_moves(self):
        for x in self.pieces:
            first_move = x.get('first_move', False)
            x.update({'possible_moves': available_moves(x['name'],x['position'],self.pieces,first_move,turn_manager)})
            x.update({'possible_move_square':available_moves_rect(x['possible_moves'])})

    def draw_pieces(self):
        for x in self.pieces:
            color = x['color']
            rect = x['rect']
            image = x['image']
            first_move = x.get('first_move', False)
            pygame.draw.rect(screen, color, rect)
            image_rect = image.get_rect(topleft=rect.topleft)
            screen.blit(image,image_rect)
            available_moves(x['name'],x['position'],self.pieces,first_move,turn_manager)

def select_piece():
    global turn_manager
    global selected_piece
    black_king = next(x for x in pieces_init.pieces if x['name'] == 'b_king')
    white_king = next(x for x in pieces_init.pieces if x['name'] == 'w_king')
    defender = defenders(pieces_init.pieces,turn_manager) 
    defender = defender if defender != None else []

    mouse_pos = pygame.mouse.get_pos()
    if turn_manager == 1:
        for x in pieces_init.pieces:
            if x['rect'].collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    if x['name'][0] == 'w' and white_king['check'] == False or x['name'] == 'w_king' or white_king['check'] == True and x in defender:    
                        if len(x['possible_moves']) > 0:
                            display_possible_moves(x,screen)
                            turn_manager = 3
                            selected_piece = x
                            break
                        else:
                            turn_manager = 1

    elif turn_manager == 2:
        for x in pieces_init.pieces:
            if x['rect'].collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    if x['name'][0] == 'b' and black_king['check'] == False or x['name'] == 'b_king' or black_king['check'] == True and x in defender:    
                        if len(x['possible_moves']) > 0:
                            display_possible_moves(x,screen)
                            turn_manager = 4
                            selected_piece = x
                            break
                        else:
                            turn_manager = 2

    elif turn_manager == 3 or turn_manager == 4:
            for y in selected_piece['possible_move_square']:
                if y.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0] == 1:
                        is_check(turn_manager,pieces_init.pieces)

                        team = 'w' if turn_manager == 3 else 'b'
                        king = next((x for x in pieces_init.pieces if team + '_king' in x['name']))
                        enemy_king = next((x for x in pieces_init.pieces if '_king' in x['name'] and x['name'][0] != team))


                        if 'king' in selected_piece['name']:
                            if selected_piece['first_move'] == True:
                                selected_square = pygame.Vector2(y.x/100,y.y/100)
                                castle_squares = [pygame.Vector2(3,y.y/100),pygame.Vector2(7,y.y/100)]
                                if selected_square in castle_squares:
                                    if selected_square == castle_squares[0]:
                                        rook1= next((x for x in pieces_init.pieces if 'rook1' in x['name'] and selected_piece['name'][0] == x['name'][0]), None)
                                        rook1_end_pos = pygame.Rect(y.x + 100,y.y,100,100)

                                        castle_movement(selected_piece,rook = rook1 ,new_king_position=castle_squares[0],new_rook_position=pygame.Vector2(1,0),piece_dict=pieces_init.pieces,func=smooth_movement(rook1['rect'],rook1_end_pos,rook1))
                                    elif selected_square == castle_squares[1]:
                                        rook2= next((x for x in pieces_init.pieces if 'rook2' in x['name'] and selected_piece['name'][0] == x['name'][0]), None)
                                        rook2_end_pos = pygame.Rect(y.x - 100,y.y,100,100)
                                        
                                        castle_movement(selected_piece,rook = rook2,new_king_position=castle_squares[1],new_rook_position=pygame.Vector2(-1,0),piece_dict=pieces_init.pieces,func=smooth_movement(rook2['rect'],rook2_end_pos,rook2))

                        previous_position = selected_piece['position']
                        new_position = pygame.Vector2(y.x/100,y.y/100)

                        selected_piece.update({'position':new_position})

                        taken_piece = [x for x in pieces_init.pieces if selected_piece['position'] == x['position'] and x['name'] != selected_piece]
                        taken_piece_copy = taken_piece

                        missed_en_passant(selected_piece,pieces_init.pieces)

                        check_for_en_passant(selected_piece,pieces_init.pieces)

                        pieces_init.create_possible_moves()
                        
                        for taken_piece in pieces_init.pieces:
                            if taken_piece['position'] == selected_piece['position'] and taken_piece['name'] != selected_piece['name']:
                                pieces_init.pieces.remove(taken_piece)
                            else:
                                pass

                        delete_ep_pawn(selected_piece,pieces_init.pieces)

                        change_first_move(selected_piece)

                        change_first_move_2_squares(selected_piece,previous_position,new_position)

                        is_check(turn_manager,pieces_init.pieces)

                        if king['check'] == True:
                            selected_piece.update({'position':previous_position})
                            pieces_init.pieces += taken_piece_copy
                            main_game()
                            if turn_manager == 4:
                                turn_manager = 2
                            else:
                                turn_manager = 1
                            break
                        
                        if turn_manager == 3:
                            turn_manager = 2
                        else:
                            turn_manager = 1

                        smooth_movement(selected_piece['rect'],y,selected_piece)

                        main_game()

                        if any(enemy_king['position'] in x['possible_moves'] for x in pieces_init.pieces if x['name'][0] != enemy_king['name'][0]):
                            enemy_king.update({'check':True}) 

                        pieces_init.create_possible_moves()

                        if 'pawn' in selected_piece['name']:
                            opposite_side = 1 if team == 'w' else 8
                            if selected_piece['position'].y == opposite_side:
                                turn_manager = 5 if opposite_side == 1 else 6
                                screen.blit(torn_page,(450,-50))

                        break

    elif turn_manager == 5 or turn_manager == 6:
        buttons = [{'rect': pygame.Rect(535, 25, 75, 260), 'value': 'queen1', 'new_image_w' : w_queen, 'new_image_b' : b_queen},
                   {'rect': pygame.Rect(770, 150, 75, 150), 'value': 'rook1', 'new_image_w' : w_rook, 'new_image_b' : b_rook},
                   {'rect': pygame.Rect(875, 100, 70, 200), 'value': 'bishop1', 'new_image_w' : w_bishop, 'new_image_b' : b_bishop},
                   {'rect': pygame.Rect(630, 110, 100, 175), 'value': 'horse1', 'new_image_w' : w_horse, 'new_image_b' : b_horse}]
        changed = False
        team = selected_piece['name'][0]
        
        button_surface = pygame.Surface((500,380),pygame.SRCALPHA)
        button_surface.fill((255, 0, 0, 0))
        screen.blit(torn_page,(450,-50))
        screen.blit(button_surface,(480,-50))

        for button in buttons:
            pygame.draw.rect(button_surface,'yellow',button['rect'])

        for x in buttons:
            if x['rect'].collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    new_name = selected_piece['name'].replace('pawn',x['value'])
                    new_image = x['new_image_'+ team]
                    selected_piece.update({'name':new_name})
                    selected_piece.update({'image':new_image})
                    changed = True

        if changed: 
            turn_manager = 2 if turn_manager == 5 else 1

        main_game()

        is_check(turn_manager,pieces_init.pieces)
        pieces_init.create_possible_moves()
        

        
def checkmate(piece_dict,turn_manager):
    turn = {
        1 : 'w',
        2 : 'b',
        3 : 'w',
        4 : 'b',
        5 : 'w',
        6 : 'b'
    }
    team = turn[turn_manager]
    king = next(x for x in piece_dict if team + '_king' in x['name'])
    attackers = get_attackers(piece_dict,king)
    defender_list = defenders(piece_dict,turn_manager)
    black_win = pygame.image.load('black_wins.png')
    white_win = pygame.image.load('white_wins.png')

    if attackers != []:
        if king['possible_moves'] == [] and defender_list == []:
            winner_screen = white_win if king['name'][0] == 'b' else black_win
            
            global game_over
            game_over = True

            screen.blit(winner_screen,(450,250))
            # pygame.display.flip()

def smooth_movement(start_pos,end_pos,piece,step=30):
    start_x = start_pos.x
    start_y = start_pos.y 

    end_x = end_pos.x + 10
    end_y = end_pos.y + 10

    difference_x = (end_x - start_x) / step
    difference_y = (end_y - start_y) / step

    for i in range(step + 1):
        start_x += difference_x
        start_y += difference_y

        current_x = int(start_x)
        current_y = int(start_y)
        
        piece.update({'rect': pygame.Rect(current_x, current_y, 80, 80)})
        screen.blit(board,(100,100))
        pieces_init.draw_pieces()
        pygame.display.flip()
    
    piece_move_sfx.play()

def main_game():
    screen.blit(table,(0,0))
    pieces_init.create_pieces()
    pieces_init.draw_pieces()
    pieces_init.create_possible_moves()

turn_manager = 1
game_over = False
screen = pygame.display.set_mode((1500,1000))
clock = pygame.time.Clock()
square_size = 100
padding = 10
font = pygame.font.Font(None, 20)
piece_move_sfx = pygame.mixer.Sound('chess_piece_moved.wav')
board_init = BoardManager()
pieces_init = PieceManager(pieces)
table = pygame.image.load('table.png')
board = pygame.image.load('chess_board.png')
torn_page = pygame.image.load('torn_page.png')


main_game()

while True:
    checkmate(pieces_init.pieces,turn_manager)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            select_piece()

    if turn_manager not in [5,6] and game_over == False:
        pieces_init.draw_pieces()


    pygame.display.update()
    clock.tick(60)
