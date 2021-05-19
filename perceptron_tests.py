from perceptron import Perceptron
from perceptron import Point

k = Perceptron()
points = list()

for i in range(0, 200):
    points.append(Point())


for point in points:
    inputs = [point.x, point.y]
    print(inputs)
    k.train(inputs, point.label)

    print()

# 0.7128944917574527, -1.0739953769485413
# 2.5678649097302446e-06, -1.3545371279968294