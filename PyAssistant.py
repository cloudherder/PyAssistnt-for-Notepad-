#! /usr/bin/env python
#coding=utf-8
#	Programmer: cloudherder
#	E-mail:		cloudherder@126.com
#
#	Copyleft 2015  cloudherder
#
#	Distributed under the terms of the GPL (GNU Public License)
#
#	PyAssistant for Notepad++ is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import re
import os
import inspect
import sys


class PyAssistant():
	def __init__(self,functions={},preDict={},typeList=[]):
		self.fn=functions
		self.preDict=preDict
		self.charcode=-1
		self.curDict={}
		self.curDictKey=[]
		self.parttenDot=re.compile('([\_\w]?[\w\d_\.]*[\(\[\.]?)$')
		self.parttenAny=re.compile('([\_\w]?[\w\d_\.]*)$')
		self.trigChars=['(', '[' ,'.']
		self.typeList=typeList
		self.SwitchFile('')

	def GetPyDict(self,python_script):
		self.curDict=self.preDict
		if type(python_script) is str:
			python_script = python_script.split("\n")
		for line in python_script:
			impok=False
			ks = line.strip().split(' ')
			if (line[0:7] == "import " or line[0:5] == "from " ) :
				line=line.split('#')[0].strip()
				try:
					exec(line)
					impok=True
				except Exception,ex:
						self.fn['write']('%s%s%s%s'%(line,': ',str(ex),"\n"))
				if impok:
					mdls,ns=[],[]
					if line[0:7] == "import ":
						ks1=map(lambda x:x.strip(),line[7:].split(','))
						if len(ks1)>0:
							GetNameSpace(ks1,self.curDict,self.typeList)
					elif line[0:5] == "from ":
						ks1=map(lambda x:x.strip(),line[5:].split(' import '))
						if len(ks1)>1:
							if ks1[1]=='*':
								GetNameSpace([ks1[0]],self.curDict,self.typeList)
							else:
								ks2=ks1[1].split(',')
								GetNameSpace(ks2,self.curDict,self.typeList)

	def SwitchFile(self,args):
		cid=args['bufferID'] if args else self.fn['getCurrentBufferID']()
		file=self.fn['getBufferFilename'](cid)
		if file[-4:]=='.pyw' or file[-3:]=='.py':
			self.fn['autoCSetFillUps'](self.trigChars)
			self.GetPyDict(self.fn['getText']())

	def AutoCSelected(self,args):
		pos=args['position']
		item=args['text']
		txt=self.fn['getCurLine']()
		line=self.fn['lineFromPosition'](pos)
		linestart=self.fn['positionFromLine'](line)
		txt=txt[0:pos-linestart]
		partten=''
		if self.charcode ==46:
			partten=self.parttenDot
		elif self.charcode	in range(48,58) + range(65,91) + range(97,123):
			partten=self.parttenAny
		if partten:
			matches=re.search(partten,txt)
			if matches:
				cmd=matches.group(0)
				startpos=pos-len(cmd)
				self.fn['deleteRange'](startpos,len(cmd))
				self.fn['insertText'](startpos,item)
				self.fn['setCurrentPos'](startpos+len(item))
				self.fn['setAnchor'](startpos+len(item))
		if self.charcode>-1:
			self.charcode=-1

	def DoTips(self,args):
		txt=self.fn['getCurLine']()
		pos=self.fn['getCurrentPos']()
		line=self.fn['lineFromPosition'](pos)
		linestart=self.fn['positionFromLine'](line)
		txt=txt[0:pos-linestart]
		partten=''
		if args['ch']==10: #is \n
			self.fn['gotoPos'](self.fn['positionFromLine'](line-1))
			text1=self.fn['getCurLine']()
			indent=''
			idtp=re.compile('(^\s*)')
			idtm=re.search(idtp,text1)
			if idtm:
				indent=idtm.group(0)
			if ':'==text1.strip()[-1:]:
				indent+="	"
			self.fn['gotoPos'](pos)
			self.fn['addText'](indent)
		elif args['ch'] in [40,46]:	 #40 is ( ;46 is .
			self.charcode=args['ch']
			partten=self.parttenDot
		elif args['ch']	  in range(48,58) + range(65,91) + range(97,123):
			self.charcode=args['ch']
			partten=self.parttenAny
		if partten:
			matches=re.search(partten,txt)
			if matches:
				cmd=matches.group(0)
				self.curDictKey=self.curDict.keys()
				self.curDictKey.sort()
				if args['ch']==46: #is .
					cmd=cmd[:-1]
					if cmd in self.curDictKey or (cmd not in self.curDictKey and  cmd[:cmd.rfind('.')] in self.curDictKey):
						if cmd not in self.curDictKey and  cmd[:cmd.rfind('.')] in self.curDictKey:
							GetNameSpace([cmd],self.curDict,self.typeList)
						self.curDictKey=GetPathChildren(self.curDictKey,cmd,'.')
						self.curDictKey.sort()
						if self.fn['autoCActive']():
							self.fn['autoCCancel']()
						self.fn['userListShow'](3,' '.join(self.curDictKey))
						self.fn['autoCSelect'](cmd)
						self.fn['autoCSetChooseSingle'](True)
				elif args['ch']==40: #is (
					cmd=cmd[:-1]
					if cmd in self.curDictKey:
						if self.curDict[cmd]:
							if self.fn['callTipActive']():
								self.fn['callTipCancel']()
							self.fn['callTipShow'](pos,self.curDict[cmd])
							self.fn['callTipSetPosition'](True)
				else:
					if args['ch']  in range(48,58) or args['ch']  in range(65,91)  or args['ch']  in range(97,123) :
						self.curDictKey=GetPathChildren(self.curDictKey,cmd,'')
						if self.curDictKey:
							if self.fn['autoCActive']():
								self.fn['autoCCancel']()
							self.fn['userListShow'](3,' '.join(self.curDictKey))
							self.fn['autoCSelect'](cmd)
							self.fn['autoCSetChooseSingle'](True)
							
	def ClosingFile(self,args):
		file=self.fn['getBufferFilename'](args['bufferID'])
		if (file[-4:]=='.pyw' or file[-3:]=='.py'):
			self.curDict={}
			
	def Hook(self):
		self.fn['ncallback'](self.ClosingFile, [NOTIFICATION.FILEBEFORECLOSE])
		self.fn['ncallback'](self.SwitchFile, [NOTIFICATION.FILEOPENED,NOTIFICATION.BUFFERACTIVATED])
		self.fn['callback'](self.DoTips,[SCINTILLANOTIFICATION.CHARADDED])
		self.fn['callback'](self.AutoCSelected,[SCINTILLANOTIFICATION.USERLISTSELECTION])
		self.fn['autoCSetIgnoreCase'](False)
		self.fn['autoCSetMaxWidth'](30)
		self.fn['autoCSetMaxHeight'](7)
		self.fn['write']("\nPyAssistant has hooked!\n")


def GetPathChildren(arr=[],path='',splitor='.'):
	ret=[]
	if not path.strip():
		pp='[^'+splitor+'.]*$'
	else:
		pp=path+splitor+'[^'+splitor+'.]*$'
	p=re.compile(pp)
	for n in arr:
		if n.strip():
			m=re.match(p,n)
			if m  and  n:
				ret.append(n)
	return ret

def Import(name):
	obj=''
	try:
		obj=__import__(name,{},{},['*'])
	except Exception,ex:
		self.fn['write']('%s%s%s'%('Loading ',nm," is failed!\n"))
	return obj

def GetNameSpace(mdls=[],dict={},typeList=[]):
	for k in mdls:
		mdl=map(lambda x:x.strip(),k.split(' as '))
		nm=mdl[1] if len(mdl)>1 else mdl[0]
		pnm='' if len(mdl)>1 else mdl[0]+'.'
		obj=Import(nm)
		if obj:
			GetNameSpaceInfo(pnm,obj,dict,typeList,1)
			
def GetNameSpaceInfo(parentName,object,dict={},typeList=[],istop=0):
	ctp=getType(object,typeList)
	if ctp: 
		name=''
		try:
			name=object.__name__
		except:
			pass
		if name and not name.startswith('_') :# and objname.endswith('_')):
			if parentName  and parentName[:-1]!=name:
				objname=parentName+'.'+name
			else :
				objname=name
			if ctp in ['Function,Routine,Method,Generatorfunction,Code']: 
				try:
					tip=inspect.getcallargs(object)
				except:
					tip=inspect.getdoc(object)
			else:
				tip=inspect.getdoc(object)
			d={ objname:tip}
			dict.update(d)
			if ctp in ['Class','Module','Generator']:
				# name=objname if istop else name
				for nm,obj in inspect.getmembers(object):
					if getType(object,typeList) and not nm.startswith('_')	and nm not in ['os','types','string']:
						GetNameSpaceInfo(objname,obj,dict,typeList,0)

def getType(obj,typeList=[]):
	ret=''
	if 'abstract' in typeList and inspect.isabstract(obj):
		ret='Abstract'
	elif 'builtin'	in typeList and inspect.isbuiltin(obj):
		ret='Builtin'
	elif 'code' in typeList and inspect.iscode(obj):
		ret='Code'
	elif 'class' in typeList and inspect.isclass(obj):
		ret='Class'
	elif 'function' in typeList and inspect.isfunction(obj):
		ret='Function'
	elif 'datadescriptor' in typeList and inspect.isdatadescriptor(obj):
		ret='Datadescriptor'
	elif 'generator' in typeList and inspect.isgenerator(obj):
		ret='Generator'
	elif 'generatorfunction' in typeList and inspect.isgeneratorfunction(obj):
		ret='Generatorfunction'
	elif 'getsetdescriptor' in typeList and inspect.isgetsetdescriptor(obj):
		ret='Getsetdescriptor'
	elif 'method' in typeList and inspect.ismethod(obj):
		ret='Method'
	elif 'module' in typeList and inspect.ismodule(obj):
		ret='Module'
	elif 'routine' in typeList and inspect.isroutine(obj):
		ret='Routine'
	elif 'traceback' in typeList and inspect.istraceback(obj):
		ret='Traceback'
	return ret

def Hook():
	pa.Hook()


sys.stdout = console
objTypes=['class','module','routine','function','method','builtin','generator','abstract','code','datadescriptor','generatorfunction', 'getsetdescriptor']#
file=os.path.join(os.path.dirname(os.path.realpath(__file__)),'PyAssistantDict.py')
if not os.path.exists(file):
	f=open(file,'w')
	f.write("preDict={}\n")
	f.close()
if __name__ == "__main__":
	if len(sys.argv)>1 and sys.argv[0][sys.argv[0].rfind('PyAssistant.py'):len(sys.argv[0])]=='PyAssistant.py':
		f=open(file,'w')
		f.write("preDict={\n")
		mdls=sys.argv[1].split(',')
		for mdl in mdls:
			tdict={}
			if mdl:
				GetNameSpace([mdl],tdict,objTypes)
				ks=tdict.keys()
				ks.sort()
				f.write('%s%s%s%s'%("	'",mdl,"':'","',\n"))
				for k in ks:
					f.write('%s%s%s%s%s'%("	'",k,"':'''", tdict[k] if tdict[k] else '' ,"''',\n"))
		f.write("}\n")				
		f.close()
	else:
		from Npp import *
		from  PyAssistantDict import preDict
		functions={'msgbox':notepad.messageBox,#console.write
			'getCurrentBufferID':notepad.getCurrentBufferID,
			'getBufferFilename':notepad.getBufferFilename,
			'autoCSetFillUps':editor.autoCSetFillUps,
			'addText':editor.addText,
			'getText':editor.getText,
			'insertText':editor.insertText,
			'getCurLine':editor.getCurLine,
			'gotoPos':editor.gotoPos ,
			'getLength':editor.getLength,
			'getTextRange':editor.getTextRange,
			'getCharAt':editor.getCharAt,
			'getCurrentPos':editor.getCurrentPos,
			'lineFromPosition':editor.lineFromPosition,
			'positionFromLine':editor.positionFromLine,
			'autoCActive':editor.autoCActive,
			'autoCCancel':editor.autoCCancel,
			'userListShow':editor.userListShow,
			'autoCSetChooseSingle':editor.autoCSetChooseSingle,
			'autoCSetIgnoreCase':editor.autoCSetIgnoreCase,
			'autoCSelect':editor.autoCSelect,
			'autoCSetMaxWidth':editor.autoCSetMaxWidth,
			'autoCSetMaxHeight':editor.autoCSetMaxHeight,
			'callTipActive':editor.callTipActive,
			'callTipCancel':editor.callTipCancel,
			'callTipSetPosition':editor.callTipSetPosition,
			'callTipShow':editor.callTipShow,
			'deleteRange':editor.deleteRange,
			'setCurrentPos':editor.setCurrentPos,
			'setAnchor':editor.setAnchor,
			'callback':editor.callback,
			'callbackSync':editor.callbackSync,
			'clearCallbacks':editor.clearCallbacks,
			'ncallback':notepad.callback,
			'nclearCallbacks':notepad.clearCallbacks,
			'write':console.write,
		}
		for k in dir(__builtins__):
			if not (k.startswith('_') and k.endswith('_') ) and k not in ['print']:
				GetNameSpaceInfo('',eval(k),preDict,objTypes)
		pa=PyAssistant(functions,preDict,objTypes)
		Hook()


