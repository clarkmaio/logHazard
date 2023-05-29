# logHazard
Simple functions to compute and visualize logHazard trasform.

In order to compute analytical trasform I use `Sympy` package.
In `lohH` class you will find both `.transform` and `.inverse_transform` methods that can be applied to `Function` classes (from `Sympy`).

Let $g \in C^1(0,1)$ such that
  - $0 \leqslant g(t) < 1$
  - $g'(t) \geqslant 0$

then we define

$$
logH(g)(s) = \frac{g'(s)}{1-g(s)}
$$


$$
logH^{-1}(f)(x) = 1-\exp\left(-\int_a^x \exp \left(f(s)\right) ds \right)
$$


Inspired from the paper ["Constrained functional time series: Applications to the Italian
gas market"](https://sci-hub.se/10.1016/j.ijforecast.2016.05.002).
