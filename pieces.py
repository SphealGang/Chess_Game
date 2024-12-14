import pygame
from piece_functionality import *

w_pawn = pygame.image.load('pieces/w_pawn.png')
w_rook = pygame.image.load('pieces/w_rook.png')
w_horse = pygame.image.load('pieces/w_horse.png')
w_bishop = pygame.image.load('pieces/w_bishop.png')
w_queen = pygame.image.load('pieces/w_queen.png')
w_king = pygame.image.load('pieces/w_king.png')


b_pawn = pygame.image.load('pieces/b_pawn.png')
b_rook = pygame.image.load('pieces/b_rook.png')
b_horse = pygame.image.load('pieces/b_horse.png')
b_bishop = pygame.image.load('pieces/b_bishop.png')
b_queen = pygame.image.load('pieces/b_queen.png')
b_king = pygame.image.load('pieces/b_king.png')

pieces = [
    {'name': 'b_pawn1', 'position': pygame.Vector2(1, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn2', 'position': pygame.Vector2(2, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn3', 'position': pygame.Vector2(3, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn4', 'position': pygame.Vector2(4, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn5', 'position': pygame.Vector2(5, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn6', 'position': pygame.Vector2(6, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn7', 'position': pygame.Vector2(7, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_pawn8', 'position': pygame.Vector2(8, 2), 'color': 'red', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': b_pawn},
    {'name': 'b_rook1', 'position': pygame.Vector2(1, 1), 'color': 'red', 'possible_moves': [], 'first_move': True, 'image': b_rook},
    {'name': 'b_horse1', 'position': pygame.Vector2(2, 1), 'color': 'red', 'possible_moves': [], 'image': b_horse},
    {'name': 'b_bishop1', 'position': pygame.Vector2(3, 1), 'color': 'red', 'possible_moves': [], 'image': b_bishop},
    {'name': 'b_queen', 'position': pygame.Vector2(4, 1), 'color': 'red', 'possible_moves': [], 'image': b_queen},
    {'name': 'b_king', 'position': pygame.Vector2(5, 1), 'color': 'red', 'possible_moves': [], 'first_move': True, 'check': False, 'image': b_king},
    {'name': 'b_bishop2', 'position': pygame.Vector2(6, 1), 'color': 'red', 'possible_moves': [], 'image': b_bishop},
    {'name': 'b_horse2', 'position': pygame.Vector2(7, 1), 'color': 'red', 'possible_moves': [], 'image': b_horse},
    {'name': 'b_rook2', 'position': pygame.Vector2(8, 1), 'color': 'red', 'possible_moves': [], 'first_move': True, 'image': b_rook},

    {'name': 'w_pawn1', 'position': pygame.Vector2(1, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn2', 'position': pygame.Vector2(2, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn3', 'position': pygame.Vector2(3, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn4', 'position': pygame.Vector2(4, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn5', 'position': pygame.Vector2(5, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn6', 'position': pygame.Vector2(6, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn7', 'position': pygame.Vector2(7, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_pawn8', 'position': pygame.Vector2(8, 7), 'color': 'yellow', 'possible_moves': [], 'en_passant': None, 'first_move_2_squares': False, 'image': w_pawn},
    {'name': 'w_rook1', 'position': pygame.Vector2(1, 8), 'color': 'yellow', 'possible_moves': [], 'first_move': True, 'image': w_rook},
    {'name': 'w_horse1', 'position': pygame.Vector2(2, 8), 'color': 'yellow', 'possible_moves': [], 'image': w_horse},
    {'name': 'w_bishop1', 'position': pygame.Vector2(3, 8), 'color': 'yellow', 'possible_moves': [], 'image': w_bishop},
    {'name': 'w_queen', 'position': pygame.Vector2(4, 8), 'color': 'yellow', 'possible_moves': [], 'image': w_queen},
    {'name': 'w_king', 'position': pygame.Vector2(5, 8), 'color': 'yellow', 'possible_moves': [], 'first_move': True, 'check': False, 'image': w_king},
    {'name': 'w_bishop2', 'position': pygame.Vector2(6, 8), 'color': 'yellow', 'possible_moves': [], 'image': w_bishop},
    {'name': 'w_horse2', 'position': pygame.Vector2(7, 8), 'color': 'yellow', 'possible_moves': [], 'image': w_horse},
    {'name': 'w_rook2', 'position': pygame.Vector2(8, 8), 'color': 'yellow', 'possible_moves': [], 'first_move': True, 'image': w_rook}
]
