#!/usr/bin/python3

sum = 0

N = int(input("몇개의 숫자를 입력할건가요? : "))
print("입력한 숫자만큼 숫자를입력")

for i in range(N):
   a =  int(input())
   sum += a

print("총합: {}" .format(sum))
print("평균: ", sum / N)


