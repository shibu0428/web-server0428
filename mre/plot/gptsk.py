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

# 骨格の姿勢を変換する関数
def transform_skeleton(quaternions, coordinates, parent_path):
    transformed_coordinates = [np.zeros(3)] * 27  # 27関節分の座標を初期化

    for i, (quaternion, coordinate) in enumerate(zip(quaternions, coordinates)):
        rotated_coordinate = rotate_coordinates(quaternion, coordinate)
        parent_index = parent_path[i]
        if i != parent_index:  # 根関節以外
            rotated_coordinate += transformed_coordinates[parent_index]
        transformed_coordinates[i] = rotated_coordinate

    return transformed_coordinates

# 3Dプロットを行う関数
def plot_3d_skeleton(coordinates, parent_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 親子関係に基づいて線で結ぶ
    for i, parent_index in enumerate(parent_path):
        if i != parent_index:  # 自分自身とは線を結ばない
            ax.plot([coordinates[i][0], coordinates[parent_index][0]],
                    [coordinates[i][1], coordinates[parent_index][1]],
                    [coordinates[i][2], coordinates[parent_index][2]], color='blue')

    # 座標点をプロット
    for coordinate in coordinates:
        ax.scatter(coordinate[0], coordinate[1], coordinate[2], color='red')

    # 軸ラベル設定
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # 表示
    plt.show()

# 標準入力から一行で四元数と座標のデータを読み込む関数
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

# メインの実行部分
def main():
    quaternions, coordinates = read_input()
    parent_path = [0,0,1,2,3,4,5,6,7,8,9,7,11,12,13,7,15,16,17,0,19,20,21,0,23,24,25]
    transformed_skeleton = transform_skeleton(quaternions, coordinates, parent_path)
    plot_3d_skeleton(transformed_skeleton, parent_path)

if __name__ == "__main__":
    main()
