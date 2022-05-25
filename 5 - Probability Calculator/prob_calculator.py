import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.total = 0
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
                self.total += 1

    def __str__(self):
        return str(self.contents)

    def draw(self, num_balls: int):
        if self.total == 0:
            return None

        else:
            if num_balls > self.total:
                num_balls = self.total

            new_contents = copy.deepcopy(self.contents)
            balls_draw = []

            for i in range(num_balls):
                ball_no = random.randint(0, len(new_contents) - 1)
                balls_draw.append(new_contents[ball_no])
                new_contents.pop(ball_no)

                self.contents.pop(ball_no)
                self.total -= 1

            return balls_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    This function should accept the following arguments:
    hat:
        A hat object containing balls that should be copied inside the function.

    expected_balls:
        An object indicating the exact group of balls to attempt to draw from the 
        hat for the experiment. 

    num_balls_drawn:
        The number of balls to draw out of the hat in each experiment.

    num_experiments:
        The number of experiments to perform. 
        (The more experiments performed, the more accurate the approximate probability
         will be.)

    The experiment function should return a probability.
    '''
    m = 0
    test_hat = copy.deepcopy(hat)
    for i in range(num_experiments):
        drawed_balls = Counter(test_hat.draw(num_balls_drawn))

        is_contained = []
        for key in expected_balls:
            if key in drawed_balls and drawed_balls[key] >= expected_balls[key]:
                is_contained.append(True)
            else:
                is_contained.append(False)

        if not False in is_contained:
            m += 1

    return m/num_experiments
