# logHazard
Simple functions to compute and visualize logHazard trasform.

In order to compute analytical trasform I use `Sympy` package.
In `lohH` class you will find both `.transform` and `.inverse_transform` methods that can be applied to `Function` classes (from `Sympy`).

Let $g \in C^1(0,1)$ such that
$$
\begin{itemize}
  \item 0 \leqslant g < 1
  \item g' \geqslant 0
\end{itemize}
$$

then we define

$$
logH(g) = \frac{g'}{1-g}
$$
