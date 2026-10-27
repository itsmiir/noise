### Primer on math syntax

Throughout this repository, I use mathematical syntax to talk about several concepts. Math is unavoidable when talking about noise on any deep level. Since I'm not a mathematician, I try to keep it to a minimum, but the language of math is beautifully precise and useful, so it's worth using.

I use certain mathematical shorthand when referring to specific functions and variables that I use often. They are listed here, and in general, any $\LaTeX$ math in this repo adheres to these standards unless explicitly called out.
### Abuse of notation
- I abuse the terms "vector," "matrix," and "tensor" to refer to 1, 2, and $n$-dimensional finite tuples of values, respectively; essentially as shorthand for something like a `numpy` `ndarray`. The $i$th component of a rank-$N$ tensor of shape $I,J,K,...$ is a tensor of rank $N-1$ and shape $J,K,...$. Matrices are column-major.
- Tensors (including vectors and matrices) are denoted with bold text. 
- Explicitly defined vectors and matrices are denoted with square brackets. 3D tensors are defined by nesting vectors inside a matrix.
- For tensors, I use $\bullet$ to denote inner product (dot product), $\times$ to denote cross product, and $*$ to denote elementwise multiplication.
- I allow functions like $\sin$ and $\cos$ that would normally apply to a single value to apply to tensors elementwise.
### Algorithm syntax
When I write procedures in math syntax, I will write each step sequentially using a markdown list. 
- I define variables with $\text{let}$, and will usually use set notation as a "type hint." To define a variable $\bold x$ that is an $n$-dimensional vector of real numbers:
  - $\text {let } \bold x \in \R^n$
- Carets ($>$) represent "apply this function to the thing before".To represent $\tan(\cos(\sin(\bold x)))$ (where $\bold x$ is a 4d vector of real numbers):
  - $\text{let } \bold x\in\R^4$
  - $>\sin$
  - $>\cos$
  - $>\tan$
### Functions
- $\text{grid}_{\bold X}$ represents a function that generates a coordinate grid indexing $(|\bold X|)$-dimensional space. This is a rank-$(|\bold X|+1)$ tensor $\bold T$ of integers of shape $\bold X_1\times \bold X_2 \times ... \times\bold X_n\times n$, where the value of $\bold T_{i_1,i_2,...i_{n}}=[i_1-1, i_2-1, ...,i_n-1]$. For example, $\text{grid}_{m,n}$ generates the rank-3, $m\times n \times 2$ tensor $\begin{bmatrix}
    [0, 0] &[0,1]& \dots & [0,n]\\
    [1, 0] &[1,1]& \dots & [1,n]\\
    \vdots & &  \ddots & \vdots\\
    [m, 0] &[m,1] & \dots & [m,n]
  \end{bmatrix}$.
- $\text{FT}$ refers to a transformation on a tensor from time/space domain to frequency domain. For an $N$x$M$ The precise operation being done is this:
  - $\text{let } \bold X\in \Z^n;\bold G: \text{grid}_\bold X; f:\Z\times\R^n\to[-1,1]; s\in\Z$
  - $f(s, \bold G)$
  - $>  $
- $r$ is shorthand for the magnitude function; i.e. 
  - $\text{let } r:\bold x\in\R^n\mapsto \left(\sum_{i=1}^{|\bold x|}\bold x_i^2\right)^{\frac12}$
  - When this function is applied to higher-dimensional tensors, it acts on the final axis of the tensor.
### Standard names
- $\bold x$ is generally an arbitrary coordinate vector in either $\R^n$ or $\Z^n$.
- $\bold G$ is generally a grid.
- $N$ usually denotes an arbitrary noise function.
- $W_N$ and $W_U$ denote white noise functions with normally- and uniformly-distributed values, respectively.
- 