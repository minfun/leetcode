# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/design-tinyurl/#/description

import string
import random
import unittest


class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url_code = {}
        self.code_url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.code_url.keys():
            # while encode_str not in self.url_code.keys():
            encode_str = ''.join(random.choice(self.alphabet) for _ in range(6))
            if encode_str not in self.code_url.values():
                self.url_code[encode_str] = longUrl
                self.code_url[longUrl] = encode_str
        return 'http://tinyurl.com/' + encode_str

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.url_code.get(shortUrl[-6:], None)


class Test(unittest.TestCase):

    def setUp(self):
        self.codec = Codec()

    def test_encode_url(self):
        longUrl = 'https://leetcode.com/problems/design-tinyurl'
        short_url = self.codec.encode(longUrl)
        self.assertEqual(self.codec.decode(short_url), longUrl)

if __name__ == '__main__':
    unittest.main()
