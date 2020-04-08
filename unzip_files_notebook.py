# Using Python to extract files from a .zip file

from zipfile import ZipFile
with ZipFile('foo.zip', 'r') as zf:
    zf.extractall('destination_path/')

# Another way with fewer line of code

from shutil import unpack_archive
unpack_archive('foo.zip', 'destination_path/')