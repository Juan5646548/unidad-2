from math import pi
def ley_kepler(G: float, M: float, T: float) ->float:
    return ((G*M) / 4*(pi**2)*(T**2))