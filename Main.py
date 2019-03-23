from Challenge import Challenge
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':

    # Get stats directory from user. Implement search function
    statsPath = input("Path to stats directory?")
    if len(statsPath) == 0:
        statsPath = "H:\\Games\\steamapps\\common\\FPSAimTrainer\\FPSAimTrainer\\stats"

    # If user input didn't end in a slash, add it.
    if statsPath[len(statsPath):len(statsPath)] != "\\":
        statsPath = statsPath + "\\"

    # Get the list of filenames in the stats directory
    onlyFiles = [f for f in listdir(statsPath) if isfile(join(statsPath, f))]
    print("Found {} challenge stats in {}.".format(len(onlyFiles), statsPath))

    # Iterate over all files
    for f in onlyFiles:
        testChallenge = Challenge.parse_file(statsPath, f)
        print(testChallenge.to_string())
