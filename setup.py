import os,sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

try:
ext = Extension("cracks",sources=["cracks.c"])

setup(
	ext_modules=[ext],
	cmdclass={"build_ext": build_ext}
)

try:
	os.system("rm -rf build")
except:
	pass
