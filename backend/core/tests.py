from django.test import TestCase


class InitiateGameTest(TestCase):
    def test_initiate_game(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)

class SetRobotTest(TestCase):
    def test_set_robot(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        
        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )
    def test_set_robot_invalid_position(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        
        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [11, 11]})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error_code'], 'invalid')

class SetDinosaursTest(TestCase):
    def test_set_dinosaur(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        

        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[2, 1], [2, 2]]})
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

    def test_set_dinosaurs_invalid_positions(self):

        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        
        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[11, 11], [11, 12]]})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error_code'] , 'invalid')

class MoveActionTest(TestCase):
    def test_move_action(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[2, 1], [2, 2]]})
        print(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/1/action/move', {'action_type': 'move', 'direction': 'W'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )
class AttackActionTest(TestCase):
    def test_attack_action(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        

        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[2, 1], [2, 2]]})
        self.assertEqual (response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/1/action/attack')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

class GameOverTest(TestCase):
    def test_game_over(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        

        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[0, 1], [2, 1]]})
        self.assertEqual (
            response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/1/action/attack')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 3)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

# Integration tests
class GameTest(TestCase):
    def test_game(self):
        response = self.client.post('/api/v1/games/initiate-game/start', {'player': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        

        response = self.client.post('/api/v1/games/initiate-game/1/set-robot', {'robot_position': [1, 1]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/initiate-game/1/set-dinosaur', {'dinosaurs_positions': [[0, 1], [2, 1]]})
        self.assertEqual (
            response.status_code
            , 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/1/action/move', {'action_type': 'move', 'direction': 'W'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )

        response = self.client.post('/api/v1/games/1/action/move', {'action_type': 'move', 'direction': 'E'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['player'], 'test')
        self.assertEqual(response.data['status'], 2)
        self.assertEqual(response.data['board'], {
            'id': 1,
            'game': 1,
            'cells': [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        } )
        

