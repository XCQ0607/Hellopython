import os
import time
#os模块是一个与操作系统交互的模块，提供了许多与操作系统相关的功能，如文件和目录操作、进程管理、环境变量操作等。



def main(deleteflag=0):
    # 获取当前工作目录
    current_dir = os.getcwd()     #os.getcwd() 函数用于获取当前工作目录的路径。全称get current working directory
    print(f"当前工作目录: {current_dir}")

    # 创建一个新目录
    new_dir = os.path.join(current_dir, "test_dir")   #os.path.join() 函数用于将多个路径组合成一个路径。参数：第一个参数是目标目录的路径，后面的参数是要组合的路径。这里只是将当前目录和test_dir组合成一个路径，但是并没有创建这个目录。test_dir是当前目录的子目录。
    os.makedirs(new_dir, exist_ok=True)   #makedirs() 函数用于递归创建目录。参数：第一个参数是要创建的目录的路径
    # exist_ok=True表示如果目录已经存在，不会抛出异常
    print(f"创建新目录: {new_dir}")

    # 更改当前工作目录
    os.chdir(new_dir)     #chdir() 函数用于更改当前工作目录。参数：第一个参数是要更改的目录的路径
    print(f"更改当前工作目录到: {os.getcwd()}")

    # 创建一个新文件并写入内容
    file_path = os.path.join(new_dir, "test_file.txt")
    with open(file_path, "w") as f:
        f.write("Hello, World!")
    print(f"创建并写入文件: {file_path}")

    # 读取文件内容
    with open(file_path, "r") as f:
        content = f.read()
    print(f"文件内容: {content}")

    # 获取文件信息
    file_stat = os.stat(file_path)   #stat() 函数用于获取文件的状态信息。参数：第一个参数是要获取状态信息的文件的路径
    print(f"文件大小: {file_stat.st_size} 字节")
    print(f"最后修改时间: {time.ctime(file_stat.st_mtime)}")

    #查看当前文件权限
    print(f"文件权限: {oct(os.stat(file_path).st_mode)[-3:]}")      #这里[-3:] 表示取最后三个字符，因为文件权限是八进制数，所以需要取最后三个字符。666表示文件所有者有读写权限，文件所属组和其他用户有读权限。
    #oct() 函数用于将一个整数转换为八进制字符串。参数：第一个参数是要转换的整数

    # 修改文件权限
    os.chmod(file_path, 0o644)   #chmod() 函数用于更改文件的权限。参数：第一个参数是要更改权限的文件的路径，第二个参数是要设置的权限
    #权限格式：0o是八进制数的前缀，644表示文件所有者有读写权限，文件所属组和其他用户有读权限。
    print("修改文件权限为 644")

    # 重命名文件--更改文件名
    new_file_path = os.path.join(new_dir, "renamed_file.txt")     # 新的文件路径
    try:
        os.rename(file_path, new_file_path) # 重命名文件，参数：第一个参数是要重命名的文件的路径，第二个参数是新的文件路径
    except FileExistsError:
        os.remove(new_file_path)
        os.rename(file_path, new_file_path)
    print(f"重命名文件: {file_path} -> {new_file_path}")

    # 创建符号链接
    link_path = os.path.join(new_dir, "symlink")
    try:
        os.symlink(new_file_path, link_path)     #symlink() 函数用于创建符号链接。参数：第一个参数是要创建的符号链接的路径，第二个参数是要链接的文件的路径
    except FileExistsError:              #IndentationError 是一个异常类，用于表示缩进错误,全部错误的父类是Exception
        os.remove(link_path)
        os.symlink(new_file_path, link_path)
    print(f"创建符号链接: {link_path} -> {new_file_path}")
    # 删除符号链接
    #这个remove和unlink一样
    #os.unlink(link_path)

    # 获取链接指向的文件
    print(f"符号链接指向: {os.readlink(link_path)}")

    # 列出目录内容
    print("目录内容:")
    for item in os.listdir(new_dir):    #listdir() 函数用于列出目录中的文件和子目录。参数：第一个参数是要列出的目录的路径
        print(f"  {item}")

    # 递归遍历目录
    print("递归遍历目录:")
    for root, dirs, files in os.walk(new_dir):  #walk() 函数用于递归遍历目录。参数：第一个参数是要遍历的目录的路径
        for name in files:    #files是一个列表，包含了当前目录中的所有文件
            print(f"  文件: {os.path.join(root, name)}")  #这里给的name是相对路径，所以需要用os.path.join()函数将root和name拼接起来，得到绝对路径
        for name in dirs:     #dirs是一个列表，包含了当前目录中的所有子目录
            print(f"  目录: {os.path.join(root, name)}")

    # 获取文件系统信息
    if os.name == 'posix':
        # Unix系统
        fs_stat = os.statvfs(new_dir)  #statvfs() 函数用于获取文件系统的信息。参数：第一个参数是要获取信息的文件系统的路径
        print(f"文件系统总大小: {fs_stat.f_frsize * fs_stat.f_blocks / (1024*1024*1024):.2f} GB")
        print(f"可用空间: {fs_stat.f_frsize * fs_stat.f_bavail / (1024*1024*1024):.2f} GB")
    elif os.name == 'nt':
        # Windows系统
        import shutil
        fs_stat = shutil.disk_usage(new_dir)
        total_size_gb = fs_stat.total / (1024 * 1024 * 1024)
        free_size_gb = fs_stat.free / (1024 * 1024 * 1024)
        print(f"文件系统总大小: {total_size_gb:.2f} GB")
        print(f"可用空间: {free_size_gb:.2f} GB")

    #此时的文件目录结构
    # test_dir  3.使用代码删除：os.rmdir(new_dir)  rmdir() 函数用于递归删除目录。参数：第一个参数是要删除的目录的路径
    # ├── renamed_file.txt  1.使用代码删除：os.remove(new_file_path)
    # └── symlink -> renamed_file.txt   2.使用代码删除：os.unlink(link_path)

    # 删除文件和目录(要有顺序，先删除文件，再删除目录)
    if deleteflag:
        print("删除文件和目录")
        os.remove(new_file_path)  # remove() 函数用于删除文件。参数：第一个参数是要删除的文件的路径
        os.remove(link_path)
        os.chdir(current_dir)  # chdir() 函数用于更改当前工作目录。参数：第一个参数是要更改的目录的路径
        os.rmdir(new_dir)  # rmdir() 函数用于删除目录。参数：第一个参数是要删除的目录的路径

if __name__ == "__main__":
    deleteflag=0
    main(deleteflag)
