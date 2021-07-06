import os
import sys
import datetime

# 读取索引文件存放列表
tlist = []


# 读取剪切索引文件
def read_txt(fp):
    f = open(fp,'rb')
    for line in f.readlines():
        line = str(line, "utf-8")
        tlist.append(tuple(line.split()))
    f.close  


# 时间格式转换
def convert(num):
    s1 = str(num)
    return ":".join([s1[0:2], s1[2:4], s1[4:6]])


# 剪切核心函数
def cut(cut_time_file_path):
    read_txt(cut_time_file_path)
    file_path = tlist[0][0] # 剪切文件位置
    file_name = tlist[1][0] # 剪切文件名称
    print(file_path)
    print(file_name)
    file_type = file_name.split(".")[1] # 文件类型
    count = 1   # 没有命名的计数
    for i in range(2,len(tlist)):
        t1 = convert(tlist[i][0])
        t2 = convert(tlist[i][1])
        try:
            t3 = str(tlist[i][2])
        except IndexError:
            t3 = datetime.datetime.now().strftime("%Y-%m-%d") +"-未命名-" + str(count)
            count += 1

        cmd_str = "ffmpeg -i %s -vcodec copy -acodec copy -ss %s -to %s  %s -y" \
                    % ("\"" + file_path + "\\" + file_name + "\"", t1, t2, "\"" + file_path + "\\"  + t3+"."+file_type + "\"")
        p = os.popen(cmd_str)
    p.close


if __name__ == "__main__":
    try:
        cut(sys.argv[1])
    except IndexError:
        print("请输入剪切索引文件地址")