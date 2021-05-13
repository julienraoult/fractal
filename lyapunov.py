# http://eljjdx.canalblog.com/archives/2008/09/14/10571223.html
                
import numpy as np
import matplotlib.pyplot as plt

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
        skip = 1200
        #for i in range(skip):
        #    seq  = self.a[0][0] if (i%2 == 0) else self.b[0][0]
        #    pn   = F_logistic(pn, seq)                    
        exponent = np.zeros((step, step))
        for index_a in range(step):
            print(index_a)
            for index_b in range(step):
                pn  = 0.5
                exp = 0
                for i in range(skip, skip + self.nb_iters):
                    seq  = self.a[0][index_a] if (i%2 == 0) else self.b[0][index_b]
                    pn   = F_logistic(pn, seq)                                        
                    exp += np.log(np.absolute(Fprime_logistic(pn, seq)))
                exponent[index_a,index_b] = exp / self.nb_iters
                # print(exp)
        self.exponent = exponent
        #print(exponent)            
        return 

    def display(self):

        ''' colormap 
        cf. http://matplotlib.org/examples/color/colormaps_reference.html
        '''
        cmaps = ['plasma', 'bwr', 'Spectral', 'gist_rainbow', 'gnuplot2', 'nipy_spectral']
        my_cmap = plt.get_cmap(cmaps[0])
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
        plt.imshow(self.exponent, cmap = my_cmap, vmin = -2, vmax = 0.0001,
                   origin = 'lower', extent = extent)
        plt.colorbar()
        plt.show()
            
def main():
    print('Lyapunov in python!')
    lyapunov = Lyapunov(nb_iters = 200, ab_min = 2, ab_max = 4, ab_step = 0.004)
    lyapunov.process()
    lyapunov.display()
    
if __name__ == "__main__":
    main()
