"""find duplicate files in directory tree
"""

import os

def walkdir(dirname):
    names = []

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walkdir(path))
            
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + "'" + filename + "'"
    fp = os.popen(cmd)
    res = fp.read()
    fp.close()
    return res.split('*')[0].strip()


def compute_checksums(dirname, suffix):
    names = walkdir(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            checksum = compute_checksum(name)
            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]
                
    return d

def print_duplicates(d):
    for key, names in d.items():
        if len(names) > 1:
            for name in names:
                print(name)

                
if __name__ == '__main__':
    d = compute_checksums('.', '.py')
    print(d)
    print_duplicates(d)
