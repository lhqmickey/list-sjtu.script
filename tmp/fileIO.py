#!/usr/bin/python
template = open('inclTemplate.incl','r')
incl = open('test.incl','w')
incl.write(template.read())
incl.write("I Love %s"%"CaiC")
template.close();
incl.close();
