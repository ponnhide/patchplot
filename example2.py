import os 
import sys 
import matplotlib
import patchplot as pp

if __name__ == "__main__":
    pp.margin = 0.1
    fig = pp.set_fig()
    ax1 = pp.set_ax(fig,label=1) 
    
    ax2 = pp.set_ax(fig,label=2,aspect=(0.4,1))  
    pp.stack(fig,ax1,ax2,d="l")
    
    ax3 = pp.set_ax(fig,label=3,aspect=(1,0.4))  
    pp.stack(fig,ax1,ax3,d="t")
 
    pp.savefig(fig,"example2.pdf")
