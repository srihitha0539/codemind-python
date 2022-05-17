A,B,C=map(int,input().split())
s=(A+B+C)/2
import math
Area=math.sqrt(s*(s-A)*(s-B)*(s-C))
print('%0.2f'%Area)