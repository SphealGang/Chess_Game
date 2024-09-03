import pygame
from pieces import *

square_size = 100

def update_piece(rect,vector):
    rect.x = vector.x * square_size + 20
    rect.y = vector.y * square_size + 20

def available_moves(piece_name,current_position,piece_dict):
    legal_squares = []
 
    if 'w_pawn' in piece_name:
        if current_position.y == 7:
            legal_squares.append(current_position - pygame.Vector2(0,1))
            legal_squares.append(current_position - pygame.Vector2(0,2))      
        else:
            legal_squares.append(current_position - pygame.Vector2(0,1))

        for y in legal_squares:
            for piece in piece_dict:
                if y == piece['position']:
                    legal_squares = []

        for square in piece_dict:
            if (current_position - pygame.Vector2(0,1) + pygame.Vector2(1,0)) == square['position']and square['name'][0] == 'b':
                legal_squares.append(current_position - pygame.Vector2(0,1) + pygame.Vector2(1,0))
            elif (current_position - pygame.Vector2(0,1) - pygame.Vector2(1,0)) == square['position'] and square['name'][0] == 'b':
                legal_squares.append(current_position - pygame.Vector2(0,1) - pygame.Vector2(1,0))
        
    elif 'b_pawn' in piece_name:
        legal_squares.append(black_pawn_func(current_position,piece_dict) )


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
    
def black_pawn_func(current_position,piece_dict):
        square_list = []
        
        if current_position.y == 2:
            square_list.append(current_position + pygame.Vector2(0,1))
            square_list.append(current_position + pygame.Vector2(0,2))      
        else:
            square_list.append(current_position + pygame.Vector2(0,1))

        for y in square_list:
            for piece in piece_dict:
                if y == piece['position']:
                    square_list = []

        for square in piece_dict:
            if (current_position + pygame.Vector2(0,1) + pygame.Vector2(1,0)) == square['position']and square['name'][0] == 'w':
                square_list.append(current_position + pygame.Vector2(0,1) + pygame.Vector2(1,0))
            elif (current_position + pygame.Vector2(0,1) - pygame.Vector2(1,0)) == square['position'] and square['name'][0] == 'w':
                square_list.append(current_position + pygame.Vector2(0,1) - pygame.Vector2(1,0))

        return square_list
