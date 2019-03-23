class Challenge:
    def __init__(self, name, score, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.score = score

    def to_string(self):
        return "Scored {} on {} challenge, doing {} damage with {:2.2f}% accuracy.".format(self.score, self.name, self.damage, self.accuracy * 100) + "\n\n"

    @staticmethod
    def parse_file(base, filename):
        lines = open(base + filename, "r")

        name = filename
        score = 0.0
        damageDone = 0.0
        damagePossible = 0.0
        damagePossibleIndex = -1
        skip = False

        # Iterate over each line in the file to grab the relevant bits
        for line in lines:
            # Currently used for skipping kill list.
            if skip:
                if len(line) < 2:
                    # We've reached the end of the kill list, so stop skipping lines.
                    skip = False
                continue

            # I don't care about the enumerated kill list at this point. Maybe in the future?
            if line.__contains__("Kill #"):
                skip = True
                continue

            # All numbers are prefaced by a comma, so grab the substring from the character after the comma, to the
            # end of the string.
            if score == 0 and line.__contains__("Score:,"):
                score = float(line[line.index(",") + 1:len(line)])
                print("score: {}".format(score))
                continue

            if damageDone == 0 and line.__contains__("Damage Done:,"):
                damageDone = float(line[line.index(",") + 1:len(line)])
                print("damage: {}".format(damageDone))
                continue

            # Accuracy is different in that it's in an actual CSV format. We need to find the index of Damage Possible
            # in the header, split the next line by comma, then grab the correct string from the split. Once we have
            # Damage Possible, we can divide it with Damage Done to get accuracy percentage.
            if damagePossibleIndex == -1 and line.__contains__("Damage Possible"):
                lineSplit = line.split(",")
                damagePossibleIndex = lineSplit.index("Damage Possible")
                print("Found damage possible index: {}".format(damagePossibleIndex))
                # Continue to next line since this line was merely a header.
                continue

            # if damagePossibleIndex is set, that means the previous line contained the string "Damage Possible", which
            # we consider the header of a csv. Sometimes we have empty csv rows, so we also need to check the length
            # of the current line.
            if damagePossible == 0 and int(damagePossibleIndex) > 0 and len(line) > 0:
                lineSplit = line.split(",")
                damagePossible = float(lineSplit[damagePossibleIndex])
                print("Found damage possible: {}".format(damagePossible))

        return Challenge(name, score, damageDone, damageDone / damagePossible)
