# scmattools

<!-- badges: start -->
[![codecov](https://codecov.io/gh/hfldai/scmattools/branch/main/graph/badge.svg?token=XCEMPOM53X)](https://codecov.io/gh/hfldai/scmattools)
<!-- badges: end -->

Convert a sparse count matrix (features x samples) into a new sparse count matrix of new features by calculating the overlap between features

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
usage: scmattools [-h] [-o OUTPUT] [-actual_rt ACTUAL_RT] [-actual_ct ACTUAL_CT] [-matt MATT] rq cq matq rt

positional arguments:
  rq                    path to query region intervals (make sure the file is Tab separated
  cq                    path to query cell names (make sure the file is Tab separated
  matq                  path to query region x cell sparse count matrix (.mtx)
  rt                    path to target regions

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output directory
  -actual_rt ACTUAL_RT  path to the output actual regions
  -actual_ct ACTUAL_CT  path to the output actual target cells
  -matt MATT            path to the output target region x cell sparse count matrix (.mtx)
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
* [bedtools](https://bedtools.readthedocs.io/en/latest/)
* python packages: see [requirements.txt](https://github.com/hfldai/mat2mat/blob/main/requirements.txt)

