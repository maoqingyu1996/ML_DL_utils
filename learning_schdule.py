def lr_schedule_(t, T, init_lr):
    # half
    if t < 1/20*T:
        return init_lr
    elif t < 1/8*T:
        return init_lr/2
    elif t < 1/4*T:
        return init_lr/4
    elif t < 3/8*T:
        return init_lr/8
    elif t < 1/2*T:
        return init_lr/10
    elif t < 5/8*T:
        return init_lr/20
    elif t < 3/4*T:
        return init_lr/80
    return init_lr/200
    
    
    
def lr_schedule_cosdecay(t,T,init_lr):
    lr=0.5*(1+math.cos(t*math.pi/T))*init_lr
    return lr
