import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response('Potato')
        self.assertEquals(response, '')
    def test_hello_command(self):
        response = functions.get_chatbot_response('!! hello there')
        self.assertEquals(response, 'Hey there!')
    def test_add_command(self):
        response = functions.get_chatbot_response('!! add 2 3')
        self.assertEquals(response, 5)
    def test_divide_command(self):
        response = functions.get_chatbot_response('!! divide 6 2')
        self.assertEquals(response, 3)
    def test_say_command(self):
        response = functions.get_chatbot_response('!! say butts')
        self.assertEquals(response, 'butts')
if __name__ == '__main__':
    unittest.main()