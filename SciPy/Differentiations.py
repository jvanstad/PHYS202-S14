def twoPtForwardDiff(x,y):
    #Subtracts the difference from current value from the one in front of it 
    #for both x and y and return change y/ change x. (Forward difference).
    #Use backwards difference for last point
    dydx=np.zeros(y.shape,float)
    dydx[0:-1]=(y[1:]-y[:-1])/(x[1:]-x[:-1])
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx
def twoPtCenteredDiff(x,y):
    #Takes the difference between point behind and point in front for y and x. 
    #returns change y/change x. Last point uses forward backwards difference. 
    #first uses forward diff.
    dydx=np.zeros(y.shape,float)
    dydx[1:-1]=(y[2:]-y[:-2])/(x[2:]-x[:-2])
    dydx[0]=(y[1]-y[0])/(x[1]-x[0])
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx
def FourPtCenteredDif(x,y):
    dydx=np.zeros(y.shape,float)
    #formula for allowable Four point diff
    h=x[2]-x[1]
    dydx[2:-2]=(y[:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(12*h)
    #Use center diff for second to last point
    dydx[1]=(y[2]-y[0])/(x[2]-x[0])
    dydx[-2]=(y[-1]-y[-3])/(x[-1]-x[-3])
    #Forward diff for first
    dydx[0]=(y[1]-y[0])/(x[1]-x[0])
    #Backward diff for last
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx