import time

micro = lambda: int(round(time.time() * 10**6))

def displayPeriod(t):
  if (t<10**3):
    return (str(t)+"µs")
  if (t<10**6):
    return (str(t/10**3)+"ms")
  else:
    return (str(t/10**6)+"s")

