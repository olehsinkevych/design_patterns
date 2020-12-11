from scream_behavior import ScreamBehavior


class MuteScream(ScreamBehavior):
    def scream(self):
        print('*Тишина*')