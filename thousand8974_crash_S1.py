from vpython import *
#Web VPython 3.2

ball1 = sphere(radius = 0.5 * 65.5e-3, make_trail = True)
ball2 = sphere(radius = 0.5 * 65.5e-3, make_trail = True, pos = vec(1, 0.5*65.5e-3, 0), color = color.red)

ball1.v = vec(1, 0, 0)
ball2.v = vec(0, 0, 0)
ball1.m = 0.21
ball2.m = 0.21
ball1.f = vec(0, 0, 0)
ball2.f = vec(0, 0, 0)
e = 1.0
tot_energy = 0.5 * ball1.m * mag(ball1.v)**2 + 0.5*ball2.m*mag(ball2.v)**2

t = 0
dt = 0.01
traj = gcurve()
en_traj = gcurve(color = color.cyan)

scene.autoscale = True
scene.range = 1

def collision(b1, b2, e):
    c = b2.pos - b1.pos
    c_hat = norm(c)
    dist = mag(c)
    if dot(b1.v - b2.v, c_hat) < 0:
        return False
    v1_c = dot(b1.v, c_hat)*c_hat
    v1_p = b1.v - v1_c
    v2_c = dot(b2.v, c_hat)*c_hat
    v2_p = b2.v - v2_c
    tot_m = b1.m + b2.m
    
    if dist < b1.radius + b2.radius:
        v1 = ((b1.m-e*b2.m)*v1_c + (1+e)*b2.m*v2_c) / tot_m
        v2 = ((b2.m-e*b1.m)*v2_c + (1+e)*b1.m*v1_c) / tot_m
        b1.v = v1 + v1_p
        b2.v = v2 + v2_p
        return True
    else:
        return False
            
while t < 10:
    rate(30)
    colcheck = collision(ball1, ball2, e)
    ball1.v += ball1.f / ball1.m*dt
    ball2.v += ball2.f / ball2.m*dt
    ball1.pos += ball1.v*dt
    ball2.pos += ball2.v*dt
    
    tot_energy = 0.5 * ball1.m * mag(ball1.v)**2 + 0.5*ball2.m*mag(ball2.v)**2
    
    traj.plot(pos = (t, mag(ball1.v)))
    en_traj.plot(pos = (t, tot_energy))
    t += dt