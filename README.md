# mat2mat
Convert a sparse count matrix (features x samples) into a new sparse count matrix of new features by calculating the overlap between features

<!-- badges: start -->
[![codecov](https://codecov.io/gh/hfldai/mat2mat/branch/main/graph/badge.svg?token=XCEMPOM53X)](https://codecov.io/gh/hfldai/mat2mat)
<!-- badges: end -->

A python package implementing a model-based, high resolution peak caller specific for ATAC-seq peak.

## Installation
```
# Download from github
git clone git@github.com:hfldai/mat2mat.git
cd mat2mat/

# Set up python requirements
pip install -r requirements.txt

# Install
pip install
```

## Example
```
mat2mat tests/test_data/test.query.regions tests/test_data/test.query.cells tests/test_data/test.query.mtx test.target.regions -o tests/example_output
```

## Dependencies
* [bedtools](https://bedtools.readthedocs.io/en/latest/)
* python packages: see [requirements.txt](https://github.com/hfldai/mat2mat/blob/main/requirements.txt)
