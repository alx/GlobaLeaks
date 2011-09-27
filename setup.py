#!/usr/bin/env python

from setuptools import setup

import os, glob, fnmatch

from applications import globaleaks
def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

def find_data_files(srcdir, *wildcards, **kw):
    # get a list of all files under the srcdir matching wildcards,
    # returned in a format to be used for install_data
    def walk_helper(arg, dirname, files):
        if '.git' in dirname:
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)

                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                    names.append(filename)
        if names:
            lst.append( (dirname, names ) )

    file_list = []
    recursive = kw.get('recursive', True)
    if recursive:
        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
    else:
        walk_helper((file_list, wildcards),
                    srcdir,
                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
    return file_list

data_files = [('globaleaks',['VERSION'])]
for elem in find_data_files('applications', '*.*'):
    data_files.append((os.path.join("globaleaks", elem[0]), elem[1]))

packages = ['globaleaks']

setup(name=globaleaks.__name__,
      version=globaleaks.__version__,
      description='The Opensource Whistleblowing Framework',
      author=globaleaks.__authors__,
      author_email=globaleaks.__email__,
      url=globaleaks.__site__,
      install_requires=['web2py'],
      package_dir={'globaleaks': ''},
      packages=packages,
      data_files=data_files,
      scripts=['startglobaleaks'],
     )
