# Sorting Algorithm Performance Analysis
**Authors:** Ariel kellum 207064494,
            David Vaisfeld 208897645

## Project Overview
This project evaluates the performance and time complexity of three sorting algorithms: **Bubble Sort**, **Insertion Sort**, and **Quick Sort**. The program runs a series of experiments using both completely random arrays and nearly sorted arrays to demonstrate how initial data conditions affect algorithm efficiency.

## How to Run the Program
The experiment is run via the command line. Open your terminal in the project folder and execute the following command:

`python run_experiments.py -a 1 3 5 -s 100 500 1000 3000 -e 1 -r 10`

### Command Line Arguments:
* `-a`: Algorithms to run (1: Bubble Sort, 3: Insertion Sort, 5: Quick Sort)
* `-s`: Array sizes to test (e.g., 100, 500, 1000, 3000)
* `-e`: Noise level for nearly sorted arrays (1 = 5% noise, 2 = 20% noise)
* `-r`: Number of repetitions to average the execution time

note: the line used to create the resulting images was
`python run_experiments.py -a 1 3 5 -s 100 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 -e 1 -r 15`

---

## Part B: Random Array Performance 
**Output:** `result1.png`

* **Bubble Sort (Slowest):** Exhibits a strict $O(n^2)$ time complexity. It is the slowest because it must repeatedly compare and swap adjacent elements all the way through the array. The large number of 3-step swaps required in memory creates a massive overhead.
* **Insertion Sort (~Half the time of Bubble):** Also operates in $O(n^2)$ time, but finishes in roughly half the time of Bubble Sort. This is because, on average, its inner loop only has to scan halfway through the "already sorted" portion before finding the correct insertion spot. Furthermore, it *shifts* elements rather than performing full swaps, saving significant memory operations.
* **Quick Sort (Fastest):** Maintains a highly efficient $O(n \log n)$ average time complexity. By using a divide-and-conquer strategy to recursively partition the array, it barely registers on the graph's time scale compared to the quadratic algorithms, easily handling the 5,000-element arrays.

---

## Part C: Nearly Sorted Array Performance
**Output:** `result2.png`

When the algorithms are fed a "nearly sorted" array (an ordered array subjected to 5% random swaps via the `-e 1` flag), the performance dynamics change completely:

* **Insertion Sort's Massive Optimization:** Insertion Sort drops from its slow quadratic speed down to a nearly linear $O(n)$ time, flattening out on the graph and becoming highly competitive with Quick Sort.
* **The "Why":** This speedup is due to Insertion Sort's inner `while` loop condition (`while i >= 0 and A[i] > key`). Because the elements are mostly in the correct order already, the condition `A[i] > key` fails almost immediately. The algorithm realizes no shifting is needed, skips the heavy nested loop, and simply runs through the outer array in linear time.
