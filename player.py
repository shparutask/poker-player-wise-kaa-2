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
        return 1000       

    def showdown(self, game_state):
        pass

