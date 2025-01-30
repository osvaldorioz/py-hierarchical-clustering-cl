from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "hierarchical_clustering",
        ["app/hierarchical_clustering.cpp"],
        extra_compile_args=["-std=c++20"],
    ),
]

setup(
    name="hierarchical_clustering",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
