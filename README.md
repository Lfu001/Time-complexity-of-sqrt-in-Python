# Time-complexity-of-sqrt-in-Python
Investigate whether the computation time of sqrt() varies with the size of the input. Measure the computation time for math.sqrt(), numpy.sqrt() and (** 0.5).

## How to measure computation time？
Measure the time it takes to execute a `function` 100000 times.
```
function: {math.sqrt(), numpy.sqrt(), (** 0.5)}
```
`time.time()` is used to measure time.

## Result
Figure 1: Comparison of all functions.
![comparison_of_time_to_compute_sqrt](https://user-images.githubusercontent.com/82690385/159659421-52884e5f-4120-4771-a067-1f0627d73873.png)

Figure 2: Enlarged view of Figure 1
![comparison_of_time_to_compute_sqrt_2](https://user-images.githubusercontent.com/82690385/159659511-7ec20014-c94e-4f16-a23b-f2afe9e90a16.png)

## Conclusion
  - All sqrt functions have O(1) time complexity.
  - Computing time: `numpy.sqrt() >> math.sqrt() > (** 0.5)`