# Progression

## Sequence vs Series

- In mathematics, both sequences and series are fundamental concepts related to ordered sets of numbers.

### Sequence

- A sequence is an ordered list of numbers, where each number (called a term) follows a specific rule or pattern.
- Notation: a1, a2, a3, ..., an

### Series

- A series is the sum of the terms of a sequence.
- Notation: Sn = a1 + a2 + a3 + ... + an

## Types of progression

### Arithmetic progression (AP)

- A sequence in which each term after the first is obtained by adding a fixed constant (called the common difference) to the previous term.
- General form: a, a+d, a+2d, ..., [a + (n-1)d]
- Formula for the n-th term: an = a + (n-1)d
- Sum of first n terms: Sn = n/2 [2a + (n-1)d]
- NOTE: Sum of first n positive integers, Sn = [n * (n+1)]/2

### Geometric progression (GP)

- A sequence in which each term after the first is obtained by multiplying the previous term by a fixed constant (called the common ratio).
- General form: a, ar, ar^2, ..., [a * r^(n-1)]
- Formula for the n-th term: an = a \* r^(n-1)
- Sum of first n terms:
  - for r > 1 --> Sn = a \* [(r^n - 1) / (r-1)]
  - for r = 1 --> Sn = a \* n
  - for r < 1 --> Sn = a/(1-r)

### Harmonic progression (HP)

- A sequence in which the reciprocals of the terms form an arithmetic progression.
- General form: 1/a, 1/(a+d), 1/(a+2d), ..., 1/[a + (n-1)d]
- Formula for the n-th term: an = 1/[a + (n-1)d]
- Sum of first n terms: There is no simple formula for the sum of a harmonic progression.
