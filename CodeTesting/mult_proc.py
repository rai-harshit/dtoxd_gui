from multiprocessing import Pool

def f(x):
	return x**2

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3,4,5]))