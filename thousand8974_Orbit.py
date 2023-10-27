from vpython import *
#Web VPython 3.2

sf = 6

t = 0
dt = 60*60

G = 6.673e-11
r = 384400000
Earth = sphere(pos = vector(0, 0, 0), radius = sf * 6400000, texture = textures.earth)
Moon = sphere(pos = vec(r, 0, 0), radius = sf*1737000, color = color.white, make_trail = True)

Earth.mass = 7.972e24
Moon.mass = 7.36e22

vi = sqrt(G * Earth.mass / r**1)
Moon.v = vec(0, vi * 0.7, 0)
Earth.v = -Moon.v * Moon.mass / Earth.mass

k_graph = gcurve(color = color.cyan)
u_graph = gcurve(color = color.green)
ku_graph = gcurve(color = color.black)

scene.waitfor('click')

while t < 10*365*24*60*60:
    rate(100)
    r = Moon.pos - Earth.pos
    Moon.f = -G * Earth.mass * Moon.mass / mag(r)**2 * norm(r)
    Earth.f = -Moon.f
    
    Moon.v = Moon.v + Moon.f / Moon.mass * dt
    Moon.pos += Moon.v * dt
    k = 0.5 * Moon.mass * mag(Moon.v) ** 2
    u = -G * Earth.mass * Moon.mass/mag(Moon.pos)
    k_graph.plot(t/60/60/24, k)
    u_graph.plot(t/60/60/24, u)
    ku_graph.plot(t/60/60/24, k + u)
    if mag(r) < Earth.radius + Moon.radius:
        print(t/60/60/24)
        break
    
    t += dt

