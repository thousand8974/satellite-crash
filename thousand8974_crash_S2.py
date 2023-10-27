from vpython import *
#Web VPython 3.2

ball1 = sphere(radius = 0.5*65.5e-3, make_trail = True)
ball2 = sphere(radius = 0.5*65.5e-3, make_trail = True, pos = vec(0.3, -0.1*65.5e-3, 0), color = color.red)

ball1.v = vec(1, 0, 0)
ball2.v = vec(0, 0, 0)
ball1.m = 0.41
ball2.m = 0.21
ball1.f = vec(0, 0, 0)
ball2.f = vec(0, 0, 0)
e = 0.99
tot_energy = 0.5*ball1.m*mag(ball1.v)**2 + 0.5*ball2.m*mag(ball2.v)**2

t = 0
dt = 0.01

traj = gcurve()
en_traj = gcurve(color = color.cyan)

scene.autoscale = True
scene.range = 1
def collision(b1, b2, e):
    c = b1.pos - b2.pos
    c_hat = norm(c)
    dist = mag(c)
    v_relm = dot(b1.v - b2.v, c_hat)
    if v_relm > 0:
        return False
    
    if dist < b1.radius + b2.radius:
        j = -(1+e)*v_relm
        j = j/(1/b1.m+1/b2.m)
        b1.v += j*c_hat/b1.m
        b2.v -= j*c_hat/b2.m
    else:
        return False
        

while t < 10:
    rate(100)
    colcheck = collision(ball1, ball2, e)
    if colcheck == True:
        print("Collision")
    
    ball1.v += ball1.f/ball1.m*dt
    ball2.v += ball2.f/ball2.m*dt
    ball1.pos += ball1.v*dt
    ball2.pos += ball2.v*dt
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2 + 0.5*ball2.m*mag(ball2.v)**2
    
    traj.plot(pos = (t, mag(ball1.v)))
    en_traj.plot(pos = (t, tot_energy))
    t += dt
