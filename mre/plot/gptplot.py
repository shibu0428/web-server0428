import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R

# 与えられたデータ
in_val=[]
row=1
col=27*7
#dataを標準入力で受け取り、cutとapendでin_valに格納
for i in range(row):
    row_input = input()
    row_values = list(map(float, row_input.split()))
    in_val.append(row_values)
data = in_val
# 四元数と位置座標を分離
quaternions = np.array((data[0::7]), np.array(data[1::7]), np.array(data[2::7]), np.array(data[3::7]))
positions = np.array((data[4::7]), np.array(data[5::7]), np.array(data[6::7]))

# 四元数による回転を適用
def apply_rotation(quaternions, positions):
    rotated_positions = []
    for i in range(len(quaternions[0])):
        quaternion = quaternions[:, i]
        position = positions[:, i]
        rotation = R.from_quat(quaternion)
        rotated_position = rotation.apply(position)
        rotated_positions.append(rotated_position)
    return np.array(rotated_positions)

rotated_positions = apply_rotation(quaternions, positions)

# 回転後の座標をプロット
def plot_joints(joints):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(joints[:, 0], joints[:, 1], joints[:, 2])

    plt.show()
   
plot_joints(rotated_positions)