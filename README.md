# scmattools

<!-- badges: start -->
[![codecov](https://codecov.io/gh/hfldai/scmattools/branch/main/graph/badge.svg?token=XCEMPOM53X)](https://codecov.io/gh/hfldai/scmattools)
<!-- badges: end -->

A python toolkit for exploring genomic count matrices (matrices in format of _genomic regions (rows)_ x _samples (columns)_).

Note: The package is still in development and is updated actively.

Funtionalities:
* Given a genomic count matrix and a set of new genomic regions, compute a new count matrix with entries of intersecting region counts.

## Installation
```
# Download from github
git clone git@github.com:hfldai/scmattools.git
cd scmattools/

# Set up python requirements
pip install -r requirements.txt

# Install
pip install -e .

# Run test to check the installation is successful
python tests/test_main.py
```

## Usage
```
usage: scmattools [-h] [-o OUTPUT] [-ort OUTPUT_RT] [-oct OUTPUT_CT]
                  [-omatt OUTPUT_MATT]
                  rq cq matq rt

positional arguments:
  rq                    path to query region intervals (make sure the file is
                        Tab separated)
  cq                    path to query cell names
  matq                  path to query rq x cq sparse count matrix (.mtx)
  rt                    path to target region intervals (make sure the file is
                        Tab separated)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output directory
  -ort OUTPUT_RT, --output_rt OUTPUT_RT
                        path to the output target region intervals
  -oct OUTPUT_CT, --output_ct OUTPUT_CT
                        path to the output target cell names
  -omatt OUTPUT_MATT, --output_matt OUTPUT_MATT
                        path to the output target region x cell sparse count
                        matrix (.mtx)
```

## Example
```
scmattools tests/test_data/test.query.regions \
           tests/test_data/test.query.cells \
           tests/test_data/test.query.mtx \
           tests/test_data/test.target.regions \
           -o tests/example_output
```
More functions coming soon...

## Dependencies
* python (>=3.8)
* [bedtools](https://bedtools.readthedocs.io/en/latest/)
* python packages: see [requirements.txt](https://github.com/hfldai/mat2mat/blob/main/requirements.txt)

