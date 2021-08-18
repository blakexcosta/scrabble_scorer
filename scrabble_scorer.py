# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(
                    char=char, point_value=point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.


def initial_prompt():
    print("Let's play some Scrabble!\n")
    user_input = input("input a word please:")
    return user_input


def simple_scorer(word):
    score = 0
    for char in word:
        score += 1
    return score


def vowel_bonus_scorer(word):
    score = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word.lower():
        if(char in vowels):
            score += 3
        else:
            score += 1
    return score

# will create a new dictionary with lowercase letters as keys and their points values as values


def transform(old_point_struct):
    transformed_dict = {}
    # will return a dictionary with lowercase letters as keys
    for key, value in old_point_struct.items():
        for letter in value:
            transformed_dict[letter.lower()] = int(key)
    # print(transformed_dict)
    return transformed_dict


new_point_structure = transform(OLD_POINT_STRUCTURE)


def scrabble_scorer(word):
    score = 0
    for char in word:
        score += new_point_structure[char.lower()]
    return score


scoring_algorithms = (
    {
        "name": "simple",
        "description": "simple way of doing scoring",
        "scoring_function": simple_scorer
    },
    {
        "name": "vowels",
        "description": "scores based upon vowels",
        "scoring_function": vowel_bonus_scorer
    },
    {
        "name": "new",
        "description": "new way of doing scrabble scorer",
        "scoring_function": scrabble_scorer
    }
)


def scorer_prompt():
    algorithm_select = input(
        "which algorithm do you want to use?\n\t'0' for simple\n\t'1' for vowels\n\t'2' for new scrabble\n")
    algorithm_select = int(algorithm_select)
    return scoring_algorithms[algorithm_select]


def run_program():
    # get the word we want
    word = initial_prompt()
    # select algorithm we want
    algorithm_dict = scorer_prompt()
    algo_name = algorithm_dict["name"]
    print(f"\nalgorithm selected: {algo_name}\n\trunning algorithm...")

    # run algorithm with function selected
    function = algorithm_dict["scoring_function"]
    score = function(word)
    print(f"SCORE RECEIVED: {score}")

    # transform


run_program()
