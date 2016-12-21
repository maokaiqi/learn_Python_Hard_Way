# coding:utf-8
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# * 10就是把前面的字符串重复打印10次
print "." * 10 # what'd that do ?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# 字符串拼接，用逗号不会被打印出来，作用是下面一句会接着这一句，而不会换行
print end1 + end2 + end3 + end4 + end5 + end6,
# 字符串拼接
print end7 + end8 + end9 + end10 + end11 + end12

