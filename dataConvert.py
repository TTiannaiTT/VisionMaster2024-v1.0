#Func: 修改rm数据集中常见的四点坐标形式为YOLO中的常见pose数据格式
#可参考YOLO的example中的coco数据集的格式
#"特别提醒":一定要小心数据集的格式和顺序，尤其是排列顺序会影响对称性，这里要和flip_idx对应上！或者可能不涉及对称性）
#格式： 分类类别 * 1 + 矩形坐标(x,y) * 2 + 关键点坐标（x,y) * 4
#Ref： https://blog.csdn.net/qq_39128381/article/details/132620229

import os
# 定义一个path变量，里面是存着所以需要改的txt文件的文件夹名称
path = r'C:\Users\John\Desktop\test'
# 系统列表出所有path文件夹里面文件的名称 （此操作并不会有序遍历所有文件，因此需要下一条代码排列）
total_txt = os.listdir(path)
# 通过文件名格式前的数字大小按升序排列
total_txt.sort(key=lambda x: int(x.split('.')[0]))

#开始文件操作
# 遍历前面读取的已修改的有序文件
for file in total_txt:
    fileName = path + '/' + file

    file = open(fileName, 'r')  # 打开文件阅读模式
    lines = file.readlines()  # 返回列表形式的内容

    # 以行为单位遍历文件内容（index是行数，line是单行内容）
    for index, line in enumerate(lines):
        strT = lines[index]  # 读取当前行的内容

        if strT[0:2] == "71":  # 切片判断前两个字符
            strT = "2" + strT[2:]  # 改成2加字符第二位往后
            lines[index] = strT  # 改写lines中的内容
            verify = 1  # 验证文件有需要保存的内容

        # 与上述同理
        elif strT[0:2] == "57":
            strT = "3" + strT[2:]
            lines[index] = strT


        # 这里如果没有想要保持的就直接用空代替来写入lines中
        else:
            strT = ''
            lines[index] = strT
    # 然后将读取模式关闭
    file.close()

    # lines列表转换为字符串放在strT中
    strT = "".join(lines)

    # 打开文件写入模式，把更新后的lines写进txt文件中
    file = open(fileName, 'w')
    file.write(strT)
    file.close()


