# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/design-tinyurl/#/description
from tiny_url_534 import Codec
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.codec = Codec()

    def test_encode_url(self):
        longurl = 'https://leetcode.com/problems/design-tinyurl'
        short_url = self.codec.encode(longurl)
        self.assertEqual(self.codec.decode(short_url), longurl)
