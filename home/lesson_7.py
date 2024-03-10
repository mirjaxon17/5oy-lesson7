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
            # start = self.start
            #stop
            if (self.start > self.stop and self.step > self.start) or (self.start < self.stop and self.step < 0) or (self.start > self.stop and self.step > self.stop) or (self.start > self.stop and self.step > self.stop) or (self.start < 0 and self.stop > 0 and self.step < 0):
                print("rr")
                raise StopIteration
            else:
                #run
                if (self.start > self.stop and self.step > self.stop) or (self.start > self.stop and self.step > 0) or (self.start > 0 and self.stop < self.start and self.step > self.stop) or (self.start < 0 and self.stop > self.start or self.step > 0) or (self.start > self.stop and self.stop < 0 and self.step < 0):
                    if self.start >= self.stop:
                        raise StopIteration

            return self.start


for i in Range(-10, -1, 1):
    print(i)



# for i in range(-10, -1):
#     print(i)