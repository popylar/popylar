import os
import uuid
from setuptools import setup, find_packages
PACKAGES = find_packages()

ver_file = os.path.join('popylar', 'version.py')
with open(ver_file) as f:
    exec(f.read())

popylar_path = op.join(op.expanduser('~'), '.popylar')
uid = uuid.uuid1()

fhandle = open(popylar_path, 'a')
fhandle.write(uid)
fhandle.close()

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
