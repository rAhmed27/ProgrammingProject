import math
res = width, height = 1600, 900
halfWidth = width / 2
halfHeight = height / 2
fps = 60
playerPOS = 1.5, 5
playerAngle = 0
playerSpeed = 0.004
playerROTspeed = 0.002
playerScaleSize = 60
mouseSensitivity = 0.0003
mouseMaxRel = 40
mouseLeftBorder = 100
mouseRightBorder = width - mouseLeftBorder
floorColour = (30, 30, 30)
fullFOV = math.pi / 5
halfFOV = fullFOV / 2
numRays = int(width // 2)
halfNumRays = numRays / 2
deltaAngle = fullFOV / numRays
maxDepth = 20 
screenDist = halfWidth / math.tan(halfFOV)
scale = width // numRays
textureSize = 256
halfTextureSize = 128