# Giving 2 sorted lists, merge them together
import unittest, sys

class TestNWayMerge(unittest.TestCase):

    def test_merge_two(self):
        # Merge a and b, result should be
        array_a = range(1, 6)
        array_b = range(6, 11)
        expected = [1,2,3,4,5,6,7,8,9,10]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_matching(self):
        array_a = [1,2,3]
        array_b = [3,4,5]
        # Merge a and b, result should be
        expected = [1,2,3,3,4,5]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_diff_size(self):
        array_a = [1,7,9,10]
        array_b = [3,4,5]
        # Merge a and b, result should be
        expected = [1,3,4,5,7,9,10]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_all_same(self):
        array_a = [1,1,1,1]
        array_b = [2,2]
        # Merge a and b, result should be
        expected = [1,1,1,1,2,2]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_one_empty(self):
        array_a = [1,1,1,1]
        array_b = []
        # Merge a and b, result should be
        expected = [1,1,1,1]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_both_empty(self):
        array_a = []
        array_b = []
        # Merge a and b, result should be
        expected = []
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_two_huge(self):
        array_a = [10**100]
        array_b = [1,2]
        # Merge a and b, result should be
        expected = [1,2,10**100, 10**200]
        merged_array = merge_two(array_a, array_b)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_three(self):
        array_a = [1,2,3]
        array_b = [4,5,6]
        array_c = [7,8,9]
        expected = [1,2,3,4,5,6,7,8,9]
        merged_array = n_way_merge(array_a, array_b, array_c)
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_four(self):
        array_a = [1,2]
        array_b = [2,5,6]
        array_c = [4,8,9]
        array_d = [11,12]
        expected = [1,2,2,4,5,6,8,9,11,12]
        merged_array = n_way_merge(array_a, array_b, array_c, array_d)
        print 'moo', merged_array
        self.assertEquals(merged_array, expected, 'Array merged together')

    def test_merge_five(self):
        array_a = [1,2]
        array_b = [5,6]
        array_c = [8,9]
        array_d = [11,12]
        array_e = [12,12]
        expected = [1,2,5,6,8,9,11,12,12,12]
        merged_array = n_way_merge(array_a, array_b, array_c, array_d, array_e)
        self.assertEquals(merged_array, expected, 'Array merged together')


def n_way_merge(*args):
    length = len(args)
    if length == 2:
        return merge_two(args[0], args[1])
    elif length == 1:
        return args[0]
    else:
        first, second = args[0:2]
        rest = args[2:len(args)]
        merged_left = merge_two(first, second)
        return n_way_merge(merged_left, *rest)

def merge_two(array_1, array_2):
    # pointer for arrays
    ptr_1 = ptr_2 = 0
    total_len = len(array_1) + len(array_2)
    result = []
    while len(result) < total_len:
        item_1 = array_1[ptr_1] if ptr_1 < len(array_1) else sys.maxint
        item_2 = array_2[ptr_2] if ptr_2 < len(array_2) else sys.maxint
        if item_1 < item_2:
            result.append(item_1)
            ptr_1 = ptr_1 + 1
        else:
            result.append(item_2)
            ptr_2 = ptr_2 + 1

    return result

