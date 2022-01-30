import setuptools

setuptools.setup(
    name="scmattools",
    version="0.0.1",
    author="Liangti Dai",
    author_email="liangti.dai@rdm.ox.ac.uk",
    description="A python tool to generate a sparse count matrix from the intersection of region lists",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'scmattools = scmattools:cli',
        ],
    }
)
