# Sorting Algorithm Performance Analysis
**Author:** Ariel kellum 207064494,
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

---

## Part B: Random Array Performance 
**Output:** `result1.png`

When sorting completely random arrays, the time complexities align with theoretical expectations:
* **Bubble Sort & Insertion Sort:** Both algorithms exhibit a $\Theta(n^2)$ quadratic growth curve. As the array size increases, the execution time curves upward steeply.
* **Quick Sort:** Maintains a highly efficient, flat $O(n \log n)$ average time complexity, drastically outperforming the other two algorithms on larger datasets.

---

## Part C: Nearly Sorted Array Performance
**Output:** `result2.png`

When the input data is "nearly sorted" (e.g., a sorted array with only 5% random swaps), the performance dynamics change completely:
* **Insertion Sort's Optimization:** Insertion Sort drops from its slow quadratic $\Theta(n^2)$ time down to a nearly linear $O(n)$ time, making it incredibly fast and competitive with Quick Sort.
* **The "Why":** This massive speedup is due to Insertion Sort's inner `while` loop condition (`while i >= 0 and A[i] > key`). Because the elements are mostly in the correct order already, the condition `A[i] > key` fails almost immediately. The algorithm skips the heavy nested shifting and simply glides through the outer `for` loop.
