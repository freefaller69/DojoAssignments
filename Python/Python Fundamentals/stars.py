x = [4, 6, "zipper", "egg", 5, 7, 25]

def draw_stars():
    for idx in x:
        if isinstance(idx, str):
            print idx[0] * len(idx)
            print "\n"
        else:
            print "*" * idx,
            print "\n"
draw_stars()
