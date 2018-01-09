##testmultiprocessing
#- * -coding: utf - 8 - * -


from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p1 = Process(target=run_proc, args=('hello',))
    print('Child process will start.')
    p.start()
    p1.start()
    p.join()
    p1.join()
    print('Child process end.')