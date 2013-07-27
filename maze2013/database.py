from redis import StrictRedis

r = StrictRedis()
_k = lambda k: "maze.%s" % k

if __name__ == '__main__':
    print r
