# 编辑器及调试器

编辑器和调试器都属于CodeEditor的内容。

编辑器基于QSciscintilla。

调试器则是一个普通的插件，基于pdb，使用进程间通信作为扩展。



## 使用方法

编辑器的相关事件与编辑器工具栏相连接。当用户在编辑窗口中左右键点击或者操作鼠标滚轮时，工具栏将自动切换到编辑器一侧。在编辑时，为了尽可能增大编辑区域，可以点击选项卡隐藏工具栏，使用右键菜单或者快捷键进行操作。

### 批量注释

选中文本后，按住`Ctrl+/`可以取消注释。不要和我说这两个键离得远——因为右`Ctrl`离'/'很近，按起来极其方便。当然，也可以点击工具栏按钮进行操作。

注释快捷键可以在主界面的设置项中进行设置。

### 缩进与取消缩进

快捷键为Tab/Shift+Tab。也可以点击工具栏相应按钮进行操作。

### 撤销与重做

快捷键暂时为Ctrl+Z和Ctrl+Y。

### 复制、粘贴、剪切、全选

与常见编辑器相同。

### 查找和替换

查找和替换的对话框可以通过`Ctrl+F`调出，既可以替换又可以查找。也可以点击工具栏上选项，对当前文件进行操作。

### 跳转到行
操作可以按Ctrl+G，输入相应行即可。

### 运行
工具栏上有三个运行按钮，意思分别为在IPython中运行、在终端运行和调试。

#### 添加断点
点击左侧，即可添加断点。

### 插入单元格
连续输入三个以上的#号，可以插入单元格运行标记，点击标记可以运行当前单元格。

### 插入运行当前脚本语句。
输入`if __name__=='__main__':`即可插入一个运行标记。
点击它可以在IPython中运行整个文件
按住Ctrl点击可以在控制台运行整个脚本

### 插入变量控件

使用mkvar语句插入

使用标准控件语句插入控件的测试。
测试中涉及到的代码都是可以直接在其他环境中运行的。
为了方便记忆，关键字可以用mkval或者mkvar
保存对话框结果之后，对话框将被销毁。同时，代码也会被改变。
规范：{赋值表达式}{一个‘#’号注释}{mkvar/mkval}{参数list}
例如：
a = 132 #mkvar['m',(0,200),3]
目前支持数字、字符串、bool型不加参数的输入。
如果字符串型变量希望用路径的形式进行选择，则可以采用这样的语句：
p = '' #mkvar ['file_ctrl']
此时将指定用路径选择对话框来改写路径。

#### 限制
- 限制等号左右只有左变量、右常量且为单变量赋值的情况。右侧必须以一个列表式结束。
```python
### 合法的情况：
p = '' # mkvar ['file_ctrl']
a = 132 # mkvar['m',(0,200),3]
### 不合法的情况：非单变量赋值
a,b = ['aaa','bbb']#mkvar['list_ctrl']
### 不合法的情况：左右均为变量
a='hello'
b=a # mkvar
### 不合法的情况：右侧不以列表形式结束。
p = '' # mkvar
```



## 开发过程




