
import unittest
from ..models import rectangle as rect

class TestRect(unittest.TestCase):

    def setUp(self):
        self.shape_rect = rect.Rectangle(2, 3)

    def test_area(self):
        self.assertEqual(self.shape_rect.area(2, 3), 6)

    def test_perimeter(self):
        self.assertRaises(TypeError,self.shape_rect,10, "3")
        self.assertRaises(ValueError,self.shape_rect,10, -3)
