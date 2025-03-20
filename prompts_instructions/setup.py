# setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Define the extension
extensions = [
    Extension(
        "bollinger_cython",
        ["bollinger_cython.pyx"],
        include_dirs=[np.get_include()],
        extra_compile_args=["-O3", "-march=native", "-ffast-math"]
    )
]

# Setup configuration
setup(
    name="bollinger_cython",
    ext_modules=cythonize(extensions, compiler_directives={
        'language_level': 3,
        'boundscheck': False,
        'wraparound': False,
        'initializedcheck': False,
        'nonecheck': False,
        'cdivision': True,
    }),
)
