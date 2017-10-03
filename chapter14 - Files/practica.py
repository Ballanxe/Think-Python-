import os

# def walk(dirname):
#     """Finds the names of all files in dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     names = []
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             names.append(path)
#         else:
#             names.extend(walk(path))
#     return names

# print walk('../..')

def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.

    filename: string
    """
    cmd = 'md5sum ' + filename
    return pipe(cmd)

def pipe(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat