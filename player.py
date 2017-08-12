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
        fold = 0
        # try:
        print(json.dumps(game_state))

        action_ = game_state['in_action']
        mystatus = game_state['players'][action_]

        communityCards = game_state['community_cards']
        mycards = mystatus['hole_cards']

        current_buy = game_state['current_buy_in']

        myBet = mystatus['bet']
        bigBlind = game_state['big_blind']

        theCall = current_buy - myBet
        theRaise = theCall + bigBlind

        allIn = theCall + game_state['minimum_raise']

        if len(communityCards) > 0:
            rank = self.rank_request(communityCards + mycards)

            if rank > 2:
                return allIn
            elif rank == 1 and current_buy < mystatus['stack'] / 4:
                return theCall
            else:
                return fold

        firstCard = mycards[0]
        secondCard = mycards[1]

        if firstCard['rank'] == secondCard['rank']:
            return theRaise
        else:
            # Если ставка меньше 1/4 банка тогда сброс
            # [СБРОС]
            if current_buy > mystatus['stack'] / 4:
                return fold
            elif myBet < bigBlind:
                return bigBlind
            # Если колл 0, тогда поднимаем - первая наша ставка
            elif theCall == 0:
                return theRaise
            # Или колл
            else:
                return theCall
        # except:
        #     print("Unexpected error:", sys.exc_info()[0])

        return fold

    def showdown(self, game_state):
        pass

