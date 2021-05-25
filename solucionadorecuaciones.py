from sympy import Eq, solve
from sympy.abc import v,w,x,y,z
sol = solve([ Eq(1*v+1*w+1*x+1*y+1*z,1),
              Eq(.4*v-.8*w+.3*x+.4*y+.2*z, 0),
              Eq(.3*v+.4*w-.9*x+.3*y+.4*z, 0),
              Eq(.1*v+.3*w-.9*y+.3*z,0),
              Eq(.1*w-.9*z,0)])
print(sol)
#{v: 0.243609022556391, w: 0.304511278195489, x: 0.278195488721804, y: 0.139849624060150, z: 0.0338345864661654}