import json


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        # sys.stdout(game_state)

        print(json.dumps(game_state))
        action_ = game_state['in_action']
        return game_state['current_buy_in'] - game_state['players'][action_]['bet'] + game_state['minimum_raise']

    def showdown(self, game_state):
        pass

