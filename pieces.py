import pygame
from piece_functionality import *

pieces = [
    {'name':'w_pawn1',
     'position':pygame.Vector2(1, 7),
     'color':'yellow',
      'possible_moves':[]
     },

     {'name':'w_pawn2',
      'position': pygame.Vector2(2, 4),
      'color':'yellow',
      'possible_moves':[]
      },

      {'name':'w_pawn3',
      'position': pygame.Vector2(1, 4),
      'color':'yellow',
      'possible_moves':[]
      },
      {'name':'w_rook2',
      'position': pygame.Vector2(8, 8),
      'color':'yellow',
      'possible_moves':[]
      },
      {'name':'b_pawn1',
     'position':pygame.Vector2(1, 2),
     'color':'red',
      'possible_moves':[]
     },

     {'name':'b_pawn2',
      'position': pygame.Vector2(2, 3),
      'color':'red',
      'possible_moves':[]
      },

      {'name':'b_pawn3',
      'position': pygame.Vector2(6, 2),
      'color':'red',
      'possible_moves':[]
      }
    ]
