# by luffycity.com
# s = "伊丽莎白鼠"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# # print(s[5]) # 索引不能超过边界
#
# print(s[-1]) # 倒数第一个
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])

s = "伊丽莎白鼠的溜肥肠还有挖掘机"
#切片 [起始位置: 结束位置] 1.顾头不顾尾, 2.从左往右切
print(s[1:3])   # 从1切到3. 但是取不到3  [1,3)
print(s[1:]) # 从1开始切. 切到结尾
print(s[:2]) # 从头切到2
print(s[:]) # 从头到尾
print(s[-3:-1]) # 只能从左往右切

# 给出第三个参数来控制方向,第三个参数叫步长
# print(s[-1:-3:-1]) # - 表示反方向. 从右往左切

# print(s[4:10:3])
# print(s[-3:-9:-2])