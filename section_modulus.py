#  (right)  |
#  (mid) ___| <- This is a Z-shaped beam
# (left) |       The following function calculates its section modulus
def Z(left, mid, right, thick):
    # solving the y-centroid integral by taking the origin at the center of the middle beam
    # y0 = integral of y * dA / integral of dA
    y0 = right * (right + thick) / 2 - left * (left + thick) / 2
    y0 /= right + mid + left
    # compute the integral of the second moment of area by each component
    # Ix = integral of (y - y0)^2 * dA
    Ix  = mid * ((thick/2 - y0)**3 - (-thick/2 - y0)**3) / 3  # middle beam
    Ix += thick * ((thick/2 + right - y0)**3 - (thick/2 - y0)**3) / 3  # right beam
    Ix += thick * ((-thick/2 - y0)**3 - (-thick/2 - left - y0)**3) / 3  # left beam
    print(Ix)
    # compute the section modulus
    mod = Ix / max(right + thick/2 - y0, left + thick/2 + y0)
    return mod

#        (top)
#        |‾‾
# (left) |   | (right)
#        |___| <- This is a G-shaped beam
#        (bot)    The following function calculates its section modulus
def G(top, right, bot, left, thick):
    # solving the y-centroid integral by taking the origin at the center of the left beam
    # y0 = integral of y * dA / integral of dA
    y0 = top * (left + thick) / 2 - bot * (left + thick) / 2 - right * (left - right) / 2
    y0 /= top + right + bot + left
    # compute the integral of the second moment of area by each component
    # Ix = integral of (y - y0)^2 * dA
    Ix  = top * ((left/2 + thick - y0)**3 - (left/2 - y0)**3) / 3  # top beam
    Ix += bot * ((-left/2 - y0)**3 - (-left/2 - thick - y0)**3) / 3  # bottom beam
    Ix += thick * ((right - left/2 - y0)**3 - (-left/2 - y0)**3) / 3  # right beam
    Ix += thick * ((left/2 - y0)**3 - (-left/2 - y0)**3) / 3  # left beam
    # compute the section modulus
    mod = Ix / (left / 2 + thick + abs(y0))
    return mod 

# (top) __ 
#         |
# (mid)   |   <- This is a Z-shaped beam rotated 90 degrees
# (bot)   |__    The following function calculates its section modulus
def Z_rot90(top, mid, bot, thick):
    # solving the y-centroid integral by taking the origin at the center of the middle beam
    # y0 = integral of y * dA / integral of dA
    y0  = top * (mid + thick) / 2 - bot * (mid + thick) / 2
    y0 /= top + mid + bot
    # compute the integral of the second moment of area by each component
    # Ix = integral of (y - y0)^2 * dA
    Ix  = thick * ((mid/2 - y0)**3 - (-mid/2 - y0)**3) / 3  # middle beam
    Ix += top * ((mid/2 + thick - y0)**3 - (mid/2 - y0)**3) / 3  # top beam
    Ix += bot * ((-mid/2 - y0)**3 - (-mid/2 - thick - y0)**3) / 3  # bottom beam
    # compute the section modulus
    mod = Ix / max(mid / 2 + thick * (bot > 0) + y0, mid / 2 + thick * (top > 0) - y0)
    return mod

print(Z(0, 23, 67, 3))      # support arm
print(Z(30, 56.5, 15, 3))   # cross arm
print(G(14, 12, 50, 27, 3)) # bone
print(G(14, 12, 50, 27, 3)) # bone
print(Z_rot90(10, 40, 20, 4))
#print(Z(0, 23, 47, 3))