import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            drawBalls = random.choices(self.contents, k=number)
            for i in range(len(drawBalls)):
                self.contents.remove(drawBalls[i])
            return drawBalls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    positiveResult = 0

    if num_balls_drawn > len(hat.contents):
        num_balls_drawn = len(hat.contents)

    for i in range(num_experiments):

        drawnArray = random.sample(hat.contents, k=num_balls_drawn)
        lengthBefore = len(drawnArray)
        numberOfExpected = 0
        for key, value in expected_balls.items():
            for i in range(value):
                if drawnArray.count(key) > 0:
                    drawnArray.remove(key)
            numberOfExpected += value

        if ( (lengthBefore - len(drawnArray)) == numberOfExpected):
            positiveResult += 1

    probability = positiveResult / num_experiments
    return probability
    

