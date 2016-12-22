#coding:utf-8
name = raw_input("你的名字：")
age = raw_input("你的年龄：")
mingxing = raw_input("你喜欢的明星是谁？")
print "你的名字是 %s, %s岁了，Fan上了%s，还为他写了一首歌！" % (name, age, mingxing)
print "python -m pydoc raw_input"
print """""raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading."""""
