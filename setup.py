#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      azahid
#
# Created:     02/04/2016
# Copyright:   (c) azahid 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from setuptools import setup
import os
import py2exe

#delete the old build
os.system("rmdir /s /q dist")
#include the packages
includes = ["sip",
            "PyQt4",
            "PyQt4.QtCore",
            "PyQt4.QtGui",
           ]
datafiles = [("", [r"c:\windows\syswow64\MSVCP100.dll",
                   r"c:\windows\syswow64\MSVCR100.dll"]) ,
             ("", [r"C:\Users\user\Desktop\Team Tool\LogoConverter.png"]),
             ("imageplugins", [
            'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qgif4.dll',
            'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qjpeg4.dll',
            'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qsvg4.dll',
            ]),
             ]

setup(
    name='ConverterQtPy',
    url='',
    license='',
    windows=[{"script": "Converter.py"}],
    scripts=['Converter.py'],
    data_files=datafiles,

    options={
        "py2exe":{
            "includes": includes,
        }
    }
)