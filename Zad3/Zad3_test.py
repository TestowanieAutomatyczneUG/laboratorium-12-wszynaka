import unittest
from Zad3 import Messenger
from unittest.mock import Mock


class TestMessenger(unittest.TestCase):

    def setUp(self):
        self.temp = Messenger()

    def test_sendMessage(self):
        self.temp.send_message = Mock()
        self.temp.send_message.return_value = 'Message send'
        self.assertEqual('Message send', self.temp.send_message('mail', 'content'))

    def test_sendMessage_not_str(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, None, 'content')

    def test_sendMessage_not_str2(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, 'mail', None)

    def test_sendMessage_not_str3(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.send_message, None, None)

    def test_getMessage(self):
        self.temp.get_message = Mock()
        self.temp.get_message.return_value = ['hi', 'there']
        self.assertEqual(['hi', 'there'], self.temp.get_message('mail'))

    def test_getMessage_not_str(self):
        self.temp.get_message = Mock()
        self.temp.get_message.return_value = {}
        self.assertEqual({}, self.temp.get_message('mail'))

    def test_getMessage_not_str2(self):
        self.temp.get_message = Mock()
        self.temp.get_message.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.get_message, None)

    def tearDown(self):
        self.temp = None