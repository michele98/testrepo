import matplotlib.pyplot as plt
import numpy as np
import os


def win_iter(l, wl=5):
    """
    Generate a sliding window of wl dimension

    Parameters
    ----------
    :param l: length of the array to split
    :param wl: window length

    Return
    ----------
    :return: at each iteration it returns the indices of the window
    """
    ss = l // wl
    splits = np.array_split(np.arange(l), ss)
    for s in splits:
        yield s


def window_local(x, wl=5):
    """
    Computes the local minima on a running window on the columns of a 2D array.

    Parameters
    ----------
    :param x: a 2D `numpy.array` containing the data
    :param wl: window length

    Return
    ----------
    :return: The index of the local minimum for each window.
    """
    n, p = x.shape
    ss = win_iter(p, wl)
    locmin = []

    for idx in ss:
        iwidx = np.argmin(x[:, idx], axis=1)
        locmin.append(idx[iwidx])

    locmin = np.asarray(locmin)
    return locmin.T


if __name__ == '__main__':

    # Set the working directory
    prjdir = '/home/m-calvanese/wv2016/testrepo'

    # Read the data from a csv file. Columns separated by \t.
    # The first line of the file contains the scanned wavelengths
    tmpdata = np.loadtxt(os.path.join(prjdir, 'marzipan.csv'), delimiter='\t')
    wl = tmpdata[0]
    spectrum = tmpdata[1:]

    # Get dataset dimension
    n, p = spectrum.shape

    # Have a first look at our spectra
    for i in range(n):
        plt.plot(wl, spectrum[i, :], '--', label='sample %d' % i)
    plt.grid()
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflection intensity')
    plt.show()

    # Find local minima
    """
    for index, point in enumerate(spectrum[0]):
        old_dev = new_dev
        new_dev = np.diff(index, point)
        if np.sign(new_dev) > np.sign(old_dev):
            idx = window_local(spectrum)
        """
    derivatives = np.diff(spectrum[0])
    old_dev = 1
    for derivative in derivatives:
        if np.sign(derivative) > np.sign(old_dev):
            idx = window_local(spectrum)
        old_dev = derivative
    #idx = window_local(spectrum, wl=90)[0]

    # Compute a regression line for the first sample
    p2 = np.polyfit(wl[idx], spectrum[0, idx].flatten(), deg=1)
    pf = np.poly1d(p2)

    # Plot and have a look at the data
    plt.plot(wl, spectrum[0, :], 'b', label='sample %d' % 0)
    plt.plot(wl[idx], spectrum[0, idx], 'or', label='local minima')
    plt.plot(wl, pf(wl), '--', label='Fitting')
    plt.grid()
    plt.legend()
    plt.show()
