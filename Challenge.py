class Challenge:
    def __init__(self, name, damage, accuracy, score):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.score = score

    def to_string(self):
        return "Scored {} on {} challenge, doing {} damage with {} accuracy.".format(self.score, self.name, self.damage, self.accuracy)
