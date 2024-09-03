x = ['w_pawn1','w_rook2','w_queen']


white_pieces = [
    {'name':'w_pawn1',
     },

     {'name':'w_pawn2',
      },

      {'name':'w_pawn3',
      }
    ]

for piece in x:
    for y in white_pieces:
        if piece == y['name']:
            x.remove(piece)

print(x)