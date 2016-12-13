from setuptools import setup, find_packages
import os
import os.path as op
import uuid
import configparser


ver_file = os.path.join('popylar', 'version.py')
with open(ver_file) as f:
    exec(f.read())

popylar_path = op.join(op.expanduser('~'), '.popylar')

# If UID file does not exist, then generate a UID and save to file.
# We don't overwrite an existing one in order to keep UIDs constant
# when the package is upgraded or installed in a venv.

if not os.path.exists(popylar_path):
    default_dict = dict(user=dict(uid=uuid.uuid1().hex,  track=True))
    parser = configparser.ConfigParser(default_dict)
    with open(popylar_path, 'w') as fhandle:
        parser.write(fhandle)

PACKAGES = find_packages()

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            packages=PACKAGES,
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
