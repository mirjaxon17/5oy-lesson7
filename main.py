# range(x, y) => x - indexdan y - indexgacha, lekin y kirmaydi, step = 1
# range(x, y, z) => x - indexdan y - indexgacha, lekin y kirmaydi, step = z
# range(m) => 0 - indexdan boshlab m gacha => start = 0, stop = m, step = 1

class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step

        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration

        else:return self.start


for i in Range(2, 10, 2):
    print(i)
