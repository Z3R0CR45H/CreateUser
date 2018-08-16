import win32net
import win32netcon

shinfo={}

shinfo['netname']='python test'
shinfo['type']=win32netcon.STYPE_DISKTREE
shinfo['remark']='data files'
shinfo['permissions']=0
shinfo['max_uses']=-1
shinfo['current_uses']=0
shinfo['path']= r"\\csh-instruct-fp\users$\students\2017\test"
shinfo['passwd']=''
server='csh-instruct-fp'

win32net.NetShareAdd(server,2,shinfo)
