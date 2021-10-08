import main
import unittest


class HeapTestSort(unittest.TestCase):
    def setUp(self):
        self.asc_sorted_array = [1, 2, 4, 6, 7, 8, 100, 120]
        self.desc_sorted_array = [120, 100, 8, 7, 6, 4, 2, 1]
        self.unsorted_array = [2, 1, 4, 8, 7, 6, 120, 100]

    def test_sorting(self):
        main.args.sort_array = self.unsorted_array
        testing_array = main.main()
        is_sorted = all(testing_array[i] >= testing_array[i + 1] for i in range(len(testing_array) - 1))
        self.assertTrue(is_sorted)

    def test_asc_by_asc_sorted_array(self):
        main.args.sort_array = self.asc_sorted_array
        main.args.order = "asc"
        self.assertEqual(main.main(), self.asc_sorted_array)

    def test_asc_by_desc_sorted_array(self):
        main.args.sort_array = self.desc_sorted_array
        main.args.order = "asc"
        self.assertEqual(main.main(), self.asc_sorted_array)

    def test_desc_by_asc_sorted_array(self):
        main.args.sort_array = self.asc_sorted_array
        main.args.order = "desc"
        self.assertEqual(main.main(), self.desc_sorted_array)

    def test_desc_by_desc_sorted_array(self):
        main.args.sort_array = self.desc_sorted_array
        main.args.order = "desc"
        self.assertEqual(main.main(), self.desc_sorted_array)


if __name__ == "__main__":
    unittest.main()