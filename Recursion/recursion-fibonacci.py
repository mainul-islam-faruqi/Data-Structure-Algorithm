def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def fibonacci1(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci1(n-2) + fibonacci1(n-1)

def test_fibonacci1():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n,f in enumerate(fib):
        assert fibonacci1(n+1) == f
