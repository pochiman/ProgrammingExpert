##### Range Iterator #####

# Write a class based iterator named Range that is initialized by passing three interger values, a start, stop and step.
# Your iterator should mimic the range function in functionality but always accept three integer values.

# You may assume all three of these initialization values will always be integers and that the step will never be zero.

##### Sample Output #####
# >>> r = Range(2, 5, 1)
# >>> for x in r:
#         print(x)
# 2
# 3
# 4
# >>> r = Range(-2, -5, -1)
# >>> for x in r:
#         print(x)
# -2
# -3
# -4

class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.current_value >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current_value <= self.stop:
            raise StopIteration

        self.current_value += self.step

        return self.current_value - self.step