# -*- coding: utf-8 -*-
# 源码https://github.com/SavinaRoja/PyUserInput

# import the module
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# instantiate an mouse object
m = PyMouse()
k = PyKeyboard()

# move the mouse to int x and int y (these are absolute positions)
# m.move(570L, 413L)

# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
m.click(1106L, 43L, 1)

# get the screen size
# print m.screen_size()
# (1024, 768)

# get the mouse position
print m.position()
# (500, 300)

# x_dim, y_dim = m.screen_size()
# print x_dim,y_dim
# m.click(x_dim/2, y_dim/2, 1)
# k.tap_key('l',n=22,interval=1) 
k.type_string('o World!')

##enter失效，是bug，官方代码未修复
# k.press_key("Enter") 
# k.release_key("Enter")
k.tap_key("Enter",n=2,interval=1)
# k.tap_key("Enter")