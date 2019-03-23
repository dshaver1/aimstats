from datetime import datetime
import re


class Challenge:
    def __init__(self, name, score, damage, accuracy, date):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.score = score
        self.date = date

    def to_string(self):
        return "Scored {} on {}, doing {} damage with {:2.2f}% accuracy.".format(self.score,
                                                                                           self.name,
                                                                                           self.damage,
                                                                                           self.accuracy * 100) + "\n"

    @staticmethod
    def parse_date(filename):
        reg = re.match(r".+(\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}) Stats.csv", filename, re.IGNORECASE)
        date_str = reg.group(1)

        actual_date = datetime.strptime(date_str, "%Y.%m.%d-%H.%M.%S")

        return actual_date

    @staticmethod
    def parse_challenge_name(filename):
        reg = re.match(r"(.+) - Challenge - .+ Stats.csv", filename, re.IGNORECASE)
        challenge_name = reg.group(1)

        return challenge_name

    @staticmethod
    def parse_file(base, filename):
        timestamp = Challenge.parse_date(filename)
        challenge_name = Challenge.parse_challenge_name(filename)

        lines = open(base + filename, "r")

        score = 0.0
        damage_done = 0.0
        damage_possible = 0.0
        damage_possible_index = -1
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
                # print("score: {}".format(score))
                continue

            if damage_done == 0 and line.__contains__("Damage Done:,"):
                damage_done = float(line[line.index(",") + 1:len(line)])
                # print("damage: {}".format(damage_done))
                continue

            # Accuracy is different in that it's in an actual CSV format. We need to find the index of Damage Possible
            # in the header, split the next line by comma, then grab the correct string from the split. Once we have
            # Damage Possible, we can divide it with Damage Done to get accuracy percentage.
            if damage_possible_index == -1 and line.__contains__("Damage Possible"):
                line_split = line.split(",")
                damage_possible_index = line_split.index("Damage Possible")
                # print("Found damage possible index: {}".format(damage_possible_index))
                # Continue to next line since this line was merely a header.
                continue

            # if damagePossibleIndex is set, that means the previous line contained the string "Damage Possible", which
            # we consider the header of a csv. Sometimes we have empty csv rows, so we also need to check the length
            # of the current line.
            if damage_possible == 0 and int(damage_possible_index) > 0 and len(line) > 0:
                line_split = line.split(",")
                damage_possible = float(line_split[damage_possible_index])
                # print("Found damage possible: {}".format(damage_possible))

        return Challenge(challenge_name, score, damage_done, damage_done / damage_possible, timestamp)
