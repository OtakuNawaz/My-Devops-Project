import unittest

def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y



class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10,5),15)
        self.assertEqual(add(-1,5),4)
        self.assertEqual(add(-4,-5),-9)

    def test_subtract(self):
            self.assertEqual(subtract(10,5),5)
            self.assertEqual(subtract(-1,5),-6)
            self.assertEqual(subtract(-4,-5),1)

    def test_multiply(self):
            self.assertEqual(multiply(10,5),15)
            self.assertEqual(multiply(-1,5),-5)
            self.assertEqual(multiply(-4,-5),20)
            self.assertEqual(multiply(1,-5),-5)



# Faced some issue when i created a seperate file with calc funtions and tried importing it thus did everything in the same file.