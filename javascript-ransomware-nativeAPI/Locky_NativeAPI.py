# -*- coding:utf-8 -*-
import PyV8
import _winreg
def WScript_create():
    return WScript()
    
class WshShell(PyV8.JSClass): 
    def ExpandEnvironmentStrings(self, uni):
        str=_winreg.ExpandEnvironmentStrings(unicode(uni)) #환경변수 변경
        print '[*] ExpandEnvironmentStrings: ', uni
        print ' -> new: ', str
        return str
    def Run(self,a,b,c):
        print '[*] WshShell.Run '
        print '  - a: ', a
        print '  - b: ', b
        print '  - c: ', c

class XMLHTTP(PyV8.JSClass):
    def send(self):
        print '[*] XMLHTTP.send'
    def open(self, a, b, c):
        print '[*] XMLHTTP.open : '
        print '  - a: ', a
        print '  - b: ', b
        print '  - c: ', c
    
class ADODBStream(PyV8.JSClass):
    def send(self):
        print '[*] ADODBStream.send'
    def open(self):
        print '[*] ADODBStream.open'
    def write(self, a):
        print '[*] ADODBStream.write'
        print '  - a: ',a
    def SaveToFile(self,a,b):
        print '[*] ADODBStream.SaveToFile:'
        print '  - a: ', a
        print '  - b: ', b
    def close(self):
        print '[*] ADODBStream.close'
        
class WScript(PyV8.JSClass):
    def Sleep(self, n):
        print '[*] WScript.Sleep : ',n
    def CreateObject(self,str):
        print '[*] WScript.CreateObject : ',str
        if(str.lower()=='wscript.shell'):
            return WshShell()
        elif(str.lower()=='msxml2.xmlhttp'):
            return XMLHTTP()
        elif(str.lower()=='adodb.stream'):
            return ADODBStream()
        
class NativeAPI(PyV8.JSClass):
    WScript=WScript_create()

ctx=PyV8.JSContext(NativeAPI()) # pyV8 초기화
ctx.enter()
buf=open('details_8f3759.js_vir','rb').read()
ctx.eval(buf)
