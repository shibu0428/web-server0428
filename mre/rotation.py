import numpy as np
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plt

def rotate_coordinates(quaternion, original_coordinates):
    # 四元数を回転行列に変換
    rotation_matrix = Rotation.from_quat(quaternion).as_matrix()
    
    # 座標を列ベクトルに変換
    original_coordinates = np.array(original_coordinates).reshape(-1, 1)
    
    # 回転後の座標を計算
    rotated_coordinates = np.dot(rotation_matrix, original_coordinates)
    
    # 結果を1次元配列に戻す
    rotated_coordinates = rotated_coordinates.flatten()
    
    return rotated_coordinates
row=1
col=27*7
in_val=[]
#親情報のnode位置　0の親はなし 1の親は0
parent_path=[26,0,1,2,3,4,5,6,7,8,9,7,11,12,13,7,15,16,17,0,19,20,21,0,23,24,25]
for i in range(row):
    row_input = input()
    row_values = list(map(float, row_input.split()))
    in_val.append(row_values)
data = np.array(in_val)
print(data.shape)
xyzold=[0.0,0.0,0.0]
plotdata=np.zeros((27, 3))
i=0#0データ目を処理　のちを考えて添え字化
plotdata[0]=data[0][4:7]
for j in range(0,27):
    quat=[data[i][7*int(parent_path[j])],data[i][7*int(parent_path[j])+1],data[i][7*int(parent_path[j])+2],data[i][7*int(parent_path[j])+3]]
    xyz=[data[i][7*j+4],data[i][7*j+5],data[i][7*j+6]]
    if j!=0:plotdata[j]=rotate_coordinates(quat, xyz)+plotdata[parent_path[j]]
    #else : plotdata[j]=rotate_coordinates(quat, xyz)
i=0
j=27
quat=[data[i][7*j-7],data[i][7*j-6],data[i][7*j-5],data[i][7*j-4]]
xyz=[data[i][4],data[i][5],data[i][6]]
plotdata[0]=rotate_coordinates(quat, xyz)
np.set_printoptions(suppress=True)
print(plotdata)
np.set_printoptions(suppress=False)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(plotdata[0, 0], plotdata[0, 1], plotdata[0, 2], color='red')
ax.scatter(plotdata[1:10, 0], plotdata[1:10, 1], plotdata[1:10, 2], color='blue')
ax.scatter(plotdata[10, 0], plotdata[10, 1], plotdata[10, 2], color='red')
ax.scatter(plotdata[11:14, 0], plotdata[11:14, 1], plotdata[11:14, 2], color='blue')
ax.scatter(plotdata[14, 0], plotdata[14, 1], plotdata[14, 2], color='green')
ax.scatter(plotdata[15:18, 0], plotdata[15:18, 1], plotdata[15:18, 2], color='blue')
ax.scatter(plotdata[18, 0], plotdata[18, 1], plotdata[18, 2], color='green')
ax.scatter(plotdata[19:22, 0], plotdata[19:22, 1], plotdata[19:22, 2], color='blue')
ax.scatter(plotdata[22, 0], plotdata[22, 1], plotdata[22, 2], color='green')
ax.scatter(plotdata[23:26, 0], plotdata[23:26, 1], plotdata[23:26, 2], color='blue')
ax.scatter(plotdata[26, 0], plotdata[26, 1], plotdata[26, 2], color='green')


for i in range(10):
    ax.plot([plotdata[i, 0], plotdata[i+1, 0]], [plotdata[i, 1], plotdata[i+1, 1]], [plotdata[i, 2], plotdata[i+1, 2]], color='black', linewidth=1)
for i in range(11,14):
    ax.plot([plotdata[i, 0], plotdata[i+1, 0]], [plotdata[i, 1], plotdata[i+1, 1]], [plotdata[i, 2], plotdata[i+1, 2]], color='black', linewidth=1)
for i in range(15,18):
    ax.plot([plotdata[i, 0], plotdata[i+1, 0]], [plotdata[i, 1], plotdata[i+1, 1]], [plotdata[i, 2], plotdata[i+1, 2]], color='black', linewidth=1)
for i in range(19,22):
    ax.plot([plotdata[i, 0], plotdata[i+1, 0]], [plotdata[i, 1], plotdata[i+1, 1]], [plotdata[i, 2], plotdata[i+1, 2]], color='black', linewidth=1)
for i in range(23,26):
    ax.plot([plotdata[i, 0], plotdata[i+1, 0]], [plotdata[i, 1], plotdata[i+1, 1]], [plotdata[i, 2], plotdata[i+1, 2]], color='black', linewidth=1)

ax.plot([plotdata[7, 0], plotdata[11, 0]], [plotdata[7, 1], plotdata[11, 1]], [plotdata[7, 2], plotdata[11, 2]], color='black', linewidth=1)
ax.plot([plotdata[7, 0], plotdata[15, 0]], [plotdata[7, 1], plotdata[15, 1]], [plotdata[7, 2], plotdata[15, 2]], color='black', linewidth=1)
ax.plot([plotdata[0, 0], plotdata[19, 0]], [plotdata[0, 1], plotdata[19, 1]], [plotdata[0, 2], plotdata[19, 2]], color='black', linewidth=1)
ax.plot([plotdata[0, 0], plotdata[23, 0]], [plotdata[0, 1], plotdata[23, 1]], [plotdata[0, 2], plotdata[23, 2]], color='black', linewidth=1)


ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])
plt.savefig("rot.png")
plt.show()