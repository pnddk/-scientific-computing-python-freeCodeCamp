import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, balls_drawn):
        if balls_drawn > len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, balls_drawn)
            for ball in drawn_balls:
                self.contents.remove(ball)    
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    exp_num_balls = []   

    for index in expected_balls:
        exp_num_balls.append(expected_balls[index])
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn) 
      
        actual_num_balls = []

        for index in expected_balls:
            actual_num_balls.append(drawn_balls.count(index))

        if actual_num_balls >= exp_num_balls:
            successful_experiments += 1

    return successful_experiments / num_experiments
