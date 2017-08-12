import json
import sys


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        # sys.stdout(game_state)

        print(json.dumps(game_state))
        return 20

    def showdown(self, game_state):
        pass

