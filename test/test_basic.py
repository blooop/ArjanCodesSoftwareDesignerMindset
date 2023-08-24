from arjan_codes_sw_design_mindset.basic_class import BasicClass

from unittest import TestCase


class TestBasicClass(TestCase):
    def test_init(self):
        instance = BasicClass()

        self.assertEqual(instance.int_var, 0)
