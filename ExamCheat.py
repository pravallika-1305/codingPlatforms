while (True):
    N, M = map(float, input().split())
    if N==0 and M==0: break
    print('%.6f' % ((M-N+1)/(M+1)))  if M >= N else  print('%.6f' % (float(0)))