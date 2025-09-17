import math
res = width, height = 1600, 900
halfWidth = width / 2
halfHeight = height / 2
fps = 60
playerPOS = 1.5, 5
playerAngle = 0
playerSpeed = 0.004
playerROTspeed = 0.002
fullFOV = math.pi / 12
halfFOV = fullFOV / 2
numRays = int(width // 2)
halfNumRays = numRays / 2
deltaAngle = fullFOV / numRays
maxDepth = 20 
screenDist = halfWidth / math.tan(halfFOV)
scale = width // numRays
textureSize = 256
halfTextureSize = 128