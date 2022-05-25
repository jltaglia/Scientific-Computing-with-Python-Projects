import prob_calculator

prob_calculator.random.seed(95)

hat = prob_calculator.Hat(red=3,blue=2)
print(hat.contents)
print(hat)

hat = prob_calculator.Hat(red=5,blue=2)
actual = hat.draw(2)
expected = ['blue', 'red']
print('actual ->', actual)
print('expected ->', expected)


actual = len(hat.contents)
expected = 5
print('actual ->', actual)
print('expected ->', expected)



hat = prob_calculator.Hat(blue=3, red=2, green=6)
probability = prob_calculator.experiment(
                hat=hat, 
                expected_balls={"blue": 2, "green": 1},
                num_balls_drawn=4,
                num_experiments=1000)
actual = probability
expected = 0.272
print('actual ->', actual)
print('expected ->', expected)


print('------------------------')


hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = prob_calculator.experiment(
                hat=hat,
                expected_balls={"yellow": 2, "blue": 3, "test": 1},
                num_balls_drawn=20,
                num_experiments=100)
actual = probability
expected = 1.0
print('actual ->', actual)
print('expected ->', expected)
