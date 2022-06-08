import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import sympy
from sympy import Function, Symbol, Derivative, exp, log, integrate

from plot import plot_side_by_side, plot

x = Symbol('x')



class logH:
    '''
    LogHazard trasform
    Class to compute symbolic transform
    '''

    @staticmethod
    def transform(f: Function):
        return log(f.diff(x)/(1-f))

    @staticmethod
    def hazard(f: Function):
        return f.diff(x)/(1-f)


    @staticmethod
    def inverse_transform(g: Function):
        '''
        logH^-1(g) = 1-exp(-integral_0^x exp(g(t))dt )
        '''
        expg = exp(g)
        integral = integrate(expg, x) # Primitive
        integral0 = integral.evalf(subs={x:0}) # Primitive evaluation in 0

        return 1-exp(-(integral-integral0))


def SymEval(f: Function, xvec, real_part: bool = True):
    '''
    Evaluate Sym function f on array xvec.
    :param real_part: True to return only real part of output
    '''
    if real_part:
        evaluation = np.array([f.evalf(subs={x: xx}).as_real_imag()[0] for xx in xvec])
    else:
        evaluation = np.array([f.evalf(subs={x: xx}) for xx in xvec])
    return evaluation





if __name__ == '__main__':

    # ---------- Function definition ----------
    f = log(x+1)


    # ---------- logH transform ----------
    logHf = logH.transform(f)
    Hazf = logH.hazard(f)


    # ---------- Evaluation ----------
    xvec=np.linspace(0, .99, 100)

    y = SymEval(f, xvec=xvec)
    logHy = SymEval(logHf, xvec=xvec)
    Hazy = SymEval(Hazf, xvec=xvec)

    # ---------- Plot ----------
    # plot_side_by_side(xvec, y, Hazy, y1_title='f', y2_title='logH(f)')
    plot(xvec, y, logHy, y1_label='f', y2_label='logH')






