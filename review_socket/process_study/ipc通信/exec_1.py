import multiprocessing as mp
import time,os
'''
os.mkdir(path)，他的功能是一级一级的创建目录，前提是前面的目录已存在，如果不存在会报异常，比较麻烦，但是存在即有他的道理，当你的目录是根据文件名动态创建的时候，你会发现他虽然繁琐但是很有保障，不会因为你的一时手抖，创建而创建了双层或者多层错误路径，

os.makedirs(path),单从写法上就能猜出他的区别，他可以一次创建多级目录，哪怕中间目录不存在也能正常的（替你）创建，想想都可怕，万一你中间目录写错一个单词.........
'''

q = mp.Queue()
def copy_file(file,old_folder,new_folder):
    fr = open(old_folder + '/' + file,'rb+')
    fw = open(new_folder + '/' + file,'wb+')
    #拷贝
    while True:
        data = fr.read()
        if not data:
            break
        n = fw.write(data)
        q.put(n)
    fw.close()
    fr.close()

def main():
    base_folder = '/home/tarena/测试/review_socket/process_study/ipc通信/'
    dir  = input('请输入要拷贝的目录')
    dir = "test_folder"
    old_folder = base_folder + dir
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)
    all_files = os.listdir(old_folder)
    # print(all_files)
    total_size = 0
    for file in all_files:
        total_size += os.path.getsize(old_folder+"/"+file)
    # print('文件目录大小是%.2fM'%(total_size/1024/1024))
    print('文件目录大小是%.2fKb'%(total_size))
    # 进程池部分
    pool = mp.Pool()
    for file in all_files:
        pool.apply_async(copy_file,args=(file,old_folder,new_folder))
    pool.close()
    copy_size = 0
    while True:
        copy_size += q.get()
        print('拷贝了%.2f %%的文件'%(copy_size/total_size*100))
        if copy_size >= total_size:
            break
    pool.join()

if __name__ == '__main__':
    main()








