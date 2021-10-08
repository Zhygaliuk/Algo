import argparse
import time

parser = argparse.ArgumentParser(description='HeapSort')
parser.add_argument('--order', type=str, help="Order asc/desc")
parser.add_argument('--sort_array', type=int, nargs='+', help='Enter integer')
args = parser.parse_args()

comparisons = 0
swaps = 0


def heapify(array, limit, largest_value, order):
    global comparisons
    root = largest_value
    left = 2 * largest_value + 1
    right = 2 * largest_value + 2

    if order == 'asc':
        if left < limit and array[root] < array[left]:
            root = left

        if right < limit and array[root] < array[right]:
            root = right
    elif order == 'desc':
        if left < limit and array[root] > array[left]:
            root = left

        if right < limit and array[root] > array[right]:
            root = right
    comparisons += 2

    if root != largest_value:
        swap(array, largest_value, root)
        heapify(array, limit, root, order)


def heap_sort(array, order):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i, order)

    for i in range(len(array) - 1, 0, -1):
        swap(array, 0, i)
        heapify(array, i, 0, order)


def swap(array, index1, index2):
    global swaps
    array[index1], array[index2] = array[index2], array[index1]
    swaps += 1
    return array


def main():
    global swaps
    global comparisons
    print("Heap sort:")

    starting = time.perf_counter()
    heap_sort(args.sort_array, args.order)
    end = time.perf_counter()
    duration = (end - starting) * 1000

    print(f"Execution time: {duration}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print("Sorted array: ")
    print(args.sort_array, "\n")

    return args.sort_array


if __name__ == "__main__":
    main()
