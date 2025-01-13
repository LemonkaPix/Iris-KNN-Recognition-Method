import math

dataset = open("iris.csv", "r").read().split("\n")
dataset.pop(0)
dataset.pop(len(dataset)-1)

vectors = []
for item in dataset:
    temp = item.split(",")
    vectors.append([
        float(temp[0]),
        float(temp[1]),
        float(temp[2]),
        float(temp[3]),
        temp[4]
    ])

trainData = []
testData = []
for i in range(len(vectors)):
    if i % 5 != 0:
        trainData.append(vectors[i])
    else:
        testData.append(vectors[i])

def Distance_4d(vector1, vector2):
    return math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)))

def RecognizeIris(input, data):

    closestNeighbourDistance = math.inf
    closestNeighbourString = ""

    for record in data:
        distance = Distance_4d(input[0:4], record[0:4])
        if distance < closestNeighbourDistance:
            closestNeighbourDistance = distance
            closestNeighbourString = record[-1]
    return closestNeighbourString


correctPredictionsCount = 0
for case in testData:

    answer = case[-1]

    prediction = RecognizeIris(case, trainData)

    if prediction == answer:
        correctPredictionsCount += 1

percentage = float(correctPredictionsCount) / float(len(testData)) * 100.0
print("Model precission: " + str(percentage) + "%")
print()

print("Sepal length (cm): ")
userInput = [float(input())]
print("Sepal width (cm): ")
userInput.append(float(input()))
print("Petal length (cm): ")
userInput.append(float(input()))
print("Petal width (cm): ")
userInput.append(float(input()))

print("Your iris is " + RecognizeIris(userInput, vectors))