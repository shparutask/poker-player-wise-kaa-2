import json
import unittest

from player import Player


class TestStringMethods(unittest.TestCase):

    def test_diff_rank(self):
         player = Player()
         # self.assertEqual(player.betRequest(json.loads('{"current_buy_in": 110, "round": 5, "orbits": 1, "community_cards": [{"suit": "spades", "rank": "K"}, {"suit": "diamonds", "rank": "5"}, {"suit": "spades", "rank": "J"}], "pot": 330, "tournament_id": "598e25d6b0cdd800040018da", "minimum_raise": 4, "game_id": "598f0e2983144400040002dc", "bet_index": 0, "dealer": 2, "big_blind": 4, "players": [{"version": "Maverik", "name": "Maverik", "bet": 0, "time_used": 40189, "status": "out", "id": 0, "stack": 0}, {"version": "0.1", "name": "Z team", "bet": 110, "time_used": 12404125, "status": "active", "id": 1, "stack": 2858}, {"version": "Excited Fish", "name": "Excited Bird", "bet": 110, "time_used": 464251, "status": "active", "id": 2, "stack": 0}, {"version": "Default Python folding player", "name": "Wise Kaa 2", "hole_cards": [{"suit": "diamonds", "rank": "7"}, {"suit": "diamonds", "rank": "3"}], "bet": 110, "time_used": 1087506, "status": "active", "id": 3, "stack": 812}], "small_blind": 2, "in_action": 3}')), 0)
         self.assertEqual(player.betRequest(json.loads('{"current_buy_in": 110, "round": 5, "orbits": 1, "community_cards": [], "pot": 330, "tournament_id": "598e25d6b0cdd800040018da", "minimum_raise": 4, "game_id": "598f0e2983144400040002dc", "bet_index": 0, "dealer": 2, "big_blind": 4, "players": [{"version": "Maverik", "name": "Maverik", "bet": 0, "time_used": 40189, "status": "out", "id": 0, "stack": 0}, {"version": "0.1", "name": "Z team", "bet": 110, "time_used": 12404125, "status": "active", "id": 1, "stack": 2858}, {"version": "Excited Fish", "name": "Excited Bird", "bet": 110, "time_used": 464251, "status": "active", "id": 2, "stack": 0}, {"version": "Default Python folding player", "name": "Wise Kaa 2", "hole_cards": [{"suit": "diamonds", "rank": "7"}, {"suit": "diamonds", "rank": "3"}], "bet": 110, "time_used": 1087506, "status": "active", "id": 3, "stack": 812}], "small_blind": 2, "in_action": 3}')), 0)

    def test_request(self):
        # raise NameError(res)
        player = Player()
        self.assertEqual(0, player.rank_request(json.loads('[{"suit": "hearts","rank": "3"},{"suit": "clubs","rank": "9"},{"rank": "10", "suit": "diamonds"}, {"rank": "5", "suit": "diamonds"}, {"rank": "6", "suit": "clubs"}]')))


    def test_all_cards(self):
        player = Player()
        self.assertEqual(5, len(player.getAllCards(json.loads('{"in_action": 3, "tournament_id": "598e25d6b0cdd800040018da", "players": [{"status": "out", "name": "Maverik", "id": 0, "version": "Maverik", "time_used": 43696, "bet": 0, "stack": 0}, {"status": "active", "name": "Z team", "id": 1, "version": "0.1", "time_used": 2408637, "bet": 140, "stack": 3218}, {"status": "out", "name": "Excited Bird", "id": 2, "version": "Excited Fish", "time_used": 62689, "bet": 0, "stack": 0}, {"hole_cards": [{"rank": "A", "suit": "diamonds"}, {"rank": "8", "suit": "hearts"}], "status": "active", "name": "Wise Kaa 2", "id": 3, "version": "Default Python folding player", "time_used": 1972094, "bet": 140, "stack": 502}], "pot": 280, "dealer": 3, "orbits": 23, "bet_index": 2, "minimum_raise": 140, "small_blind": 70, "round": 93, "big_blind": 140, "community_cards": [{"rank": "10", "suit": "diamonds"}, {"rank": "5", "suit": "diamonds"}, {"rank": "6", "suit": "clubs"}], "game_id": "598ecf438314440004000096", "current_buy_in": 140}'))))

if __name__ == '__main__':
    unittest.main()