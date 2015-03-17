

import os, shutil
import errno

def mkdir_p(path):
    """
    'mkdir -p' in Python from http://stackoverflow.com/a/11860637/1716869
    It creates all the subfolders till the end folder.
    """
    try:
        # import errno
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def rm_if_exists(path):
    try:
        shutil.rmtree(path)
    except OSError:
        pass


def check_if_path(path, msg='Not valid path'):
    """
    Checks if a path exists.
    If it does, it returns True, otherwise it prints a message (msg) and returns False
    """
    if not(os.path.isdir(path)):
        print(msg)
        return False
    return True


def find_image_type(dirname, fname):
    """
    Accepts a directory and a filename and returns the extension of the image. The image should
    have one of the extensions listed below, otherwise an exception is raised.
    """
    from os.path import splitext
    extensions = {'png', 'jpg', 'gif', 'jpeg'} #can add to this list if required
    try:
        image_type = splitext(fname)[-1][1:] # Assumption that the first element is an image.
    except IOError:
        print('Probably the first element in the folder is not an image, which is required')
        raise
    if image_type in extensions:
        return image_type
    else:
        import imghdr
        try:
            type1 = imghdr.what(dirname + '/' + fname)
        except IOError:
            raise IOError('The file %s does not exist.\n' % (dirname + '/' + fname))
        if type1 in extensions:
            return type1
        else:
            raise ValueError('%s is not supported type (extension) of image' % type1)


def remove_empty_folders(path):
    """
    Accepts a path/directory and removes all empty folders in that path (not the empty ones in the subfolders).
    """
    if not check_if_path(path, 'The path (%s) is not valid.' % path):
        return -1
    sub_folders = os.listdir(path)
    for fol in sub_folders:
        p1 = path + fol + '/'
        if not check_if_path(p1, ''):  # then it is not a folder
            continue
        if len(os.listdir(p1)) == 0:
            print('The folder %s is empty, removing' % fol)
            rm_if_exists(p1)