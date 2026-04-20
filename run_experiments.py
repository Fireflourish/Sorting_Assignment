import random
import time
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
sys.setrecursionlimit(10000)

"""---------------------------------- part D - Simple User Interface ----------------------------------"""

parser = argparse.ArgumentParser(description="Sorting Algorithm Experiments")
parser.add_argument('-a', type=int, nargs='+', default=[1, 3, 5], help="Algorithms to run (1-5)")
parser.add_argument('-s', type=int, nargs='+', default=[100, 1000, 2000, 3000, 4000, 5000], help="Array size")
parser.add_argument('-e', type=int, default=1, help="Noise level")
parser.add_argument('-r', type=int, default=10, help="Number of repetitions")
args = parser.parse_args()


"""---------------------------------- part A - algorithm implementation -------------------------------"""
def quick_sort(A):
    quick_sort_helper(A, 0, len(A)-1)
def quick_sort_helper(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort_helper(A, p, q-1)
        quick_sort_helper(A, q+1, r)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j + 1] = A[j+1], A[j]

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

algs = {1: bubble_sort, 3: insertion_sort, 5: quick_sort}

"""---------------------------------- part B - Comparative Experiment ---------------------------------"""
r = args.r                        #number of repetitions
array_sizes = np.array(args.s)
sorting_algs = [algs[i] for i in args.a]
times = np.zeros((len(sorting_algs), len(array_sizes), r))

for alg in range(len(sorting_algs)):
    for n in range(len(array_sizes)):
        for size in range(r):
            arr = [random.randint(1, array_sizes[n]) for _ in range(array_sizes[n])]

            start = time.perf_counter()
            sorting_algs[alg](arr)
            end = time.perf_counter()

            times[alg, n, size] = end - start

avg_time = times.mean(2)
std_time = times.std(2)


plt.figure(figsize=(10, 6))
for alg in range(len(sorting_algs)):
    plt.plot(array_sizes, avg_time[alg], label=sorting_algs[alg].__name__, linewidth=2)
    plt.fill_between(array_sizes, avg_time[alg] - std_time[alg], avg_time[alg] + std_time[alg], alpha=0.1)

plt.title("Sorting Algorithm Performance (Random Arrays)")
plt.xlabel("Array Size (n)")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.grid(True)

#plt.savefig("result1.png")


"""---------------------------- part C - Experiment with Noise or Partial order -----------------------"""
def nearly_sorted_array(n, noise):
    ns_arr = list(range(1, n + 1))
    num_swaps = int(n * noise / 100)

    for _ in range(num_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        ns_arr[i], ns_arr[j] = ns_arr[j], ns_arr[i]

    return ns_arr
noises = {1:5, 2:20}

noise_percent = noises[args.e]
times2 = np.zeros((len(sorting_algs), len(array_sizes), r))

for alg in range(len(sorting_algs)):
    for n in range(len(array_sizes)):
        for size in range(r):
            arr = nearly_sorted_array(array_sizes[n], noise_percent)

            start = time.perf_counter()
            sorting_algs[alg](arr)
            end = time.perf_counter()

            times2[alg, n, size] = end - start

avg_time2 = times2.mean(2)
std_time2 = times2.std(2)

plt.figure(figsize=(10, 6))
for alg in range(len(sorting_algs)):
    plt.plot(array_sizes, avg_time2[alg], label=sorting_algs[alg].__name__, linewidth=2)
    plt.fill_between(array_sizes, avg_time2[alg] - std_time2[alg], avg_time2[alg] + std_time2[alg], alpha=0.1)

plt.title(f"Sorting Algorithm Performance (Nearly Sorted Arrays, {noise_percent}% noise)")
plt.xlabel("Array Size (n)")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.grid(True)

#plt.savefig("result2.png")
plt.show()


