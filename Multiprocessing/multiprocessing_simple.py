import os
import torch.multiprocessing as mp # Identical in usage to base Python multiprocessing but works better with torch tensors

os.environ['SET_NUM_THREADS'] = '1'

def worker(name):
    print('Hello', name)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    process = mp.Process(target=worker, args=('Adam',))
    process.start()
    process.join()