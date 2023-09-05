from datetime import time


def how1(b):
    def wrap (*args, **kwargs):
        time1 = time()
        result = b(*args, **kwargs)
        time2 = time()
        print(f"it took {time2 - time1} to execute")
        return result
    return wrap


@how1
def show(num: int):
    double = []
    for i in range(num):
        double.append(i * 2)
    return double

