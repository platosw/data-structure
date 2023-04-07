"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    data = open(filename)

    species = set()

    # TODO: replace this with your code
    for line in data:
        line = line.split('|')
        species.add(line[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    data = open(filename)
    villagers = []

    if search_string == 'All':
        for line in data:
            line = line.split('|')
            villagers.append(line[0])
    else:
        for line in data:
            line = line.split('|')
            if search_string == line[1]:
                villagers.append(line[0])

    # TODO: replace this with your code

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    data = open(filename)

    music = []
    fashion = []
    nature = []
    play = []
    education = []
    fitness = []

    for line in data:
        line = line.split('|')
        if line[3] == 'Music':
            music.append(line[0])
        elif line[3] == 'Fashion':
            fashion.append(line[0])
        elif line[3] == 'Nature':
            nature.append(line[0])
        elif line[3] == 'Play':
            play.append(line[0])
        elif line[3] == 'Education':
            education.append(line[0])
        elif line[3] == 'Fitness':
            fitness.append(line[0])

    return [music, fashion, nature, play, education, fitness]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    data = open(filename)

    all_data = []

    # TODO: replace this with your code
    for line in data:
        line = line.split('|')
        line[4] = ''.join(list(line[4])[:-1])
        all_data.append((line[0], line[1], line[2], line[3], line[4]))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    data = open(filename)

    result = None

    for line in data:
        line = line.split('|')
        if villager_name in line:
            motto = ''.join(list(line[4])[:-1])
            result = f'Name: {line[0]}, Motto: {motto}'

    return result


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    data = open(filename)
    # TODO: replace this with your code
    same_personality = set()

    villager = None
    for line in data:
        line = line.split('|')

        if villager_name == line[0]:
            villager = line[2]
            break

    data.close()
    data = open(filename)

    if villager:
        print(villager)
        for line in open(filename):
            line = line.split('|')
            if line[2] == villager:
                same_personality.add(line[0])

    return same_personality


# print(all_species('villagers.csv'))
# print(get_villagers_by_species('villagers.csv', 'Anteater'))
# print(all_names_by_hobby('villagers.csv'))
# print(all_data('villagers.csv'))
# print(find_motto('villagers.csv', 'Audie'))
print(find_likeminded_villagers('villagers.csv', 'Cyrano'))
