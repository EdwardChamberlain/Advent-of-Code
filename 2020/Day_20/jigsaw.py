class tile:
    pass

def render_pos(pos):
    if pos:
        return '■'
    else:
        return '□'

def render_frame(frame, frame_id='Frame'):
    print(f"\n{frame_id:-^19} ")
    for r in frame:
        print(' '.join([render_pos(p) for p in r]))
    print()

def get_borders(frame):
    '''
    Gets the border of the frame in the order:
    Top, bottom, left, right
    '''
    bor_1 = frame[0]
    bor_2 = frame[-1]
    bor_3 = [i[0] for i in frame]
    bor_4 = [i[-1] for i in frame]
    return (bor_1, bor_2, bor_3, bor_4)

def match_border(border_a, border_b):
    flipped_a = border_a.copy()
    flipped_a.reverse()
    return border_a == border_b or flipped_a == border_b

def number_of_matches(a, all_borders):
    return sum([match_border(a, b) for b in all_borders]) -1

def de_border(frame):
    return [i[1:-1] for i in frame[1:-1]]

def flipx(frame):
    return list(reversed(frame))

def flipy(frame):
    return [list(reversed(i)) for i in frame]

def get_vector_connected(edge, frame):
    for i, b in enumerate(get_borders(frame)):
        if match_border(edge, b):
            return i
    return None