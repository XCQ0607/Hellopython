import os
import time

def main():
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")

    # 创建一个新目录
    new_dir = os.path.join(current_dir, "test_dir")
    os.makedirs(new_dir, exist_ok=True)
    print(f"创建新目录: {new_dir}")

    # 更改当前工作目录
    os.chdir(new_dir)
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
    file_stat = os.stat(file_path)
    print(f"文件大小: {file_stat.st_size} 字节")
    print(f"最后修改时间: {time.ctime(file_stat.st_mtime)}")

    # 修改文件权限
    os.chmod(file_path, 0o644)
    print("修改文件权限为 644")

    # 重命名文件
    new_file_path = os.path.join(new_dir, "renamed_file.txt")
    os.rename(file_path, new_file_path)
    print(f"重命名文件: {file_path} -> {new_file_path}")

    # 创建符号链接
    link_path = os.path.join(new_dir, "symlink")
    os.symlink(new_file_path, link_path)
    print(f"创建符号链接: {link_path} -> {new_file_path}")
    # 删除符号链接
    #这个remove和unlink一样
    #os.unlink(link_path)

    # 获取链接指向的文件
    print(f"符号链接指向: {os.readlink(link_path)}")

    # 列出目录内容
    print("目录内容:")
    for item in os.listdir(new_dir):
        print(f"  {item}")

    # 递归遍历目录
    print("递归遍历目录:")
    for root, dirs, files in os.walk(new_dir):
        for name in files:
            print(f"  文件: {os.path.join(root, name)}")
        for name in dirs:
            print(f"  目录: {os.path.join(root, name)}")

    # 获取文件系统信息
    fs_stat = os.statvfs(new_dir)
    print(f"文件系统总大小: {fs_stat.f_frsize * fs_stat.f_blocks / (1024*1024*1024):.2f} GB")
    print(f"可用空间: {fs_stat.f_frsize * fs_stat.f_bavail / (1024*1024*1024):.2f} GB")

    # 删除文件和目录
    os.remove(new_file_path)
    os.remove(link_path)
    os.chdir(current_dir)
    os.rmdir(new_dir)
    print("删除文件和目录")

if __name__ == "__main__":
    main()