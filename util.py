import pygame


def clamp(val, lower, upper):
    return max(min(val, upper), lower)


def in_bounds(x, y, w, h):
    return 0 <= x < w and 0 <= y < h


def tint(surf, tint_color):
    """ adds tint_color onto surf.
    """
    surf = surf.copy()
    surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    surf.fill(tint_color[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    return surf


def shift(a):
    a.append(a[0])
    del(a[0])

