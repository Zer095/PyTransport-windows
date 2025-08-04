from setuptools import setup, Extension
import os
from shutil import rmtree
import numpy
import sys

# Define compiler flags based on the platform
if sys.platform.startswith('win'):
    # Flags for MSVC (Windows compiler)
    # /O2 is for maximum speed, /fp:fast enables fast floating-point math
    compile_args = ['/O2', '/fp:fast']
else:
    # Flags for GCC or Clang (Linux, macOS)
    # -O3 is the highest level of optimization
    # -march=native optimizes for the specific CPU architecture of your machine
    # -ffast-math allows for aggressive floating-point optimizations (use with care)
    compile_args = ['-O3', '-march=native', '-ffast-math']


# Define the path to the 'include' directory that contains the header files
include_dir = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'include'))]

# Set the CXXFLAGS environment variable to include the 'include' directory
os.environ["CXXFLAGS"] = f"-I{include_dir}"

# Define the extension module
PyTransDQ = Extension(
    "PyTransDQ",
    sources=[r"C:\Users\shcos\OneDrive\Desktop\PyTransport3.0-master\PyTransport\PyTransCpp\PyTrans.cpp",r"C:\Users\shcos\OneDrive\Desktop\PyTransport3.0-master\PyTransport\PyTransCpp\cppsrc\stepper\rkf45.cpp"],
    include_dirs = ['C:\\Users\\shcos\\OneDrive\\Desktop\\PyTransport3.0-master\\PyTransport\\PyTransCpp', 'C:\\Users\\shcos\\OneDrive\\Desktop\\PyTransport3.0-master\\PyTransport\\PyTransCpp\\cppsrc\\stepper', 'C:\\Users\\shcos\\OneDrive\\Desktop\\PyTransport3.0-master\\venv\\Lib\\site-packages\\numpy\\core\\include'],
    #extra_compile_args=compile_args,
    language="c++",
)

# Setup configuration
setup(
    name="PyTransDQ",
    ext_modules=[PyTransDQ],
    package_data={
        "PyTransDQ": [numpy.get_include()],
    },
)