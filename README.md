# logHazard
Simple functions to compute and visualize logHazard trasform.

In order to compute analytical trasform I use `Sympy` package.
In `lohH` class you will find both `.transform` and `.inverse_transform` methods that can be applied to `Function` classes (from `Sympy`).


$$
logH(g) = \frac{g'}{1-g}
$$
