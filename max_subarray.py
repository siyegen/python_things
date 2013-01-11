class SubArrayProblem(object):

    def __init__(self, array):
        self.array = array

    def solve(self):
        return self.__max_sub_array()

    def __max_sub_array(self):
        good_index = local_max = current_max = 0
        max_array = []

        for index, val in enumerate(self.array):
            local_max = max(0, local_max +val)

            if local_max > current_max:
                good_index = index
            if local_max == 0:
                max_array = []
            else:
                max_array.append(val)

            current_max = max(current_max, local_max)

        index_adjustment = len(self.array) - good_index
        good_index = good_index - index_adjustment
        return current_max, max_array[0:good_index+1]


x = [1, -5, 3, 2, 8, -3, 4, -8]

print "array %s" % repr(x)
sub_array = SubArrayProblem(x)

max_sub_value, max_sub_array = sub_array.solve()
print "%s is the max, %s is the array" % (max_sub_value, repr(max_sub_array))
