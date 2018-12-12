import os 
import sys 
import matplotlib
import patchplot as pp

if __name__ == "__main__":
    pp.margin = 0.25
    fig = pp.set_fig()
    ax1 = pp.set_ax(fig,label=1) 
    pp.savefig(fig,"step1.pdf")
    
    ax2 = pp.set_ax(fig,label=2) 
    pp.stack(fig,ax1,ax2,d="b")
    pp.savefig(fig,"step2.pdf")

    ax3 = pp.set_ax(fig,label=3,aspect=(2,1))
    pp.stack(fig,ax1,ax3,d="r")
    pp.savefig(fig,"step3.pdf")

    ax4 = pp.set_ax(fig,label=4,aspect=(0.5,1))
    pp.stack(fig,ax2,ax4,d="r")
    pp.savefig(fig,"step4.pdf")

    ax5 = pp.set_ax(fig,label=5,aspect=(1.5,1))
    pp.stack(fig,ax4,ax5,d="r")
    pp.savefig(fig,"step5.pdf")

    ax6 = pp.set_ax(fig,label=6,aspect=(3,1))
    pp.stack(fig,ax2,ax6,d="b")
    pp.savefig(fig,"step6.pdf")

    ax7 = pp.set_ax(fig,label=7,aspect=(1,3))
    pp.stack(fig,ax6,ax7,d="r")

    pp.savefig(fig,"example1.pdf")
