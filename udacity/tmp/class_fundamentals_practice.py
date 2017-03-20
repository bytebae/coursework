def hashSha256(data, prev=None):
    return "1" + data + (prev if prev else "")

def hashMd5sum(data, prev=None):
    return data + (prev if prev else "")

    
class Hash(object):
    def __init__(self, f):
        self.function = f
        self.prev = None
        
    @classmethod
    def sha256(cls):
        return cls(hashSha256)

    @classmethod
    def md5sum(cls):
        return cls(hashMd5sum)

    def update(self, val):
        self.prev = self.function(val, self.prev)

    def output(self):
        return self.prev


if __name__ == '__main__':

    s = Hash.sha256()
    # Usage
    s.update("abc")
    # ...
    s.update("pqr")
    # prints "1abc1pqr"
    print(s.output())

    m = Hash.md5sum()
    m.update("abc")
    m.update("pqr")
    # prints "abcpqr"
    print(m.output())
