sampleList = [1, 5, 9, 3, 9, 10]
print(sampleList)

sampleList.append(4)
print(sampleList)
sampleList.append(45)
print(sampleList)
sampleList.pop()
print(sampleList)


def hello():
    print("this is a function to say hello")


hello()


summary = lambda a, b: a + b

print(summary(3, 8))
