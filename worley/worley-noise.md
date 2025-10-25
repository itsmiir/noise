### Worley noise
Worley noise (AKA Voronoi noise, cellular noise) is an extension of the concept of a Voronoi diagram; a tiling of a plane (or higher-dimensional spaces) with convex polygons (or higher-dimensional polytopes). It was invented by Steven Worley in the 90s as a complement to Ken Perlin's ubiquitous Perlin noise.

Worley noise is defined in $k$ dimensions as $F_n:\Z\times\R^k\to\R$. The index $n$ refers to the $n$th-closest feature point.


The original implementation of Worley noise is as follows:
- Partition $\R^3$ into a cubic tessellation.
- Generate some "feature points" in each cube according to a Poisson distribution:
  - For some desired mean feature point density $\lambda \in \R_{>0}$, the probability of $m$ feature points being located in any cell is given by $\left(\lambda^{-m}e^\lambda m!\right)^{-1}$. Fill a table with values between 1 and 9 based off of their relative probabilities as given by this function. Hash the coordinate of the cube into a random number, and select a value from that table. The number selected will be the number of points generated in the cube, $m_{ijk}$.
- Place $m_{ijk}$ points in each cube. The location of each feature point is also determined by hashing the coordinate of the cube.
- To evaluate $F_n(x)$:
  - Identify the cube $c_x$ containing the point $x$.
  - Evaluate the locations of the points in the cube. As each point is generated, calculate its squared distance to $x$. Perform an insertion sort to keep the distances sorted in an ordered list.
  - Iterate through the 26 cubes surrounding $c_x$, evaluating and insertion-sorting the locations of each of their points as you go.
    - Skip a cube if both of the following are true:
      - The list of points has length $\ge n$.
      - No feature point in the cube could possibly be closer than the $n$th entry in the list of points.

Modern implementations of Worley noise generally make a few adjustments to this algorithm:
- Instead of using a Poisson distribution to generate the points, $m$ is locked at $1$ for each cube; i.e., there is always one feature point per cube.
- All surrounding cubes are generally checked, instead of using exit conditions.
- Worley noise is often computed in 2 and 4 dimensions as well as 3.