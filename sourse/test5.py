import numpy, scipy.optimize
import matplotlib.pyplot as plt

with open('dataXY.txt') as f:
    a = f.readlines()
    x, y = [], []
    for i in a:
        a, b = i.split()
        x.append(a)
        y.append(b)


x = numpy.array(list(map(float, x)))
y = numpy.array(list(map(float, y)))

def fit_sin(x, y):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    ff = numpy.fft.fftfreq(len(x), (x[1]-x[0]))   # assume uniform spacing
    Fyy = abs(numpy.fft.fft(y))
    guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = numpy.std(y) * 2.**0.5
    guess_offset = numpy.mean(y)
    guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, x, y, p0=guess)
    A, w, p, c = popt
    f = w/(2.*numpy.pi)
    fitfunc = lambda t: A * numpy.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}

N, amp, omega, phase, offset, noise = 500, 1, 2, 5, 4, 3
#N, amp, omega, phase, offset, noise = 50, 1., .4, .5, 4., .2
#N, amp, omega, phase, offset, noise = 200, 1., 20, .5, 4., 1
x = numpy.linspace(0, 10, N)
tt2 = numpy.linspace(0, 10, 10*N)
y = amp*numpy.sin(omega*x + phase) + offset
yynoise = y + noise*(numpy.random.random(len(y))-0.5)

res = fit_sin(x, yynoise)
print( "Amplitude=%(amp)s, Angular freq.=%(omega)s, phase=%(phase)s, offset=%(offset)s, Max. Cov.=%(maxcov)s" % res )

plt.plot(x, y, "-k", label="y", linewidth=2)
plt.plot(x, yynoise, "ok", label="y with noise")
plt.plot(tt2, res["fitfunc"](tt2), "r-", label="y fit curve", linewidth=2)
plt.legend(loc="best")
plt.show()



