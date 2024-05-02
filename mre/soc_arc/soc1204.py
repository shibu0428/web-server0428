import socket
import time
import struct
import binascii
bone_map = [
    "Hips", #0
    "Spine", #1
    None, #2
    "Chest", #3
    None, #4
    "UpperChest", #5
    None, #6
    "-", #7
    "-", #8
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
target_id = [
    0,#"Hips"
    10,#"Head"
    14,#"RightHand"
    18,#"LeftHand"
    21,#"RightFoot"
    25#"LeftFoot"
]

dof_parts=7 #つかうデータ=0,1,2,3==クォータニオン->dof=4
            #5,6,7=position->dof=8

host = ''
port = 52350

outfile=input("output file neme?")

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((host, port))

# 受信用のバッファーサイズを設定
buffer_size = 8192

print(f"UDP 受信開始。ホスト: {host}, ポート: {port}")
start_time = time.time()
sum=0
n=0
flag=0
ijou_time=time.time()
last_time = time.time()
while True:
    try:
        # データを受信
        data, addr = udp_socket.recvfrom(buffer_size)
        
        if(len(data)>1600):raise Exception()
        if time.time()-last_time > 1:
            print("データ入力開始")
            if n>0:
                flag=flag+1
            #print(flag)
        
        with open(outfile+str(flag)+'.txt', mode='a') as f:
            bnid_list = data.split(b'bnid')[1:]
            for id,part in enumerate(bnid_list):
                #if id not in target_id:
                #    continue
                tran_btdt_data = part.split(b'tran')[1:]
                dofdata = tran_btdt_data[0].split(b'btdt')[0]
                if len(dofdata) > 28:
                    dofdata=dofdata[:28]
                for id,i in enumerate(range(0, 28, 4)):
                    float_value = struct.unpack('<f', dofdata[i:i+4])
                    if id<dof_parts:
                        f.write(f"{float_value[0]} ")
            f.write(f"\n")
            f.close()
        end_time = time.time()
        n=n+1
        last_time = time.time()
    except OSError as e:
        # エラーが発生した場合は表示
        print(f"エラー: {e}")
    except Exception:
        continue
