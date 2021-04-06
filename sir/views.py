
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from itertools import product

def sir(request):
	return render(request,"sir.html")


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        sepal_length = float(request.POST.get('sucep1'))
        suceptibles = float(request.POST.get('sepal_length'))
        recovered = float(request.POST.get('petal_length'))
        time = float(request.POST.get('petal_width'))
        
        beta = 0.16793
        gamma = 0.0378
        S0=suceptibles
        R0 = recovered
        I0=sepal_length
        t0=0
        t1=time
    #def SIR(S0,I0,R0,t0, t1, beta, gamma):
        N=S0+R0+I0; #initialization
        S=S0; 
        R=R0; 
        I=I0;
        
        SS=[S0]; #updating the function
        RR=[R0]; 
        II=[I0];
        tt=[t0];
        
        dt=1; #time step
        t=t0
        
        while t <= t1:
            dS=-beta*S*I/N
            dI=beta*S*I/N-gamma*I
            dR=gamma*I
            S=S+dt*dS;
            I=I+dt*dI;
            R=R+dt*dR;
            SS.append(S); II.append(I); RR.append(R)
            t=t+dt;
            tt.append(t)
        #return(SS,II,RR,tt)
        oo=II.index(max(II));
        N=(II[0]+RR[0]+SS[0]);
        tmax=tt[oo]; Imax=II[oo];
        inftot = RR[-1]/N;

        tmax, Imax/N*100,inftot*100
            
                
                
        return JsonResponse({'sepal_length': Imax/N*100 ,
                                'sepal_width': tmax,'petal_length': inftot*100})


    