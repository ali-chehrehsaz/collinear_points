# Discover Collinear Points

### Desired Results
This project is to implement a comprehensively tested algorithm that groups collinear points in 2-dimensional space and represent them with distinct lines in the Cartesian coordinate system in output. The output represented as a list of tuples of 2 elements (slope, intercept) for each unique discovered line.

### The Approach to Test Cases
- **Trivial Test Cases:** 
These are mostly sanity tests to see expected output for straightforward, understandable inputs.
Simple edge cases of parallel lines to y and x axes
Testing the app throws and passes exceptions when expected input is not received. 
- **Comprehensive Randomized Test Cases:** Using two helper functions, we can generate any arbitrary number of non-collinear points (including duplicates) and a set of any arbitrary number of lines with 3 or more collinear points on each. And feed this data as input to our algorithm and test against expected results.


### Set up Local Development
The core algorithm only uses built-in and standard python libraries. One of the implementations uses data classes that introduced in Python 3.7, and please ensure 3.7 or higher is installed on your machine. The test cases are verified only with Python 3.8.1.
Per the project requirement to use the best professional approach, we use Pytest with the test-coverage plugin for our tests. I truly believe the benefits of the Pytest testing framework make it an excellent choice developing python projects, including backend developments.

#### Project Files
```
$ git clone https://github.com/bnikanjam/collinear_points.git
``` 
#### Create Project Environment
```
$ pipenv install --dev
$ pipenv shell
```
> Please note that `pipenv` installs code quality tools for typing and enforcing PEP8 styling guidelines from Pipfile.lock that are not necessary for running or testing of this project, and you may use them if you wish.

or if you prefer use python `venv`
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install pytest pytest-cov
```

### Run Algorithm in other Apps
The algorithm script file is in a package Python directory. Copy this directory to your other app Python project root and import it as:
```
from collinear.get_collinears import get_lines
```
Please note this app purposely raises an exception if run independently. 

### Run Tests
**Run Tests Once**:
```
$ pytest
```
**Run Tests Once with Test Coverage**:
```
$ pytest --cov=.
```
**Run Tests Continuously**:
> Run the bash file `continues_test.sh` that keeps running tests while working on the code. Running tests continuously is also very useful since we use randomized test cases and running continuous tests exposes the algorithm to a loop of different test cases continuously. The bash file runs tests 1000 times in a terminal and displays a notification on macOS systems when 1000 tests completed.
```
$ ./continues_test.sh
```
