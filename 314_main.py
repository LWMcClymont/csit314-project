import requests
import random

# change later to accept command line args
# arg1 = "1*1"
# arg2 = "-5*66"
# arg3 = "121*3"
# arg4 = "430*-2"
# arg5 = "-1*-99"

# creating a string containing the multiplication of 2 ints between 0 and 201
ran1 = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))
ran2 = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))
ran3 = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))
ran4 = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))
ran5 = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))

# counter for test cases
counter = 1

# function to evalute either the generated string or the given arguments
def evaluateEquation(string):
    ans = eval(string)
    return ans


pyAnswer1 = evaluateEquation(ran1)
pyAnswer2 = evaluateEquation(ran2)
pyAnswer3 = evaluateEquation(ran3)
pyAnswer4 = evaluateEquation(ran4)
pyAnswer5 = evaluateEquation(ran5)


#function that will compare the python evaluated answer and the answer given from the api request
def curlFunction(arg, pyAnswer):
    global counter
    req = requests.get('http://api.mathjs.org/v4/?expr='+arg)
    reqInt = int(req.text)
    if reqInt == pyAnswer:
        print("Test " + str(counter) + " = Success\nAPI calculator    " + arg + " = " + req.text + "\nPython calculator " + arg + " = " + str(pyAnswer) + "\n")
        counter += 1
    else:
        print("Test " + str(counter) + " = Fail\nAPI calculator " + arg + " = " + req.text + "\nPython calculator " + arg + " = " + str(pyAnswer) + "\n")
        counter += 1


curlFunction(ran1, pyAnswer1)
curlFunction(ran2, pyAnswer2)
curlFunction(ran3, pyAnswer3)
curlFunction(ran4, pyAnswer4)
curlFunction(ran5, pyAnswer5)


