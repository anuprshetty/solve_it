# Algorithm

## Mathematical concepts behind the analysis of algorithm

### Growth rate of a function

- The growth rate of a function generally refers to how quickly the function’s values increase or decrease as its input becomes very large.
- Growth rate focuses on the trend or speed at which a function grows.
- Example: polynomial growth, exponential growth, logarithmic growth.
- A function f(x) is said to be growing faster than g(x) if
  - $$\lim_{{x \to \infty}} \frac{f(x)}{g(x)} = \infty \quad \text{or} \quad \lim_{{x \to \infty}} \frac{g(x)}{f(x)} = 0$$

### Order of growth of a function

- The order of growth of a function describes the general class or family to which the growth rate of a function belongs, often expressed asymptotically.
- When we say that a function has a specific order of growth, we use asymptotic notations to describe how the function behaves relative to a simpler, standard function as the input grows very large.
- Example: f(x) = 3x^2 + 5x + 2 has an order of growth O(x^2), meaning it grows similarly to x^2 as x becomes very large.
- Asymptotic notations are used for representing the simple form of a function or showing the class of a function.
- General function classes or families & their comparative growth rate when their input becomes very large:
  - Order of: 1 (constant time) < log(log x) < log x (logarithmic time) < x^(1/3) < x^(1/2) < x (linear time) < x\*log x < x^2 (quadratic time) < x^3 (cubic time) < ... < 2^x (exponential time) < 3^x (exponential time) < ... < x! (factorial time) < x^x (exponential time)

### Asymptote

- An asymptote is a straight line that constantly approaches a given curve but does not meet at any infinite distance.
- ![asymptote](/media/asymptote.png)

### Asymptotic notations

- Asymptotic notations are used for representing the simple form of a function or showing the class of a function.
- General function classes or families & their comparative growth rate when their input becomes very large:
  - Order of: 1 (constant time) < log(log x) < log x (logarithmic time) < x^(1/3) < x^(1/2) < x (linear time) < x\*log x < x^2 (quadratic time) < x^3 (cubic time) < ... < 2^x (exponential time) < 3^x (exponential time) < ... < x! (factorial time) < x^x (exponential time)
- The limiting behavior of a function refers to how the function behaves as its input approaches a specific value, often infinity, negative infinity, or a particular point where the function might have a boundary or discontinuity. This is done formally using limits.
- Asymptotic notations are used to describe the limiting behavior of functions as their inputs grow very large or approach some critical value.
- Before asymptotic notations, mathematicians had to rely on more complex definitions to describe how functions behave as their inputs become large. Asymptotic notation provides an elegant and concise way to express these behaviors.
- asymptotic notations are essential for comparing the growth rates of functions, especially when dealing with large values of x.
- ![asymptote](/media/asymptotic_notations.png)

#### Big-Oh notation (O)

- Big-Oh notation describes an upper bound on the growth rate of a function.
- Example: f(x) = 2x and g(x) = x^2, then f(x) = O(g(x)) --> means that f(x) grows no faster than a constant multiple of g(x) as x becomes very large.
- NOTE: Here g(x) can be any function that upper bounds f(x) like g(x) = x^3, 2^x, etc.

#### Big-Omega notation (Ω)

- Big-Omega notation describes a lower bound on the growth rate of a function.
- Example: f(x) = 2x and g(x) = log x, then f(x) = Ω(g(x)) --> means that f(x) grows at least as fast as a constant multiple of g(x) as x becomes very large.
- NOTE: Here g(x) can be any function that lower bounds f(x) like g(x) = log(log x), 1 (or constant), etc.

#### Big-Theta notation (Θ)

- Big-Theta notation provides a tight bound on the growth rate of a function, meaning it both upper-bounds and lower-bounds the function.
- Example: f(x) = 2x and g(x) = x, then f(x) = Θ(g(x)) --> means that f(x) grows at the same rate as a constant multiple of g(x) as x becomes very large.

#### Little-oh Notation (o)

- Little-oh notation describes an upper bound on the growth rate of a function that is not tight.
- Example: f(x) = 2x and g(x) = x^2, then f(x) = o(g(x)) --> means that f(x) strictly grows slower than a constant multiple of g(x) as x becomes very large.

#### Little-Omega notation (ω)

- Little-Omega notation describes a lower bound on the growth rate of a function that is not tight.
- Example: f(x) = 2x and g(x) = log x, then f(x) = ω(g(x)) --> means that f(x) grows strictly faster than a constant multiple of g(x) as x becomes very large.

## Analysis of algorithm

- Best case scenario --> best case time and space --> best case time and space complexity using asymptotic notations.
- Worst case scenario --> worst case time and space --> worst case time and space complexity using asymptotic notations.
- Average case scenario (literally average of all possible scenarios) --> average case time and space --> average case time and space complexity using asymptotic notations.
- NOTE: Any asymptotic notation can be applied to any mathematical function. Therefore, we can use all the asymptotic notations to represent any algorithmic scenario's (best, worst, average) time and space complexities. Because time and space complexities of an algorithm are described in terms of mathematical functions regardless of whether they are for best, worst or average case scenarios.

## Analysis of time complexity of an algorithm

- T(n) --> time taken by an algorithm.

### Analysis of constant time

- Assume constant time as 1. So T(n) = 1.

### Analysis of iterative time

- n --> input value
- k --> total iterations

- | iteration      | 1   | 2   | 3   | 4   | 5   | ... | k-1 | k (total iterations) | <= or >= | loop_condition |
  | -------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | -------- | -------------- |
  | iterator_value |     |     |     |     |     | ... |     |                      | <= or >= | loop_condition |

- T(n) --> iteration time for n = k in terms of n [i.e., express k in terms of n which is nothing but T(n)].
- Examples:
  - [analysis_of_iterative_time](/media/analysis_of_iterative_time.pdf)

### Analysis of recursive time

- Recurrence relation:
  - In mathematics, a recurrence relation is an equation according to which the nth term of a sequence of numbers is equal to some combination of the previous terms.
  - Example: The factorial of x is
    $$ f(x) = \begin{cases} x \cdot f(x-1) & \text{ ; } x > 0 \\ 1 & \text{ ; } x = 0 \end{cases} $$
- Recursion: Defining a problem in terms of itself.
- Recursion in computer science:
  - recursion uses stack.
  - recursion can be visualized as recursion tree.
- The time taken by a recursive function can be represented as recurrence relation.
  - Example: time taken by the factorial function is
    $$ T(n) = \begin{cases} 1 + T(n-1) & \text{ ; } n > 0 \\ 1 & \text{ ; } n = 0 \end{cases} $$
- Examples:
  - [analysis_of_recursive_time](/media/analysis_of_recursive_time.pdf)

## Analysis of space complexity of an algorithm

- S(n) --> additional or auxiliary space taken by an algorithm excluding the input/output space.

### Analysis of constant space

- Assume constant auxiliary space as 1. So S(n) = 1.

### Analysis of iterative space

- S(n) = total auxiliary space taken for k iterations.

### Analysis of recursive space

- Recursion uses stack. So S(n) = k (recursion depth).
