def myzip(it1, it2):
    it1_iter = iter(it1)
    it2_iter = iter(it2)

    while True:
        try:
            element1 = next(it1_iter)
            element2 = next(it2_iter)
            yield (element1, element2)
        except StopIteration:
        
            break


list1 = [1, 2, 3, 4]
tuple1 = ('a', 'b', 'c', 'd')

for pair in myzip(list1, tuple1):
    print(pair)
