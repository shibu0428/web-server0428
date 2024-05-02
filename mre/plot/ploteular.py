import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ffmpeg


def update(frame, ax, angles, trace_lines):
    ax.cla()
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([-1, 1])

    angle = angles[frame]

    # オイラー角を使って回転行列を作成
    rotation_matrix = euler_to_rotation_matrix(angle)

    # 単位ベクトル
    unit_vector = np.array([1, 0, 0])

    # 回転後のベクトル
    rotated_vector = np.dot(rotation_matrix, unit_vector)

    # 3Dプロット
    ax.quiver(0, 0, 0, rotated_vector[0], rotated_vector[1], rotated_vector[2], color='r')

    # 軌跡を描く
    trace_lines.append((rotated_vector[0], rotated_vector[1], rotated_vector[2]))
    trace_xs, trace_ys, trace_zs = zip(*trace_lines)
    ax.plot(trace_xs, trace_ys, trace_zs, color='b', linewidth=1, alpha=0.5)

def euler_to_rotation_matrix(angle):
    roll, pitch, yaw = angle
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(roll), -np.sin(roll)],
                   [0, np.sin(roll), np.cos(roll)]])
    
    Ry = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                   [0, 1, 0],
                   [-np.sin(pitch), 0, np.cos(pitch)]])
    
    Rz = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                   [np.sin(yaw), np.cos(yaw), 0],
                   [0, 0, 1]])
    
    rotation_matrix = np.dot(Rz, np.dot(Ry, Rx))
    return rotation_matrix

def read_file(file_path):
    data_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # 行からスペースまたはタブで区切られたデータを取得し、floatに変換してリストに追加
            data_list.append(list(map(float, line.strip().split())))

    # NumPyのarrayに変換
    data_2d_array = np.array(data_list)
    return data_2d_array

def main():
    # オイラー角のリストをユーザーに対話的に入力
    filename=input("input file name->")
    data_list=read_file(filename)
    
    num_frames = len(data_list)
    angles = []
    trace_lines = []  # 新たに軌跡の座標を保存するリストを作成
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(num_frames):
        input_values = data_list[i]
        #print(input_values)
        values_list = input_values#.split()
        # 文字列を浮動小数点数に変換
        float_values = [float(value) for value in values_list]
        # roll = np.radians(float_values[0])
        # pitch = np.radians(float_values[1])
        # yaw = np.radians(float_values[2])
        roll = float_values[0]
        pitch = float_values[1]
        yaw = float_values[2]

        angles.append([roll, pitch, yaw])

    ani = FuncAnimation(fig, update, frames=len(angles), fargs=(ax, angles, trace_lines), interval=100, repeat=True)
    plt.show()
    outmp4=input("mp4 save input file name\n")
    ani.save(outmp4, writer="ffmpeg")
if __name__ == "__main__":
    main()
