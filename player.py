import json


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        # sys.stdout(game_state)

        print(json.dumps(game_state))

        action_ = game_state['in_action']
        mystatus = game_state['players'][action_]

        firstCard = mystatus['hole_cards'][0]
        secondCard = mystatus['hole_cards'][1]

        allIn = game_state['current_buy_in'] - mystatus['bet'] + game_state['minimum_raise']

        if firstCard['rank'] == secondCard['rank']:
            return allIn
        else:
            return 0

    def showdown(self, game_state):
        pass

