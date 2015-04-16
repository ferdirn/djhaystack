from fabric.api import *

@task
def hello(who='world!'):
    '''Say hello'''
    hi()
    print "Hello {who}".format(who=who)

def hi():
    '''Say hi'''
    print 'Hi'