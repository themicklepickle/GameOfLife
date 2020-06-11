# Project - Conway's Game of Life
# Functions to sanitize data
# Michael Xu
# May 19, 2020


# function for integer data sanitation
def integer(prompt_, min_, max_):
    while True:
        try:
            user_input = int(input(prompt_))
        except ValueError:
            continue
        else:
            if min_ is None and max_ is None:
                return user_input
                break
            elif min_ is None:
                if user_input <= max_:
                    return user_input
                    break
            elif max_ is None:
                if user_input >= min_:
                    return user_input
                    break
            else:
                if max_ >= user_input >= min_:
                    return user_input
                    break


def floating_point(prompt_, min_, max_):
    while True:
        try:
            user_input = float(input(prompt_))
        except ValueError:
            continue
        else:
            if min_ is None and max_ is None:
                return user_input
                break
            elif min_ is None:
                if user_input <= max_:
                    return user_input
                    break
            elif max_ is None:
                if user_input >= min_:
                    return user_input
                    break
            else:
                if max_ >= user_input >= min_:
                    return user_input
                    break
