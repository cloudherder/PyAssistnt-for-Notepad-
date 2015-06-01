	Readme of PyAssistant
	
	English Version（中文版见后）
	
	PyAssistant  for Notepad++ is free software; you can redistribute it and/or modify it under the terms of 
the GNU General Public License as published by the Free Software Foundation; either version 2 of the 
License, or (at your option) any later version.
 
	PyAssistnt is python script that based on the PythonScript  , PythonScript is a plugin for Notepad++. 
The purpose of PyAssistant  is  when you write Python code with Notepad + +, to provide you with 
dynamic auto-complete and auto-indent feature.
 
	1. install
	1.1 Installing the PythonScript for Notepad++.You can use Main Menu->Plugins-> Plugins Manager 
to install it, or download  it from<http://sourceforge.net/projects/npppythonscript/?source=directory>
and manual install it.
	1.2.Download PyAssistant.zip 
	1.3Unzip PyAssistant.zip to a directory Notepad Install path/plugins/PythonScript/scripts .
	1.4 Click Main Menu->Python Script->Scripts->PyAssistant to run .
	if you open the Python console of PythonScript at before  , PyAssistant is successful will display on 
console:

	PyAssistant has hooked!
	
	1.5  Click Main Menu->Python Script->Scripts->UnPyAssistant to cancel  PyAssistant bind with 
notepad++.PyAssistant is successful will display  on console:

	PyAssistant has unhooked!
	
	2. Attention
	2.1 AutoIndent we use tab completion of additions to the PyAssistan.
	2.2 Dynamic AutoComplete, PythonScript cannot normally import modules are also invalid.The 
module name raise  error at import ,will display on pyhon console .Now ,It known to be unable to import 
modules,include sqllite3 and wx.
	2.3 It raise error on import  that PythonScript modules can be run under Python to generate help 
information import to the  file PyAssistantDict.py, for PyAssistant use. Usage:
	
       python.exe PyAssistant.py module 1[, module 2, ...]
	
	3.Files
	These files of PyAssistant include：
	PyAssistant.py	main program file
	UnPyAssistant.py	cancel  PyAssistant bind with Notepad++
	PyAssistantDict.py  module information ,create by main program.If raise error about 
PyAssistantDict.py, please delete PyAssistantDict.py and run PyAssistant again.

			中文版说明

	PyAssistnt是在PythonSctipt基础上运行的脚本，PythonScript是Notepad++的一个插件。PyAssistant
的目的，是当你用Notepad++编写python代码时，为你提供动态自动完成和自动缩进的功能。
	
	1.安装
	1.1安装PythonScript for Notepad++。你可以通过主菜单->插件->插件管理器 安装它，也可以在
<http://sourceforge.net/projects/npppythonscript/?source=directory >下载手动安装。
	1.2 下载PyAssistant.zip。
	1.3 解压PyAssistant.zip到目录Notepad path/plugins/PythonScript/scripts.
	1.4 点击 主菜单->插件->Python Script->Scripts->PyAssistant 运行之。
	如果你在这之前打开了PythonScript的python控制台，PyAssistant运行成功会在控制台显示：
	
    PyAssistant has hooked!
    
	1.5 点击 主菜单->插件->Python Script->Scripts->UnPyAssistant取消PyAssistant与Notepad++的绑定。
UnPyAssistant运行成功会在控制台显示：

    PyAssistant has unhooked!
    
    2.注意事项
    2.1 PyAssistan新增加缩进是用tab完成的。
    2.2 动态自动完成，对于PythonScript不能正常import的模块也是无效的。import出错的模块名字，将显示
 在python控制台。前已知不能import的模块有：sqllite3,wx。
   2.3在PythonScript中import出错的模块，可以在python之下运行，生成模块信息导入到PyAssistantDict.py
文件中，供PyAssistant使用。用法是:

     python.exe PyAssistant.py 模块1[,模块2,...]
	
	3.文件
	PyAssistant的文件包括：
	PyAssistant.py	主程序文件
	UnPyAssistant.py 取消PyAssistant与Notepad++的绑定
	PyAssistantDict.py  模块信息文件，由主程序生成。如果有与PyAssistantDict.py有关的错误，请删除
PyAssistantDict.py文件，并再次运行PyAssistant。
   
