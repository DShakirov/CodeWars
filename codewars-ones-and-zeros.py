import time

def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        res = fn(*args, **kwargs)
        print (f'Время работы {dt} сек')
        return res
    return wrapper

@test_time
def ones_and_zeros(arr):
    return int(''.join(map(str, arr)), 2)



print(ones_and_zeros([1, 1, 1, 0]))

