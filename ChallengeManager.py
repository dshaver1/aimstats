# Manager class for challenges. Responsible for collecting runs of different challenges and placing them in the proper
# bucket. Primary interface for rendering UI.
from Challenge import Challenge


class ChallengeManager:
    def __init__(self):
        self.challenges = {}

    def add_run(self, run):
        challenge = None
        if self.challenges.__contains__(run.name):
            challenge = self.challenges[run.name]
        else:
            challenge = Challenge(run.name)
            self.challenges[run.name] = challenge

        challenge.add_run(run)

    def high_score_for_challenge(self, challenge_name):
        return self.challenges[challenge_name].high_score

    def all_high_scores(self):
        high_scores = {}
        for name in self.challenges:
            challenge = self.challenges[name]
            high_scores[challenge.name] = challenge.high_score()

        return high_scores
