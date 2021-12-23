
# Install Pytest
```
pip install -U PyTest
```

# Run a test
```
pytest first_test.py
```
## Grouping or running a sub set of tests
```
pytest -k method1 -v 

or 

pytest -m one (Using marks)
```
 - `-v ` for verbose and `-k` to select the test with method1


