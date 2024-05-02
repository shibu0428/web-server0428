import numpy as np
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 四元数を使って座標を回転させる関数
def rotate_coordinates(quaternion, original_coordinates):
    rotation_matrix = Rotation.from_quat(quaternion).as_matrix()
    original_coordinates = np.array(original_coordinates).reshape(-1, 1)
    rotated_coordinates = np.dot(rotation_matrix, original_coordinates)
    return rotated_coordinates.flatten()

# 骨格の各関節のグローバル位置を計算する関数
def calculate_global_positions(quaternions, coordinates, parent_path):
    global_positions = np.zeros((27, 3))  # 27関節分の座標を初期化

    for i in range(len(quaternions)):
        # 回転の適用
        rotated_position = rotate_coordinates(quaternions[i], coordinates[i])
        if i != 0:
            # 親関節のグローバル座標に相対座標を加算
            parent_index = parent_path[i]
            global_positions[i] = global_positions[parent_index] + rotated_position
        else:
            # 根関節はそのままグローバル座標を設定
            global_positions[i] = rotated_position

    return global_positions

# 3Dプロットを行う関数
def plot_3d_skeleton(global_positions, parent_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 関節点をプロット
    ax.scatter(global_positions[:, 0], global_positions[:, 1], global_positions[:, 2], color='red')

    # 親子関係に基づいて線で結ぶ
    for i, parent_index in enumerate(parent_path):
        if i != parent_index:
            ax.plot([global_positions[i][0], global_positions[parent_index][0]],
                    [global_positions[i][1], global_positions[parent_index][1]],
                    [global_positions[i][2], global_positions[parent_index][2]], color='blue')

    # 軸のアスペクト比を等しく設定
    ax.set_aspect('equal')

    # 軸ラベル設定
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # 表示
    plt.show()
def read_input():
    quaternions = []
    coordinates = []

    # 27関節分のデータを一行で読み込む
    data = list(map(float, input().split()))
    for i in range(27):
        quaternion = data[i * 7:(i * 7) + 4]
        coordinate = data[(i * 7) + 4:(i * 7) + 7]
        quaternions.append(quaternion)
        coordinates.append(coordinate)

    return quaternions, coordinates
# メイン関数
def main():
    quaternions, coordinates = read_input()
    parent_path = [0,0,1,2,3,4,5,6,7,8,9,7,11,12,13,7,15,16,17,0,19,20,21,0,23,24,25]

    # 骨格の各関節のグローバル位置を計算
    global_positions = calculate_global_positions(quaternions, coordinates, parent_path)

    # 3Dプロットを行う
    plot_3d_skeleton(global_positions, parent_path)
if __name__ == "__main__":
    main()
