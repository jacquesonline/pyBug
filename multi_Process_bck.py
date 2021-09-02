#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os


def run(proc_dir):
  # Do something with task here
  # Linux
  # subprocess.call(["rsync", "-arq", src, dest])
    backup_dir = "C:\\Go_backup"
    subprocess.call(["robocopy", proc_dir, proc_dir.replace(
        ".", backup_dir), "/S"])
    print("Backing up {}".format(proc_dir))


if __name__ == "__main__":

    proc_dirs = []
    os.chdir("C:\\Go")

    for root, dirs, files in os.walk(".", topdown=True):
        for name in dirs:
            proc_dirs.append(os.path.join(root, name))

    # Create a pool of specific number of CPUs
    p = Pool(len(proc_dirs))
    # Start each task within the pool
    p.map(run, proc_dirs)

# Driver function
