
import pygame
from pieces import *

square_size = 100

def update_piece(rect,vector):
    rect.x = vector.x * square_size + 20
    rect.y = vector.y * square_size + 20

def available_moves(piece_name,current_position,piece_dict,first_move,turn_manager):
    legal_squares = []
    directions = []
    line = False
    turn = {
        1 : 'b',
        2 : 'w',
        3 : 'b',
        4 : 'w',
        5 : 'b',
        6 : 'w'
    }

    current_turn = turn[turn_manager]

    if 'pawn' in piece_name:
        direction = -pygame.Vector2(0,1) if piece_name[0] == 'w' else pygame.Vector2(0,1)
        team = piece_name[0]
        starting_pos = 7 if piece_name[0] == 'w' else 2
        behind = 1 if team == 'b' else -1
        en_passant_pawn =  next((x for x in piece_dict if 'pawn' in x['name'] and x['name'][0] != team and x['en_passant'] == True), None) 

        if current_turn !=team:
            if current_position.y == starting_pos:
                legal_squares.append(current_position + direction)
                legal_squares.append(current_position + 2 * direction)
            elif current_position.y == 8 and starting_pos == 2:
                legal_squares = []      
            elif current_position.y == 1 and starting_pos == 8:
                legal_squares = []
            else:
                legal_squares.append(current_position + direction)

        if en_passant_pawn != None:
            epp_positions = [pygame.Vector2(en_passant_pawn['position'].x + 1, en_passant_pawn['position'].y),pygame.Vector2(en_passant_pawn['position'].x - 1, en_passant_pawn['position'].y)]
            for x in epp_positions:
                if current_position == x:
                    legal_squares.append(en_passant_pawn['position'] + pygame.Vector2(0,behind))

        for y in legal_squares:
            for piece in piece_dict:
                if y == piece['position']:
                    if legal_squares == [] or y == legal_squares[0]:
                        legal_squares = []
                    else:
                        legal_squares.pop()
        
        for diagonal in [-1,1]:
            for x in piece_dict:
                if (current_position + direction + pygame.Vector2(diagonal,0)) == x['position'] and x['name'][0] != team:
                    legal_squares.append(current_position + direction + pygame.Vector2(diagonal,0))
                elif current_turn == team:
                    legal_squares.append(current_position + direction + pygame.Vector2(diagonal,0))
                 
    elif 'rook' in piece_name:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        line = True

    elif 'bishop' in piece_name:
        directions = [(+1,-1),(+1,+1),(-1,+1),(-1,-1)]
        line = True

    elif 'queen' in piece_name:
        directions = [(+1,-1),(+1,+1),(-1,+1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
        line = True

    elif 'horse' in piece_name:
        directions = [(+1,+2),(-1,+2),(+2,+1),(+2,-1),(-2,+1),(-2,-1),(+1,-2),(-1,-2)]
        horse_color = piece_name[0]

        for dx,dy in directions:
            square = pygame.Vector2(current_position.x + dx,current_position.y + dy)
            occupied = False

            if horse_color == current_turn:
                legal_squares.append(square)
            
            for x in piece_dict:
                if horse_color != current_turn and square == x['position']:
                    occupied = True
                    if x['name'][0] != horse_color:
                        legal_squares.append(square)   

            if occupied:
                pass
            
            else:
                legal_squares.append(square)

    elif 'king' in piece_name:
        directions = [(0,+1),(-1,+1),(+1,+1),(+1,0),(-1,0),(0,-1),(+1,-1),(-1,-1)]
        illegal_squares = []
        team = piece_name[0]
        rook_name = team + '_rook'


        for dx,dy in directions:
            square = pygame.Vector2(current_position.x + dx,current_position.y + dy)
            occupied = False

            for x in piece_dict:
                if x['name'][0] != team:
                    for y in x['possible_moves']:
                        if y == square:
                            illegal_squares.append(y)
                
                elif square == x['position']:
                    occupied = True
                    if x['name'][0] != team:
                        legal_squares.append(square)

                elif 'pawn' in x['name']:
                    for z in x['possible_moves']:
                        if x['position'].x != z.x:
                            illegal_squares.append(x)

                elif square.x >= 9 or square.x < 1 or square.y >= 9 or square.y < 1:
                    illegal_squares.append(square)

            if occupied:
                pass
            
            else:
                legal_squares.append(square)

        if first_move == True:
            for x in piece_dict:
                rook_x = x['position'].x

                if rook_name in x['name'] and len(x['name']) == 7 and x['first_move'] == True :
                        if x['name'][-1] == '1':
                            for i in range(int(rook_x + 1), int(current_position.x)):
                                castle_square = (pygame.Vector2(i,current_position.y))
                                if any(x['position'] == castle_square for x in piece_dict):
                                    break
                                else:
                                    legal_squares.append(pygame.Vector2(3,current_position.y))
                        elif x['name'][-1] == '2':
                            for i in range(int(current_position.x)+1,int(rook_x)):
                                castle_square = (pygame.Vector2(i,current_position.y))
                                if any(x['position'] == castle_square for x in piece_dict):
                                    break
                                else:
                                    legal_squares.append(pygame.Vector2(7,current_position.y))

        legal_squares = [x for x in legal_squares if x not in illegal_squares]


    if line:        
        for x in piece_dict:
            
            for dx,dy in directions:
                for y in range(1,8):
                    square = pygame.Vector2(current_position.x + y * dx,current_position.y + y * dy)
                    
                    if square.x > 8 or square.y < 1 or square.x < 1 or square.y > 8:
                        break

                    occupied = False

                    for x in piece_dict:
                        team = piece_name[0]
                        if square == x['position']:
                            if current_turn == x['name'][0]:
                                legal_squares.append(square)
                                occupied= True
                            
                            elif x['name'][0] != team:
                                if 'king' in x['name']: 
                                    legal_squares.append(square)
                                else:
                                    legal_squares.append(square)
                                    occupied= True

                            else:
                                occupied=True
                            
                            if occupied:
                                break   

                    if occupied:
                        break

                    legal_squares.append(square)  
            
    for x in legal_squares[:]:
        if x.x >= 9 or x.x <= 0 or x.y >= 9 or x.y <= 0:
            legal_squares.remove(x)

    if current_position in legal_squares:
        legal_squares.remove(current_position)

    legal_squares = [pygame.math.Vector2(v) for v in set(map(tuple, legal_squares))]

    return legal_squares

def castle_movement(king,rook,new_king_position,new_rook_position,piece_dict,func):
    if rook in piece_dict:
        king.update({'position':new_king_position})
        rook.update({'position':new_king_position + new_rook_position})
        func

def available_moves_rect(x):
    square_list = []

    for y in x:
        highlighed_square = pygame.Rect(y.x * square_size, y.y * square_size,square_size,square_size)
        square_list.append(highlighed_square)

    return square_list

def display_possible_moves(x,screen):
    for square in x['possible_move_square']:
        color = 'orange' if (square.x / 100 + square.y / 100) % 2 == 0 else "red"
        pygame.draw.rect(screen, color, square)    

def change_first_move(selected_piece):
    if 'first_move' in selected_piece.keys():
        selected_piece.update({'first_move':False})

def change_first_move_2_squares(selected_piece,initial_position,new_position):
    team = selected_piece['name'][0]
    advance = -2 if team == 'b' else 2
    if initial_position.y - new_position.y == advance:
        if "first_move_2_squares" in selected_piece.keys():
            selected_piece.update({"first_move_2_squares":True})

def check_for_en_passant(selected_piece,piece_dict):
    team = selected_piece['name'][0]
    enemy_team = 'w' if team == 'b' else 'b'
    behind = -1 if team == 'w' else 1

    adjancent_squares = [pygame.Vector2(selected_piece['position'].x + 1, selected_piece['position'].y),pygame.Vector2(selected_piece['position'].x - 1, selected_piece['position'].y)]
    enemy_pawns = [x for x in piece_dict if enemy_team + '_pawn' in x['name'] and x['first_move_2_squares'] == True and x['position'] in adjancent_squares and x['en_passant'] == None]

    for x in enemy_pawns:
        if not any(x['position'] - pygame.Vector2(0,behind) == y['position'] for y in piece_dict):
            selected_piece.update({'en_passant':True})

def missed_en_passant(selected_piece,piece_dict):
    epp = next((x for x in piece_dict if 'pawn' in x['name'] and x['en_passant'] == True),None)

    if epp != None:
        if selected_piece['name'][0] == epp['name'][0]:
            epp.update({'en_passant':False})


def delete_ep_pawn(selected_piece,piece_dict):
    en_passant_pawn = next((x for x in piece_dict if 'pawn' in x['name'] and x['en_passant'] == True),None)
    team = selected_piece['name'][0]
    direction = 1 if team == 'b' else -1

    if en_passant_pawn != None:
        if selected_piece['position'] == en_passant_pawn['position'] + pygame.Vector2(0,direction):
            piece_dict.remove(en_passant_pawn)


def self_check(piece_dict,selected_piece,taken_piece):    
    team = selected_piece['name'][0]
    king = next((x for x in piece_dict if x['name'] == team + '_king'))
    king_position = king['position']
    attacker = next((x for x in taken_piece),None)
    
    for x in piece_dict:
        if attacker != None:
            if king_position in x['possible_moves'] and x['name'] != team:
                if x == attacker:
                    return False
                else:
                    return True

    return False

def is_check(turn_manager,piece_dict):
    turn = {
        1 : 'w',
        2 : 'b',
        3 : 'w',
        4 : 'b'
    }
    color = turn[turn_manager]

    team = [x for x in piece_dict if x['name'][0] != color]
    king = next((x for x in piece_dict if '_king' in x['name'] and x['name'][0] == color ))

    for x in team:
        for y in x['possible_moves']:
            if king['position'] == y:
                king.update({'check':True})
                return
            
    king.update({'check':False})

def get_attackers(piece_dict,king):
    attacker = []

    for x in piece_dict:
        if king['position'] in x['possible_moves']:
            attacker.append(x)

    return attacker

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
    can_be_defended = True
    king = next(x for x in piece_dict if team + '_king' in x['name'])
    king_team = [x for x in piece_dict if team in x['name']]
    attackers = get_attackers(piece_dict,king)
    attacker_squares = []

    if attackers != []: 
        if len(attackers) >= 2:
            can_be_defended == False

        for x in attackers:
            attacker_pos = x['position']
    
            attack_dir_x = attacker_pos.x - king['position'].x
            attack_dir_y = attacker_pos.y - king['position'].y

        step_x = 0 if attack_dir_x == 0 else attack_dir_x // abs(attack_dir_x)
        step_y = 0 if attack_dir_y == 0 else attack_dir_y // abs(attack_dir_y)

        
        for n in range (8):
            direction = pygame.Vector2(step_x * n, step_y * n)
            square = king['position'] + direction
            if square == attacker_pos:
                break
            elif square == king['position']:
                pass
            else:
                attacker_squares.append(square)

        # print(attacker_squares)

        can_be_defended = False
        for x in attacker_squares:
            for y in king_team:
                if x in y['possible_moves']:
                    can_be_defended = True
                    break

        # print(can_be_defended)
        
    if attackers != []:
        if king['possible_moves'] == [] and can_be_defended == False:
            print('CHECKMATE')
