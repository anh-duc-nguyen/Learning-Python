from life import *
import sys

def runTest(testCase):
    return{
        "a": smokeTest,
        "2": testGaiaBoard,
        "3": testPartical
    }.get(testCase,smokeTest)()

def smokeTest():
    print("---------SMOKE TEST--------")
    pass 

def testGaiaBoard():
    print("--------Test Gaia Board ----------")
    pass

def testPartical():
    print("--------Test Partical ------------")
    pass


if __name__ == "__main__":
    testCase = sys.stdin.readline().strip('\n')
    # testCase = str(testCase)
    # print (testCase)
    # testCase = int(testCase)
    runTest(testCase)