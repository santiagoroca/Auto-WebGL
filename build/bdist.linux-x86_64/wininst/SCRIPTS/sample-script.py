#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autowebgl==0.1.0','console_scripts','sample'
__requires__ = 'autowebgl==0.1.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('autowebgl==0.1.0', 'console_scripts', 'sample')()
    )
