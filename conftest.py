import pytest
import time


@pytest.fixture(scope='class')
def class_fixture(request):
    start_time = time.time()
    print(f'Class {request.cls.__name__} started at {start_time}')
    yield
    end_time = time.time()
    print(f'Class {request.cls.__name__} ended at {end_time}')


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f'Test finished in {end_time - start_time} seconds')
