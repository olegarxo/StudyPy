def find_farthest_orbit(orbits):
    max_s = max([a * b for a, b in orbits if a != b])
    s = [(a, b) for a, b in orbits if a * b == max_s]
    return s


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
