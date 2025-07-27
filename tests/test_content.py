import unittest
from src.content_generator import generate_content

class TestContentGenerator(unittest.TestCase):
    def test_generate_content(self):
           content = generate_content("instagram")
           self.assertIsInstance(content, str)
           self.assertGreater(len(content), 0)

if __name__ == '__main__':
       unittest.main()