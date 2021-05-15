# http://eljjdx.canalblog.com/archives/2008/09/14/10571223.html
                
import numpy as np
import matplotlib.pyplot as plt
import itertools
import time

def F_logistic(x, mu):
    return mu*x*(1-x)

def Fprime_logistic(x, mu):
    ans = mu*(1-2*x)
    if (ans == 0.0):
        ans = 0.0001
    if (ans == -np.inf):
        ans = -1000
    if (ans == np.inf):
        ans = 1000
    return ans

class Lyapunov:
    def __init__(self, nb_iters, ab_min, ab_max, ab_step):
        self.nb_iters = nb_iters
        self.ab_min   = ab_min
        self.ab_max   = ab_max
        self.ab_step  = ab_step

    def process(self):
        step = int(1/self.ab_step)
        _a = np.linspace(self.ab_min, self.ab_max, step)
        _b = np.linspace(self.ab_min, self.ab_max, step)
        self.a, self.b = np.meshgrid(_a,_b)
        self.b = self.b.T        
        
        # test = np.array([[0., 4.],[0., 4.]])
        exponent = np.zeros((step, step))
        log = True
        for i, j in itertools.product(range(step), range(step)):
            pn  = 0.5
            exp = 0
            if log: print(f'{i}', end='\r'); log = False
            for k in range(self.nb_iters):
                seq  = self.a[0][i] if (k%2 == 0) else self.b[0][j]
                pn   = F_logistic(pn, seq)                                        
                exp += np.log(np.absolute(Fprime_logistic(pn, seq)))
            exponent[i, j] = exp / self.nb_iters
            if (j==step-1): log = True
            # print(exp)
        self.exponent = exponent
        #print(exponent)            
        return 

    def display(self):

        ''' colormap 
        cf. http://matplotlib.org/examples/color/colormaps_reference.html
        '''
        cmaps = ['plasma', 'bwr', 'Spectral', 'gist_rainbow', 'gnuplot2', 'nipy_spectral']
        my_cmap = plt.get_cmap(cmaps[5])
        my_cmap.set_over('black')              # clamp value over vmax to this value
        my_cmap.set_under('#124585')           # clamp value under vmin to this value

        extent = (np.min(self.a), np.max(self.a), np.min(self.b), np.max(self.b))
                
        ''' display '''        
        plt.figure(figsize=(10,10))
        plt.suptitle('Lyapunov factal')
        plt.title('logistic map for "ab" sequence (black is chaos)')
        plt.xlabel('a')
        plt.ylabel('b')                
        # https://matplotlib.org/stable/tutorials/intermediate/imshow_extent.html
        plt.imshow(self.exponent, cmap = my_cmap, vmin = -2, vmax = 0.01,
                   origin = 'lower', extent = extent)
        plt.colorbar()
        plt.show()
            
def main():
    print('Lyapunov in python!')
    lyapunov = Lyapunov(nb_iters = 100, ab_min = 2, ab_max = 4, ab_step = 0.001)
    t1 = time.time()
    lyapunov.process()
    t2 = time.time()
    print(f'Time taken by computing: {t2-t1}')
    lyapunov.display()
    
if __name__ == "__main__":
    main()
