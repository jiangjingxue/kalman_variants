from numpy import ones 

def eulers_method(x,F,u,dt,dim):
    '''
    Accepts 
    - x: the most recent n by 1 state estimate vector 
    - F: the continuous n by m process model matrix 
    - u: the m by 1 control inputs vector 
    - dt: scalar time step delta t
    - dim: dimension of the state estimate vector
    -------
    Returns
    - Predicted state estimate vector to the next time step
    '''
    x_next = ones((dim, 1))
    x_next = x + ( F @ u ) * dt 
    return x_next 

def runge_kutta_second_order(x,y,h,f):
    k_1 = f(x,y)
    k_2 = f(x + h, y + h * k_1)
    y_next = y + h * ( 0.5 * k_1 + 0.5 * k_2)
    return y_next

def runge_kutta_fourth_order(x,y,h,f):
    k_1 = f(x,y)
    k_2 = f(x + 0.5 * h , y + 0.5 * h * k_1)
    k_3 = f(x + 0.5 * h , y + 0.5 * h * k_2)
    k_4 = f(x + h , y + h * k_3)
    y_next= y + (h / 6.0) * (k_1 + 2.0 * k_2 + 2.0 * k_3 + k_4)
    return y_next

