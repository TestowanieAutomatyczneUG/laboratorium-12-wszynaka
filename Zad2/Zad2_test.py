import unittest
from unittest.mock import *
from Zad2 import Subscriber


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_person(self):
        self.temp.add_person = MagicMock(return_value=["Person"])
        self.assertEqual(["Person"], self.temp.add_person())

    def test_add_person_not_str(self):
        self.temp.add_person = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.add_person(1)

    def test_add_person_not_str2(self):
        self.temp.add_person = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.add_person(43.34123)

    def test_delete_person(self):
        self.temp.delete_person = MagicMock(return_value=[])
        self.assertEqual([], self.temp.delete_person("Perosn"))

    def test_delete_person_not_str(self):
        self.temp.delete_person = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.delete_person(1)

    def test_delete_perosn_list(self):
        self.temp.delete_person = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.delete_person([])

    def test_delete_not_exist(self):
        self.temp.delete_person = MagicMock(side_effect=Exception("This person doesn't exist!"))
        with self.assertRaisesRegex(Exception, "This person doesn't exist!"):
            self.temp.delete_person("Person3")

    def test_send_message(self):
        self.temp.send_message = MagicMock(return_value=True)
        self.assertTrue(self.temp.send_message("333", "222"))

    def test_send_message_not_str(self):
        self.temp.send_message = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.send_message(8, "Hello")

    def test_send_message_not_str2(self):
        self.temp.send_message = MagicMock(side_effect=Exception("its not string"))
        with self.assertRaisesRegex(Exception, "its not string"):
            self.temp.send_message({}, "Maciek")

    def tearDown(self):
        self.temp = None