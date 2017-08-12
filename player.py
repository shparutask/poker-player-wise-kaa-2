import json

import requests
import sys

class Player:
    VERSION = "Default Python folding player"

    def rank_request(self, cards):
        url = "http://rainman.leanpoker.org/rank"

        myResponse = requests.post(url, data='cards=' + json.dumps(cards))
        print(myResponse.status_code)

        if (myResponse.ok):
            jData = json.loads(myResponse.content)
            return jData['rank']
        else:
            return -1

    def getAllCards(self, game_state):
        action_ = game_state['in_action']
        mystatus = game_state['players'][action_]
        communityCards = game_state['community_cards']
        mycards = mystatus['hole_cards']

        return communityCards + mycards

    def betRequest(self, game_state):
        try:
            print(json.dumps(game_state))

            action_ = game_state['in_action']
            mystatus = game_state['players'][action_]

            communityCards = game_state['community_cards']
            mycards = mystatus['hole_cards']

            current_buy = game_state['current_buy_in']

            theCall = current_buy - mystatus['bet']
            theRaise = theCall+game_state['big_blind']

            allIn = theCall + game_state['minimum_raise']

            if len(communityCards) > 0:
                rank = self.rank_request(communityCards + mycards)

                if rank > 2:
                    return allIn
                elif rank > 0 and current_buy > mystatus['stack'] / 4:
                    return theCall
                else:
                    return 0

            firstCard = mycards[0]
            secondCard = mycards[1]

            if firstCard['rank'] == secondCard['rank']:
                return theRaise
            else:
                if mystatus['current_buy_in'] > mystatus['stack'] / 4:
                    return 0
        except:
            print("Unexpected error:", sys.exc_info()[0])

        return 0

    def showdown(self, game_state):
        pass

