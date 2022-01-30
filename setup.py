import setuptools

setuptools.setup(
    name="mat2mat",
    version="0.0.1",
    author="Liangti Dai",
    author_email="liangti.dai@rdm.ox.ac.uk",
    description="A python tool to generate a sparse count matrix from the intersection of region lists",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'mat2mat = mat2mat:cli',
        ],
    }
)
