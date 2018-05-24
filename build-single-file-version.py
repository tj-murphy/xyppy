#! /usr/bin/env python

import os
import stat
import zipfile
import StringIO

package_dir = 'xyppy'
python_directive = '#!/usr/bin/env python'

packed = StringIO.StringIO()
packed_writer = zipfile.PyZipFile(packed, 'w', zipfile.ZIP_DEFLATED)
packed_writer.writepy(package_dir)
packed_writer.writestr('__main__.py', '''
from xyppy import __main__
if __name__ == '__main__':
    __main__.main()
''')
packed_writer.close()

pyfile = package_dir + '.py'
with open(pyfile, 'wb') as f:
    f.write(python_directive + '\n')
    f.write(packed.getvalue())
os.chmod(pyfile, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)