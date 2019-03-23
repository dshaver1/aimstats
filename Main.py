from ChallengeManager import ChallengeManager
from Run import Run
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':

    defaultPath = "H:\\Games\\steamapps\\common\\FPSAimTrainer\\FPSAimTrainer\\stats"
    # Get stats directory from user. TODO: Implement search function so users don't need to do this?
    statsPath = input("Path to stats directory? ({}) ".format(defaultPath))
    if len(statsPath) == 0:
        statsPath = defaultPath

    # If user input didn't end in a slash, add it.
    if statsPath[len(statsPath):len(statsPath)] != "\\":
        statsPath = statsPath + "\\"

    # Get the list of filenames in the stats directory
    onlyFiles = [f for f in listdir(statsPath) if isfile(join(statsPath, f))]
    print("Found {} challenge stats in {}.".format(len(onlyFiles), statsPath))

    # We're going to create a map of challenge names to Challenge objects, which in turn contain the list of runs.
    manager = ChallengeManager()

    # Iterate over all files
    for f in onlyFiles:
        run = Run.parse_file(statsPath, f)
        print(run.to_string())
        manager.add_run(run)

    print(manager.all_high_scores())
