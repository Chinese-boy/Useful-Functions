import traceback, os


def list_files(top):
    for path, dirs, files in os.walk(top):
        for name in files:
            yield os.path.join(path, name)


def cp_file(one, other):
    length = 30
    # 打开文件
    one_file = open(one, "rb")
    other_file = open(other, "wb")

    # 获取大小
    one_size = os.path.getsize(one)

    # 已复制长度
    num = 0
    # 每次读取1MB，然后写入1MB
    print("正在把 %s 复制到 %s ……" % (os.path.split(one)[1], os.path.split(other)[1]))
    while True:
        write_bytes = one_file.read(1024 * 1024)
        other_file.write(write_bytes)
        num += len(write_bytes)
        try:
            x = int(num / one_size * length)
        except ZeroDivisionError:
            x = length
        try:
            y = int(num / one_size * 100)
        except ZeroDivisionError:
            y = 100
        print("{}{}|已完成{:.2f}%".format("#" * x, " " * (length - x), y), end="\r")
        if len(write_bytes) < 1024 * 1024:
            break
    print("\n复制完成！")

    # 打开文件后别忘记关掉文件
    one_file.close()
    other_file.close()


def mv_file(one, other):
    length = 30
    # 打开文件
    one_file = open(one, "rb")
    other_file = open(other, "wb")

    # 获取大小
    one_size = os.path.getsize(one)

    # 已复制长度
    num = 0
    # 每次读取1MB，然后写入1MB
    print("正在把 %s 移动到 %s ……" % (os.path.split(one)[1], os.path.split(other)[1]))
    while True:
        write_bytes = one_file.read(1024 * 1024)
        other_file.write(write_bytes)
        num += len(write_bytes)
        x = int(num / one_size * length)
        print("{}{}|已完成{:.2f}%".format("#" * x, " " * (length - x), num / one_size * 100), end="\r")
        if len(write_bytes) < 1024 * 1024:
            break

    # 打开文件后别忘记关掉文件
    one_file.close()
    other_file.close()

    os.remove(one)
    print("\n移动完成！")


def cp_dir(one, other):
    if one[-1] == os.sep:
        one_parent_dir = one[:]
    else:
        one_parent_dir = one[:] + os.sep

    if other[-1] == os.sep:
        other_parent_dir = other[:]
    else:
        other_parent_dir = other[:] + os.sep
    print(other_parent_dir)

    for name in list_files(one):
        x = "".join(name.split(one_parent_dir)[1:])
        try:
            mk_dir = os.path.split(x)[0]
            os.makedirs("%s%s" % (other_parent_dir, mk_dir))
        except:
            pass
        cp_file("%s%s" % (one_parent_dir, x), "%s%s" % (other_parent_dir, x))