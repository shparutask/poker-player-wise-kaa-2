import json
import sys


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        # sys.stdout(game_state)

        print(json.dumps(game_state))
        return game_state.big_blind

    def showdown(self, game_state):
        pass

