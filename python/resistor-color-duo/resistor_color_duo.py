COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    """
    Take two colors as input and output the correct number.
    """
    num_1 = COLORS.index(colors[0])
    num_2 = COLORS.index(colors[1])
    return int(str(num_1) + str(num_2))
