#13222319810101****
nID = ''
while 1:
  nID = raw_input("Input your id plz")
  if len(nID) != len("13222319810101****"):
    print 'wring length of id,input again'
  else:
    break
  
print 'your id is %s' % (nID)


nAge = int(raw_input("input your age plz:\n"))
if nAge > 0 and nAge < 120:
  print 'thanks!'
else:
  print 'bad age'
print 'your age is %d\n' % nAge


fWeight = 0.0
fWeight = float(raw_input("input your weight\n"))
print 'your weight is %f' % fWeight


