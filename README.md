# pytest
Running the tests

RUNNING TESTS:

pytest -m tag
pytest -v verbose
pytest -s prints system outputs


SKIPPING:
@mark.skip(reason=something)
@mark.xfail - expect a test to fail

RUNNING TESTS IN PARALLEL:
pip install pytest-xdist
use pytest -v -s -n4 or whatever number to run concurrent tests (4 concurrent here)