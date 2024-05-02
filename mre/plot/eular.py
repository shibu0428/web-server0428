import numpy as np
from scipy.spatial.transform import Rotation

target_id = ["Hips","Head","RightHand","LeftHand","RightFoot","LeftFoot"]
input_file = input("input file name->")
output_file = input("output file name->")

def quaternion_to_euler(q):
    # クォータニオンをRotationオブジェクトに変換
    r = Rotation.from_quat(q)
    # Rotationオブジェクトをオイラー角に変換
    euler_angles = r.as_euler('xyz', degrees=False)
    
    return euler_angles


# ファイルを読み込んでデータを多次元配列に格納する関数
def read_file_to_2d_array(file_path):
    data_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # 行からスペースまたはタブで区切られたデータを取得し、floatに変換してリストに追加
            data_list.append(list(map(float, line.strip().split())))

    # NumPyのarrayに変換
    data_2d_array = np.array(data_list)

    return data_2d_array

# ファイルを読み込んで多次元配列に格納
data_2d_array = read_file_to_2d_array(input_file)
print("データサイズは")
print(data_2d_array.shape)

for flamedata in data_2d_array:
    for i in range(len(target_id)):
        quaternion=flamedata[i*4:i*4+4]
        euler_angles = quaternion_to_euler(quaternion)
        with open(output_file+target_id[i]+'.txt', mode='a') as f:
            f.write(str(euler_angles[0]))
            f.write(' ')
            f.write(str(euler_angles[1]))
            f.write(' ')
            f.write(str(euler_angles[2]))
            f.write(f"\n")
            f.close()