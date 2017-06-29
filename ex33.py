# -*- coding: utf-8 -*-

nn = raw_input("숫자를 입력하시오>")
print nn
i = 0
numbers = []

while i < float(nn):
    print "꼭대기에서 i는 %d" % i
    numbers.append(i)

    i = i + 1
    print "숫자는 이제: ", numbers
    print "바닥에서 i는 %d" % i


print "숫자: "

for num in numbers:
    print num