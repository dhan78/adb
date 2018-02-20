
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
#import math
%matplotlib inline

def state_transition(state_name):
    #import pdb; pdb.set_trace();
    if state_name == 'MEV1':
        t = range(10)
        a = np.sin(t) + np.random.rand()
        b = np.cos(t)
        c = np.cos(t) + np.sin(t) * np.random.rand()
        col_values=np.column_stack((t,a,b,c))
        state_pd=pd.DataFrame(col_values, columns=list('tabc'))
        return state_pd
    elif state_name == 'MEV2':
        t = range(10)
        a = 2* np.sin(t) * np.random.rand()
        b = 1/(np.cos(t) +5)
        c = np.sin(t)+ np.cos(t)* np.tan(t)
        c = 1/(a+.01) * b*.1
        col_values=np.column_stack((t,a,b,c))
        state_pd=pd.DataFrame(col_values, columns=list('tabc'))
        return state_pd



# MEV State 1
state1=state_transition(state_name='MEV1')
# MEV State 2
state2=state_transition(state_name='MEV2')
# set the last row as common
state1.iloc[-1,:]=state2.iloc[-1,:]
state1.iloc[0,:]=state2.iloc[0,:]

fig, ax = plt.subplots(1,figsize=(10,4));
plt.suptitle('MEV SubAdditivity');
q=widgets.FloatSlider(min=1,max=9,value=1,description='Quarter')
plt.plot(state1.t, state1.a , state1.t, state1.b, state1.t, state1.c);

def update_plot(q):
    plt.suptitle(str(np.round(q)))
    plt.clf()
    plt.figsize=(10,4)
    plt.suptitle('New MEV change-path')
    state2.iloc[int(q),:]=state1.iloc[int(q),:]
    plt.plot(state2.t, state2.a , state2.t, state2.b, state2.t, state2.c);
    for x,a,b,c in zip(np.round(state2.t),np.round(state2.a,2),np.round(state2.b,2),np.round(state2.c,2)):
        plt.text(x,a,a)
        plt.text(x,b,b)
        plt.text(x,c,c)
    plt.show()


for x,a,b,c in zip(np.round(state1.t),np.round(state1.a,2),np.round(state1.b,2),np.round(state1.c,2)):
    #ax.annotate('%s , %s' %xy, xy=xy, textcoords='data')
    plt.text(x,a,a)
    plt.text(x,b,b)
    plt.text(x,c,c)
widgets.interactive(update_plot,q=q)
