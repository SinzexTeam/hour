import urllib3
import time

while True:
 http = urllib3.PoolManager()
 txt = http.request('GET', "http://kpwresdpofi.ml/sinzex/asdwijopsija/sys.php?action=getusernames")
 txt = str(txt.data)
 txt = txt[2:]
 txt = txt[:-1]
 
 x = txt.replace("hours.php;", "").split(";")
 x = x[:-1]
 
 for i in x:
  print(f"http://kpwresdpofi.ml/sinzex/asdwijopsija/hour.php?username={i}")
 print("Я спать")
 local_time = 60 * 60
 time.sleep(local_time)