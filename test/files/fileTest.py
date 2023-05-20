class Singleton:
    m = 4
    def test():
        print("hello world",Singleton.m)
        
Singleton.m = 10
Singleton.test()