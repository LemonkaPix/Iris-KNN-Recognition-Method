import math

dataset = open("iris.csv", "r").read().split("\n")
dataset.pop(0)
dataset.pop(len(dataset)-1)

vectors = []
for item in dataset:
    temp = item.split(",")
    vectors.append({
        "sepal_length": float(temp[0]),
        "sepal_width": float(temp[1]),
        "petal_length": float(temp[2]),
        "petal_width": float(temp[3]),
        "species": temp[4]
    })

trainData = []
testData = []
testDataCount = int(len(vectors) * 0.2)
for i in range(len(vectors)):
    if i < len(vectors) - testDataCount:
        trainData.append(vectors[i])
    else:
        testData.append(vectors[i])

def distance_4d(vector1, vector2):
    return math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)))

correctPredictionsCount = 0
closestNeighbourDistance = 100
closestNeighbourString = ""
for i in testData:
    
