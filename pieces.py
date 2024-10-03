import pygame
from piece_functionality import *

pieces = [
     {'name':'b_pawn7',
     'position':pygame.Vector2(7, 2),
     'color':'red',
      'possible_moves':[],
      'en_passant' : None,
      'first_move_2_squares': False
     },
    #  {'name':'b_pawn5',
    #  'position':pygame.Vector2(5, 2),
    #  'color':'red',
    #   'possible_moves':[],
    #   'en_passant' : None,
    #   'first_move_2_squares': False
    #  },
     {'name':'b_bishop1',
      'position': pygame.Vector2(2, 1),
      'color':'red',
      'possible_moves':[]
      },
      {'name':'b_rook2',
      'position': pygame.Vector2(5, 1),
      'color':'red',
      'possible_moves':[],
      'first_move' : True
      },
      
      # {'name':'w_bishop2',
      # 'position': pygame.Vector2(6, 8),
      # 'color':'yellow',
      # 'possible_moves':[]
      # },
      {'name':'w_pawn1',
      'position':pygame.Vector2(1, 7),
      'color':'yellow',
      'possible_moves':[],
      'en_passant' : None,
      'first_move_2_squares': False
     },
     {'name':'w_pawn2',
      'position':pygame.Vector2(4, 7),
      'color':'yellow',
      'possible_moves':[],
      'en_passant' : None,
      'first_move_2_squares': False
     },
    {'name':'w_rook1',
      'position': pygame.Vector2(1, 8),
      'color':'yellow',
      'possible_moves':[],
      'first_move' : True
      },
    {'name':'w_rook2',
      'position': pygame.Vector2(8, 8),
      'color':'yellow',
      'possible_moves':[],
      'first_move' : True
      },
      {'name':'b_king',
      'position':pygame.Vector2(8, 1),
      'color':'red',
      'possible_moves':[],
      'first_move' : True,
      'check' : False
     },
    {'name':'w_king',
      'position':pygame.Vector2(5, 8),
      'color':'yellow',
      'possible_moves':[],
      'first_move' : True,
      'check' : False
     }
     ]
