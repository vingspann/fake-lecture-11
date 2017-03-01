import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response('Potato')
        self.assertEquals(response, '')

if __name__ == '__main__':
    unittest.main()