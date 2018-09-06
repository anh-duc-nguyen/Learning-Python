from life import *
import sys

inn = sys.stdin
err = sys.stderr
out = sys.stdout

def runTest(testCase):
    return{
        "1": smokeTest,
        "2": testGaia,
        "3": testPartical,
        "4": testTick
    }.get(testCase,smokeTest)()

def smokeTest():
    print("---------SMOKE TEST--------")
    earth = Gaia()
    earth.show()
    pass 

def testGaia():
    print("--------Test Gaia ----------")
    earth = Gaia()
    earth.show()
    for i in earth.curr:
        for j in i:
            print(j.neighbors())
    pass

def testPartical():
    print("--------Test Partical ------------")
    earth = Gaia()
    earth.curr[1][2].live()
    earth.curr[2][2].live()
    earth.curr[3][2].live()
    earth.curr[2][3].live()
    earth.show()
    earth.curr[2][3].kill()
    earth.show()
    pass

def testTick():
    print("--------Test Tick ------------")
    earth = Gaia()
    earth.curr[1][2].live()
    earth.curr[2][2].live()
    earth.curr[3][2].live()
    print("State One")
    earth.show()
    print("Star next Tick")
    earth.nextTick()
    earth.show()


if __name__ == "__main__":
    testCase = inn.readline().strip('\n')
    # testCase = str(testCase)
    # print (testCase)
    # testCase = int(testCase)
    runTest(testCase)