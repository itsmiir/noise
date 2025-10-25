### Primer on math syntax

Throughout this repository, I use mathematical syntax to talk about several concepts. Math is unavoidable when talking about noise on any deep level. Since I'm not a mathematician, I try to keep it to a minimum, but the language of math is beautifully precise and useful, so it's worth using. I'll try to explain the syntax I am using as simply as possible.

### Functions, maps, and set notation

To start, let's look at my definition for a noise function:

**A noise function in $n$ dimensions is a deterministic mapping $N_n: \mathbb Z\times\mathbb{R}^{n}\to\mathbb [-1, 1]$**.

Breaking this definition down:
- $N$ is just the name of the mapping. I used $N$ because N is for Noise. I put the subscript $n$ to indicate dimensionality; $N_1$ is a function in 1 dimension, $N_2$ is a function in 2 dimensions, $N_n$ is a function in $n$ dimensions.
#### Doublestruck letters
- The symbols $\mathbb Z$ and $\mathbb R$ are called **doublestruck** letters. $\mathbb Z$ = "doublestruck Z" and $\mathbb R$ = "doublestruck R." They are used to represent certain [sets](math-syntax.md#sets) of things. For example, $\mathbb Z$ represents the integers (e.g., 12, -1, 0, 150), and $\mathbb R$ represents the real numbers (e.g. $\pi$, 1, 0.001, -1219.2141, $\frac13$, $\sqrt 2$).
#### Sets
- A "set" is just a bunch of things (called "elements") that all share some common property. A set can be anything you want it to be. You can define a set that is made up of every sandwich that has ever been eaten by a Russian president, or a set that is made up of every possible triangle. For my purposes, though, a set will usually be a group of numbers ("group" in the colloquial sense, not the mathematical sense).
##### Subsets and inheritance
- It can be useful to think about a [set](./math-syntax.md#sets) as a "class" from object-oriented programming. Perhaps I might have a set $S$ which is made up of all possible sandwiches. I might have a subset $S'$ which is all possible sandwiches that are grilled. In computer science, I might define a class `Sandwich`, and a subclass `GrilledSandwich`. These essentially mean the same thing.
- I denote [subsets](./math-syntax.md#subsets-and-inheritance) with $\subset$. So the language $\mathbb B \subset \mathbb A$ means the same thing as:
  ```py
  class B(A):
    ...
  ```
##### Set syntax
- Some common set syntax you might see:
  - A superscript number $n$ on a set symbol can be thought of as turning it into a set of $n$-dimensional vectors. So if you think of $\mathbb R$ as a number line, $\mathbb R^2$ is a Cartesian (x/y) plane, and $\mathbb R^3$ is 3D space. Some elements of $\mathbb R$ are $1, 2, \pi, \frac13,$ or $-11.102312$. Some elements of $\mathbb R^3$ are $(0, 0, 0), (-1, 100.2312, \sqrt 2),$ and $(9.002, 33, -0.01)$.
  - $a \in A$ means "$a$ is an element of $A$. This is basically a variable declaration in math syntax. In Python, I might declare a variable with "`i: int`", and in math syntax, I might do the same thing with "$i \in \mathbb Z$" ([doublestruck Z](./math-syntax.md#doublestruck-letters)). Note that this is not a definition, but a declaration--when working with sets, we are usually less concerned with behavior for individual members of a set, and more concerned with behavior for any/all members of a set.
#### Intervals
- The syntax $[a, b]$, where $a \in \mathbb R$ and $b \in \mathbb R$, represents an interval. An interval is a special [subset](./math-syntax.md#subsets-and-inheritance) of $\R$ that includes all numbers between $a$ and $b$. A **closed interval** is one that includes its endpoints, an **open interval** does not, and a **half-open interval** includes one but not the other. A closed interval uses square brackets $[a, b]$, an open interval uses parentheses $(a, b)$, and a half-open interval uses one of each: $[a, b)$ or $(a, b]$.
#### Functions and mappings
- A "function," mathematically, is a process that takes in one or more numbers, and outputs one or more numbers. Another word for a function is a "mapping."    
- The syntax $N : A\to B$ means "$N$ is a mapping from the [set](./math-syntax.md#sets) $A$ onto the set $B$; or, in other words, $N$ assigns each thing in the "$A$" set a thing from the "$B$" set. This is essentially a mathematical function definition, roughly equivalent to:
  ```py
  def N(a: A) -> B:
    ...
  ``` 
- If I have more input variables to my function, I can use an $\times$ symbol to represent additional inputs. For $n$ inputs of the same type (or, to put it computer-ly, $n$ arguments of the same class), a superscript $n$ is used: $F: \mathbb Z\times\mathbb R^3\to\R^1$ is the same thing as
  ```py
  def F(z: int, r1: float, r2: float, r3: float) -> float:
    ...
  ```
#### "Deterministic"
- A [mapping](./math-syntax.md#functions-and-mappings) is "deterministic" if it produces the same output for every input. A dice roll is not deterministic, but the mathematical sine function is.
