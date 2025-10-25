### Intro to noise

#### Theory and notation

This repository is about noise. There are a few definitions for this word[^1], but the one I am using here is as follows:

**A noise function in $n$ dimensions is a [deterministic](./math-syntax.md#deterministic) [mapping](./math-syntax.md#functions-and-mappings) $N_n: \mathbb Z\times\mathbb{R}^{n}\to\mathbb [-1, 1]$**. 

See [this page](./math-syntax.md#functions-maps-and-set-notation) for an explanation of the math syntax. I try to hyperlink to specific definitions where possible.

Putting this all together, a plain English way of writing this definition might be like this:

**A noise function in $n$ dimensions is a function that takes in an integer (called the seed), along with a point in $n$-dimensional space and returns a single value between -1 and 1, inclusive. Every time you use the same seed and the same point in space, you will always get the same value.**
 
 A computer science way to say it might be like this:
```python
def N(seed: int, x: Iterable[float,...]) -> float:
    """Deterministic function."""
    output = some_function(seed, x)
    return clamp(output, -1, 1)
```
(English and Python are the two languages with which I can express technical topics most easily, so I will make use of them here.)

This is a pretty broad definition for noise, much broader than most people's. But I find it to be useful to think of noise this way.

##### Basis functions and operators
I like to think of noise functions as being made of two parts: **basis functions** and **operators**. Intuitively, a basis function is a primitive noise function, and an operator somehow transforms the output of that function. Formally, a basis function in $n$ dimensions is a function $B_n: \mathbb Z\times \mathbb R^n \to [-1,1]$, and an operator (as used by me) on $m$ arguments is a function $O_m:\mathbb R^m\to\R_1$. 

You can see that a basis function is itself a noise function as defined earlier, and an operator is not. However, with careful composition of functions and operators, a valid noise function can still be made. For example:
```py
import numpy as np
# for a basis function, I use the _1 suffix indicates that this is a 1-dimensional function, n = 1
def sin_1(seed: int, x: float) -> float:
    return np.sin(x)

# this basis function has n = 1
def cos_1(seed: int, x: float) -> float:
    return np.cos(x)

# for an operator, I use the _2 suffix indicates that m = 2 for this function
def add_2(a: float, b: float) -> float:
    return a + b

# for this operator, m = 1
def div2_1(a: float) -> float:
    return a / 2
```
`sin_1` is a 1d noise function (takes in a seed and a single float, outputs a float between -1 and 1), and it's also a basis function. The same applies to `cos_1`. `add_2` and `div2_1` are operators (take in $m$ inputs and output a single value).

We know that `sin_1` and `cos_1` will always output a value on the interval $[-1, 1]$, because the mathematical  functions that they're based on always return a value on $[-1, 1]$.
```py
x = get_1d_input

seed = 12

sin_1(seed, x) # this is a valid noise function; it varies from [-1, 1]

add_2(
    sin_1(seed, x), 
    cos_1(seed, x)
    ) # this is not! the output is on the interval [-2, 2]

# but we can bring it back to the proper interval using another operator...
div2_1(
    add_2(
        sin_1(seed, x), # [-1, 1]
        cos_1(seed, x), # [-1, 1]
    ) # [-2, 2]
) # [-1, 1] 
```


[^1]: Lagae, A., Lefebvre, S., Cook, R., DeRose, T., Drettakis, G., Ebert, D., Lewis, J., Perlin, K., & Zwicker, M. (2010). A survey of Procedural noise functions. Computer Graphics Forum, 29(8), 2579–2600. https://doi.org/10.1111/j.1467-8659.2010.01827.xxxx