from app import app, db
import unittest

class DivideTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_post(self):
        response = self.app.post('/api/divide', json={'a': 10, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5)

    def test_invalid_input(self):
        response = self.app.post('/api/divide', json={'a': 10, 'b': 'one'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Inputs must be integers')

    def test_divide_by_zero(self):
        response = self.app.post('/api/divide', json={'a': 10, 'b':0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'You cannot divide by 0')

if __name__ == '__main__':
    unittest.main()
