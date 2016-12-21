# coding:utf-8
"I am 6'2\" tall." # 将字符串中的双引号转义
'I am 6\'2" tall.' # 将字符串中的单引号转义
# \t是tab缩进符 缩进8个字节
tabby_cat = "\tI'm tabbed in."
# \n是换行符 Enter 换行
persian_cat = "I'm split\non a line."
# \\转义把反斜杠打印出来
backslash_cat = "I'm \\ a \\ cat."
# """三个双引号包裹 里面单引号 双引号 转义字符不需要考虑外层包裹
fat_cat = """
I'll do a "list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
