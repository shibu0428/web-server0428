import matplotlib.pyplot as plt
import numpy as np

xyz = np.zeros((27, 3))

xyz[0][0:3]=[0.26090434193611145,0.9489158987998962,-0.43941739201545715]#Hip
xyz[1][0:3]=[0.0,0.0522545650601387,-0.011846553534269333]
xyz[2][0:3]=[0.0,0.05778944492340088,0.011023926548659801]
xyz[3][0:3]=[-1.0556978516943539e-19,0.06162893399596214,0.0011833360185846686]
xyz[4][0:3]=[-1.1364889052398349e-19,0.06693855673074722,-0.004563413094729185]
xyz[5][0:3]=[-2.0299702410874898e-19,0.07825291156768799,-0.015494492836296558]
xyz[6][0:3]=[-2.6062770551168997e-19,0.09771855920553207,-0.009409227408468723]
xyz[7][0:3]=[-2.9879387067367495e-19,0.10856296122074127,0.01622484251856804]
xyz[8][0:3]=[-1.329268258380205e-19,0.04924779385328293,0.007360131945461035]
xyz[9][0:3]=[-1.8639612960026913e-19,0.04960425943136215,0.004339810460805893]
xyz[10][0:3]=[-2.0676638276257656e-19,0.04970017448067665,0.007871733978390694]
xyz[11][0:3]=[0.012686271220445633,-0.07827169448137283,0.07751482725143433]
xyz[12][0:3]=[0.13329128921031952,0.0334341898560524,-0.03363192453980446]
xyz[13][0:3]=[0.30052241683006287,0.0006153663853183389,0.0014099966501817107]
xyz[14][0:3]=[0.24934355914592743,0.0005105607560835779,0.0011698761954903603]
xyz[15][0:3]=[-0.012686271220445633,-0.07827155292034149,0.07751383632421494]
xyz[16][0:3]=[-0.13329128921031952,0.0334341898560524,-0.03363192453980446]
xyz[17][0:3]=[-0.30052241683006287,0.0006153663853183389,0.0014099966501817107]
xyz[18][0:3]=[-0.24934355914592743,0.0005105590680614114,0.0011698773596435785]
xyz[19][0:3]=[0.09503691643476486,-0.04327109456062317,0.02091449685394764]
xyz[20][0:3]=[-0.008769872598350048,-0.39892637729644775,-0.006741225253790617]
xyz[21][0:3]=[-0.023934513330459595,-0.4156942367553711,-0.062235672026872635]
xyz[22][0:3]=[0.008016129955649376,-0.10170075297355652,0.12857073545455933]
xyz[23][0:3]=[-0.09503691643476486,-0.04327109456062317,0.02091449685394764]
xyz[24][0:3]=[0.008769872598350048,-0.39892637729644775,-0.006741225253790617]
xyz[25][0:3]=[0.023934513330459595,-0.4156942367553711,-0.062235672026872635]
xyz[26][0:3]=[-0.00801613088697195,-0.10170075297355652,0.12857073545455933]


tbone = np.zeros((27, 3))
tbone[0]=xyz[0]
tbone[1]=xyz[1]+tbone[0]
tbone[2]=xyz[2]+tbone[1]
tbone[3]=xyz[3]+tbone[2]
tbone[4]=xyz[4]+tbone[3]
tbone[5]=xyz[5]+tbone[4]
tbone[6]=xyz[6]+tbone[5]
tbone[7]=xyz[7]+tbone[6]
tbone[8]=xyz[8]+tbone[7]
tbone[9]=xyz[9]+tbone[8]
tbone[10]=xyz[10]+tbone[9]

tbone[11]=xyz[11]+tbone[7]
tbone[12]=xyz[12]+tbone[11]
tbone[13]=xyz[13]+tbone[12]
tbone[14]=xyz[14]+tbone[13]

tbone[15]=xyz[15]+tbone[7]
tbone[16]=xyz[16]+tbone[15]
tbone[17]=xyz[17]+tbone[16]
tbone[18]=xyz[18]+tbone[17]

tbone[19]=xyz[19]+tbone[0]
tbone[20]=xyz[20]+tbone[19]
tbone[21]=xyz[21]+tbone[20]
tbone[22]=xyz[22]+tbone[21]

tbone[23]=xyz[23]+tbone[0]
tbone[24]=xyz[24]+tbone[23]
tbone[25]=xyz[25]+tbone[24]
tbone[26]=xyz[26]+tbone[25]



fig = plt.figure()
ax = fig.add_subplot(projection='3d')



ax.scatter(tbone[0, 0], tbone[0, 1], tbone[0, 2], color='red')
ax.scatter(tbone[1:10, 0], tbone[1:10, 1], tbone[1:10, 2], color='blue')
ax.scatter(tbone[10, 0], tbone[10, 1], tbone[10, 2], color='red')
ax.scatter(tbone[11:14, 0], tbone[11:14, 1], tbone[11:14, 2], color='blue')
ax.scatter(tbone[14, 0], tbone[14, 1], tbone[14, 2], color='green')
ax.scatter(tbone[15:18, 0], tbone[15:18, 1], tbone[15:18, 2], color='blue')
ax.scatter(tbone[18, 0], tbone[18, 1], tbone[18, 2], color='green')
ax.scatter(tbone[19:22, 0], tbone[19:22, 1], tbone[19:22, 2], color='blue')
ax.scatter(tbone[22, 0], tbone[22, 1], tbone[22, 2], color='green')
ax.scatter(tbone[23:26, 0], tbone[23:26, 1], tbone[23:26, 2], color='blue')
ax.scatter(tbone[26, 0], tbone[26, 1], tbone[26, 2], color='green')


for i in range(10):
    ax.plot([tbone[i, 0], tbone[i+1, 0]], [tbone[i, 1], tbone[i+1, 1]], [tbone[i, 2], tbone[i+1, 2]], color='black', linewidth=1)
for i in range(11,14):
    ax.plot([tbone[i, 0], tbone[i+1, 0]], [tbone[i, 1], tbone[i+1, 1]], [tbone[i, 2], tbone[i+1, 2]], color='black', linewidth=1)
for i in range(15,18):
    ax.plot([tbone[i, 0], tbone[i+1, 0]], [tbone[i, 1], tbone[i+1, 1]], [tbone[i, 2], tbone[i+1, 2]], color='black', linewidth=1)
for i in range(19,22):
    ax.plot([tbone[i, 0], tbone[i+1, 0]], [tbone[i, 1], tbone[i+1, 1]], [tbone[i, 2], tbone[i+1, 2]], color='black', linewidth=1)
for i in range(23,26):
    ax.plot([tbone[i, 0], tbone[i+1, 0]], [tbone[i, 1], tbone[i+1, 1]], [tbone[i, 2], tbone[i+1, 2]], color='black', linewidth=1)

ax.plot([tbone[7, 0], tbone[11, 0]], [tbone[7, 1], tbone[11, 1]], [tbone[7, 2], tbone[11, 2]], color='black', linewidth=1)
ax.plot([tbone[7, 0], tbone[15, 0]], [tbone[7, 1], tbone[15, 1]], [tbone[7, 2], tbone[15, 2]], color='black', linewidth=1)
ax.plot([tbone[0, 0], tbone[19, 0]], [tbone[0, 1], tbone[19, 1]], [tbone[0, 2], tbone[19, 2]], color='black', linewidth=1)
ax.plot([tbone[0, 0], tbone[23, 0]], [tbone[0, 1], tbone[23, 1]], [tbone[0, 2], tbone[23, 2]], color='black', linewidth=1)


ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])

plt.show()
'''
bone_map = ["Hips", #0
    "Spine", #1
    "None2", #2
    "Chest", #3
    "None4", #4
    "UpperChest", #5
    "None6", #6
    "-7", #7
    "-8", #8
    "Neck", #9
    "Head", #10
    "RightShoulder", #11
    "RightUpperArm", #12
    "RightLowerArm", #13
    "RightHand", #14
    "LeftShoulder", #15
    "LeftUpperArm", #16
    "LeftLowerArm", #17
    "LeftHand", #18
    "RightUpperLeg", #19
    "RightLowerLeg", #20
    "RightFoot", #21
    "RightToes", #22
    "LeftUpperLeg", #23
    "LeftLowerLeg", #24
    "LeftFoot", #25
    "LeftToes" #26
]
'''