def is_triangle(sides):
    cond_1 = sum(sides) > 0
    cond_2 = sorted(sides)[0] + sorted(sides)[1] >= sorted(sides)[2]
    return cond_1 and cond_2

def equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)

def isosceles(sides):
    return len(set(sides)) <= 2 and is_triangle(sides)

def scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides)