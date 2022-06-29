class Codec:

    def __init__(self):
        self.count = 0
        self.dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.dict[self.count] = longUrl
        return "http://tinyurl.com/"+str(self.count)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = int(shortUrl.split('/')[-1])
        return self.dict[index]

#----------------------------------------------------------------------
import hashlib
d = {}
class Codec2:

    def encode(self, longUrl):
        """
        Runtime: 12 ms, faster than 98.35% of Python online submissions for Encode and Decode TinyURL.
        Memory Usage: 13.9 MB, less than 8.26% of Python online submissions for Encode and Decode TinyURL.
        Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        x = hashlib.md5(longUrl).hexdigest()
        d[x] = longUrl
        return x

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
codec.decode(codec.encode("http://tinyurl.com/1"))