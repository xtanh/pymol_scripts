from pymol.cgo import *    # get constants
from pymol import cmd
from pymol.vfont import plain

import math

class Counter:
   def __init__(self):
       self.state = 1
counter = Counter()

def show_x(length=10.0):
    i,j,k = 10,0,0
    width = 0.3 # cylinder width
    r,g,b = 1.0, 0, 0
    x,y,z = float(0), float(0), float(0)
    i,j,k = float(i), float(j), float(k)
    r,g,b = float(r), float(g), float(b)
    width = float(width)
    length = float(length)

    h = 2.5 # cone hight
    d = width * 2* 1.618 # cone base diameter

    x1,y1,z1 = (0,0,0)
    x2,y2,z2 = (x+i*length,y+j*length,z+k*length)

    obj = [
        CYLINDER, x1, y1, z1, x2, y2, z2, width, 1.0, 1.0, 1.0, r, g, b,
        CONE,   x2, y2, z2, h+x2, y2, z2, d, 0.0, r, g, b, r, g, b, 1.0, 1.0,
        ]

    cyl_text(obj,plain,[h+x2,y2,z2],'X',0.20,axes=[[0,3,0],[0,0,3],[3,0,0]])

    cmd.delete('axis_X')
    cmd.load_cgo(obj,'axis_X')
    # cmd.load_cgo(obj,'axis_X'+str(counter.state))
    counter.state += 1

def show_y(length=10.0):
    i,j,k = 0,10,0
    width = 0.3 # cylinder width
    r,g,b = 0,1.0,0
    x,y,z = float(0), float(0), float(0)
    i,j,k = float(i), float(j), float(k)
    r,g,b = float(r), float(g), float(b)
    width = float(width)
    length = float(length)

    h = 2.5 # cone hight
    d = width * 2* 1.618 # cone base diameter

    x1,y1,z1 = (0,0,0)
    x2,y2,z2 = (x+i*length,y+j*length,z+k*length)

    obj = [
        CYLINDER, x1, y1, z1, x2, y2, z2, width, 1.0, 1.0, 1.0, r, g, b,
        CONE,   x2, y2, z2, x2, h+y2, z2, d, 0.0, r, g, b, r, g, b, 1.0, 1.0,
        ]

    cyl_text(obj,plain,[x2,h+y2,z2],'Y',0.20,axes=[[0,0,3],[3,0,0],[0,3,0]])
    cmd.delete('axis_Y')
    cmd.load_cgo(obj,'axis_Y')
    # cmd.load_cgo(obj,'axis_Y'+str(counter.state))
    counter.state += 1

def show_z(length=10.0):
    i,j,k = 0,0,10
    width = 0.3 # cylinder width
    r,g,b = 0, 0, 1.0
    x,y,z = float(0), float(0), float(0)
    i,j,k = float(i), float(j), float(k)
    r,g,b = float(r), float(g), float(b)
    width = float(width)
    length = float(length)

    h = 2.5 # cone hight
    d = width * 2* 1.618 # cone base diameter

    x1,y1,z1 = (0,0,0)
    x2,y2,z2 = (x+i*length,y+j*length,z+k*length)

    obj = [
        CYLINDER, x1, y1, z1, x2, y2, z2, width, 1.0, 1.0, 1.0, r, g, b,
        CONE,   x2, y2, z2, x2, y2, h+z2, d, 0.0, r, g, b, r, g, b, 1.0, 1.0,
        ]

    cyl_text(obj,plain,[x2,y2,h+z2],'Z',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])
    cmd.delete('axis_Z')
    cmd.load_cgo(obj,'axis_Z')
    # cmd.load_cgo(obj,'axis_Z'+str(counter.state))
    counter.state += 1





from chempy import cpv
class PutCenterCallback(object):
    prev_v = None

    def __init__(self, name, corner=0):
        self.name = name
        self.corner = corner
        self.cb_name = cmd.get_unused_name('_cb')

    def load(self):
        cmd.load_callback(self, self.cb_name)

    def __call__(self):
        if self.name not in cmd.get_names('objects'):
            import threading
            threading.Thread(None, cmd.delete, args=(self.cb_name,)).start()
            return

        v = cmd.get_view()
        if v == self.prev_v:
            return
        self.prev_v = v

        t = v[12:15]

        if self.corner:
            vp = cmd.get_viewport()
            R_mc = [v[0:3], v[3:6], v[6:9]]
            off_c = [0.15 * v[11] * vp[0] / vp[1], 0.15 * v[11], 0.0]
            if self.corner in [2,3]:
                off_c[0] *= -1
            if self.corner in [3,4]:
                off_c[1] *= -1
            off_m = cpv.transform(R_mc, off_c)
            t = cpv.add(t, off_m)

        z = -v[11] / 30.0
        m = [z, 0, 0, 0, 0, z, 0, 0, 0, 0, z, 0, t[0] / z, t[1] / z, t[2] / z, 1]
        cmd.set_object_ttt(self.name, m)

def axes(name='axes'):
    '''
DESCRIPTION

    Puts coordinate axes to the lower left corner of the viewport.
    '''
    from pymol import cgo

    cmd.set('auto_zoom', 0)

    w = 0.06 # cylinder width
    l = 0.75 # cylinder length
    h = 0.25 # cone hight
    d = w * 1.618 # cone base diameter

    obj = [cgo.CYLINDER, 0.0, 0.0, 0.0,   l, 0.0, 0.0, w, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0,
           cgo.CYLINDER, 0.0, 0.0, 0.0, 0.0,   l, 0.0, w, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
           cgo.CYLINDER, 0.0, 0.0, 0.0, 0.0, 0.0,   l, w, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0,
           cgo.CONE,   l, 0.0, 0.0, h+l, 0.0, 0.0, d, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0,
           cgo.CONE, 0.0,   l, 0.0, 0.0, h+l, 0.0, d, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0,
           cgo.CONE, 0.0, 0.0,   l, 0.0, 0.0, h+l, d, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0]

    PutCenterCallback(name, 1).load()
    cmd.load_cgo(obj, name)


cmd.extend('axes', axes)
cmd.extend('x', show_x)
cmd.extend('y', show_y)
cmd.extend('z', show_z)
