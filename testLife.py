from life import *
import sys

inn = sys.stdin
err = sys.stderr
out = sys.stdout

def runTest(testCase):
    return{
        "1": smokeTest,
        "2": testGaiaBoard,
        "3": testPartical
    }.get(testCase,smokeTest)()

def smokeTest():
    print("---------SMOKE TEST--------")
    earth = Gaia()
    earth.show()
    pass 

def testGaiaBoard():
    print("--------Test Gaia Board ----------")
    earth = Gaia()
    earth.show()
    for i in earth.board:
        for j in i:
            print(j.neighbors())
    pass

def testPartical():
    print("--------Test Partical ------------")
    pass


if __name__ == "__main__":
    testCase = inn.readline().strip('\n')
    # testCase = str(testCase)
    # print (testCase)
    # testCase = int(testCase)
    runTest(testCase)