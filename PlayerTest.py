import unittest


class TestStringMethods(unittest.TestCase):

    # def test_diff_rank(self):
    #     self.assertEqual(Player.betRequest(self, json.loads('{  "game_id": "598eb80f831444000400001c",  "big_blind": 30,  "bet_index": 7,  "minimum_raise": 985,  "small_blind": 15,  "players": [    {      "id": 0,      "bet": 1015,      "version": "Maverik",      "status": "active",      "name": "Maverik",      "time_used": 631148,      "stack": 1677    },    {      "id": 1,      "bet": 0,      "version": "0.1",      "status": "out",      "name": "Z team",      "time_used": 19945,      "stack": 0    },    {      "id": 2,      "bet": 0,      "version": "Default Java folding player",      "status": "out",      "name": "Excited Bird",      "time_used": 44940,      "stack": 0    },    {      "id": 3,      "bet": 30,      "hole_cards": [        {          "suit": "hearts",          "rank": "3"        },        {          "suit": "clubs",          "rank": "9"        }      ],      "version": "Default Python folding player",      "status": "active",      "name": "Wise Kaa 2",      "time_used": 702002,      "stack": 278    }  ],  "current_buy_in": 1015,  "orbits": 10,  "community_cards": [],  "tournament_id": "598e25d6b0cdd800040018da",  "pot": 1045,  "in_action": 3,  "dealer": 3,  "round": 40}')), 0)
    #
    # def test_equals_rank(self):
    #     self.assertEqual(Player.betRequest(self, json.loads('{  "game_id": "598eb80f831444000400001c",  "big_blind": 30,  "bet_index": 7,  "minimum_raise": 985,  "small_blind": 15,  "players": [    {      "id": 0,      "bet": 1015,      "version": "Maverik",      "status": "active",      "name": "Maverik",      "time_used": 631148,      "stack": 1677    },    {      "id": 1,      "bet": 0,      "version": "0.1",      "status": "out",      "name": "Z team",      "time_used": 19945,      "stack": 0    },    {      "id": 2,      "bet": 0,      "version": "Default Java folding player",      "status": "out",      "name": "Excited Bird",      "time_used": 44940,      "stack": 0    },    {      "id": 3,      "bet": 30,      "hole_cards": [        {          "suit": "hearts",          "rank": "9"        },        {          "suit": "clubs",          "rank": "9"        }      ],      "version": "Default Python folding player",      "status": "active",      "name": "Wise Kaa 2",      "time_used": 702002,      "stack": 278    }  ],  "current_buy_in": 1015,  "orbits": 10,  "community_cards": [],  "tournament_id": "598e25d6b0cdd800040018da",  "pot": 1045,  "in_action": 3,  "dealer": 3,  "round": 40}')), 1970)

    def dummy(self):
        self.assertEquals(1,1)

if __name__ == '__main__':
    unittest.main()