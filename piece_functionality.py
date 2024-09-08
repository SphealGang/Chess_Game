import pygame
from pieces import *

square_size = 100

def update_piece(rect,vector):
    rect.x = vector.x * square_size + 20
    rect.y = vector.y * square_size + 20

def available_moves(piece_name,current_position,piece_dict):
    legal_squares = []
 
    if 'pawn' in piece_name:
        direction = -pygame.Vector2(0,1) if piece_name[0] == 'w' else pygame.Vector2(0,1)
        team = piece_name[0]
        starting_pos = 7 if piece_name[0] == 'w' else 2

        if current_position.y == starting_pos:
            legal_squares.append(current_position + direction)
            legal_squares.append(current_position + 2 * direction)
        elif current_position.y == 8 and starting_pos == 2:
            legal_squares = []      
        elif current_position.y == 1 and starting_pos == 8:
            legal_squares = []
        else:
            legal_squares.append(current_position + direction)

        for y in legal_squares:
            for piece in piece_dict:
                if y == piece['position']:
                    if legal_squares == [] or y == legal_squares[0]:
                        legal_squares = []
                    else:
                        legal_squares.pop()

        for diagonal in [-1,1]:
            for square in piece_dict:
                if (current_position + direction + pygame.Vector2(diagonal,0)) == square['position'] and square['name'][0] != team:
                    legal_squares.append(current_position + direction + pygame.Vector2(diagonal,0))

    elif 'rook' in piece_name:

        for x in piece_dict:
            team = piece_name[0]

            for i in range(int(current_position.x-1),-1,-1):
                if any(pygame.Vector2(i,current_position.y) == x['position'] for x in piece_dict):
                    if x['name'][0] != team:
                        legal_squares.append(pygame.Vector2(i,current_position.y))
                        break
                    else:
                        break
                legal_squares.append(pygame.Vector2(i,current_position.y))
            
            for i in range(int(current_position.x)+1,9):
                if any(pygame.Vector2(i,current_position.y) == x['position'] for x in   piece_dict):
                    if x['name'][0] != team:
                        legal_squares.append(pygame.Vector2(i,current_position.y))
                        break
                    else:
                        break
                legal_squares.append(pygame.Vector2(i,current_position.y))
    
            for i in range(int(current_position.y-1),-1,-1):
                if any(pygame.Vector2(current_position.x,i) == x['position'] for x in   piece_dict):
                    if x['name'][0] != team:
                        legal_squares.append(pygame.Vector2(i,current_position.y))
                        break
                    else:
                        break
                legal_squares.append(pygame.Vector2(current_position.x,i))
    
            for i in range(int(current_position.y+1),9):
                if any(pygame.Vector2(current_position.x,i) == x['position'] for x in   piece_dict):
                    if x['name'][0] != team:
                        legal_squares.append(pygame.Vector2(i,current_position.y))
                        break
                    else:
                        break
                legal_squares.append(pygame.Vector2(current_position.x,i))

        for x in legal_squares:
            if x.x > 9 or x.x < 1 or x.y > 9 or x.y < 1:
                legal_squares.remove(x)


    for x in legal_squares:
        if current_position in legal_squares:
            legal_squares.remove(current_position)


    return legal_squares


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
    
