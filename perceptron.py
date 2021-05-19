from random import randint, random, seed, uniform

# função de ativação
def sign(n):
    return (1 if n>=0 else -1)


class Perceptron:
    # construtor
    weights = list()
    def __init__(self):
        self.weights = [0, 0]

        # inicializar os pesos aleatoriamente
        for i in range(0, len(self.weights)):
            self.weights[i] = uniform(-1, 1)
        # self.weights[0] = 0.7
        # self.weights[1] = -1


    def guess(self, inputs):
        sum = 0

        for i in range(0, len(self.weights)):
            sum += self.weights[i] * inputs[i]
            # print(f'{self.weights[i]} * {inputs[i]} * 0.1 = {sum}')

        
        output = sign(sum)
        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # print(f'guess: {guess}')
        # print(f'target: {target}')
        print(f'weights: {self.weights}')
        print(f'error: {error}')

        # ajustando todos os pesos
        for i in range(0, len(self.weights)):
            delta = error * inputs[i] * 0.05
            self.weights[i] = self.weights[i] + delta


class Point:
    def __init__(self) -> None:
        self.x = randint(0, 50)
        self.y = randint(0, 50)
        self.label = -1

        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1