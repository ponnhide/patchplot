import os 
import io
import sys 
import copy
import pickle
import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt  

#default setting
tmp    = io.BytesIO()
fonts  = [font.split("/")[-1] for font in fm.findSystemFonts()]
margin = 0.25

if "Helvetica.ttf" in fonts:
    matplotlib.rcParams['font.family'] = "Helvetica"
elif "Arial" in fonts:
    matplotlib.rcParams['font.family'] = "Arial"
else:
    pass

def set_fig(figsize=(4,4)):
    fig = plt.figure(figsize=figsize)
    return fig

def set_ax(fig,aspect=(1,1),label=1,fit=True):
    global margin
    ax = fig.add_axes([0.15,0.15,0.7*aspect[0]+(aspect[0]-1)*margin, 0.7*aspect[1]+(aspect[0]-1)*margin],label=label) 
    ax.tick_params(labelsize=14,pad=5)
    ax.aspect = [0.7*aspect[0]+(aspect[0]-1)*margin,0.7*aspect[1]+(aspect[1]-1)*margin]
    pos    = ax.get_position()
    ax.pos = [pos.x0,pos.y0,pos.x1,pos.y1]
    return ax

def stack(fig,ax_base,ax_target,d="b",label_pos="left",am=[0,0],ratio=(1,1)):
    global margin
    max_x = 0
    min_y = 0
    base_pos   = ax_base.pos
    aspect     = ax_target.aspect
    target_pos = ax_target.pos
    
    if d == "r":
        new_pos = [base_pos[2] + margin,  base_pos[1], aspect[0], aspect[1]]  
    elif d == "b":
        new_pos = [base_pos[0], base_pos[1] - margin - aspect[1], aspect[0], aspect[1]] 
    elif d == "l":
        new_pos = [base_pos[2] - margin - aspect[0], base_pos[1], aspect[0], aspect[1]]  
    elif d == "t":
        new_pos = [base_pos[0], base_pos[1] + ax_base.aspect[1] + margin, aspect[0], aspect[1]]  

    else:
        new_pos = target_pos
    
    if label_pos == "left":
        ax_target.set_position([new_pos[0]-am[0], new_pos[1]+am[1], new_pos[2]*ratio[0], new_pos[3]*ratio[1]])
    else:
        ax_target.set_position([new_pos[0]-0.5*margin-am[0], new_pos[1]+am[1], new_pos[2]*ratio[0], new_pos[3]*ratio[1]])

    ax_target.pos = [new_pos[0], new_pos[1], new_pos[0]+new_pos[2], new_pos[1]+new_pos[3]] 

def savefig(fig,name):
    fig.savefig(name,bbox_inches="tight")

def tmp_store(fig):
    global tmp
    tmp.close()
    tmp = io.BytesIO() 
    pickle.dump(fig, tmp)

def reset():
    global tmp
    tmp.seek(0)
    return pickle.load(tmp)

if __name__ == "__main__": 
    fig = set_fig()
    ax1 = set_ax(fig,label=1) 
    
    ax2 = set_ax(fig,label=2) 
    stack(fig,ax1,ax2,d="b")
    
    ax3 = set_ax(fig,label=3,aspect=(2,1))
    stack(fig,ax1,ax3,d="l")

    ax4 = set_ax(fig,label=4,aspect=(0.5,1))
    stack(fig,ax2,ax4,d="l")
    
    ax5 = set_ax(fig,label=5,aspect=(1.5,1))
    stack(fig,ax4,ax5,d="l")

    ax6  = set_ax(fig,label=6,aspect=(3,1))
    stack(fig,ax2,ax6,d="b")

    ax7 = set_ax(fig,label=7,aspect=(1,3))
    stack(fig,ax6,ax7,d="l")
    
    savefig(fig,"test.pdf")
