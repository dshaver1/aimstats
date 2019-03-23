# A simple container fcr encapsulating statistics about a particular challenge within Kovaak's. A challenge contains a
# list of runs. Each run details the statistics for a single instance of the player's performance


class Challenge:
    def __init__(self, name):
        self.name = name
        self.runs = []

    def add_run(self, run):
        self.runs.append(run)

    def high_score(self):
        high_score = 0
        for run in self.runs:
            if run.score > high_score:
                high_score = run.score

        return high_score
