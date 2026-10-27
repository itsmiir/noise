In _Texturing and Modeling: A Procedural Approach_, F. Kenton Musgrave describes a few different methods for creating procedural terrain. A few methods are:
- **Fourier synthesis**. This method generates the entire terrain _all at once_; it is not a noise function. To generate a terrain, start with a white Gaussian noise basis function $W_N(s, \bold x)$, and evaluate it over some grid of values: and apply the following operations:
  - $\text{let } \bold A=\text{grid}_{N,M}, s\in\Z$
  - $W_N(s, \bold A)$
  - $> \text{FT}$
  - $>\times \frac{1}{r^\alpha}$ for some $\alpha \in [1, 2]$
  - $>\text{IFT}$
  
  This technique generates a 