import io
import random

seed = 4864645
maxValue = 10

def streamNumbers(n) -> io.BytesIO:
    global seed
    stream = io.BytesIO()
    random.seed(seed)
    for _ in range(n):
        stream.write((str(random.randint(0, maxValue)) + "\n").encode())
    seed+=1
    return stream

def readStream(stream):
    stream.seek(0)
    liste = []
    for line in stream.readlines():
        #print(line.strip())
        liste.append(int(line.strip()))
    return liste

print(readStream(streamNumbers(10)))