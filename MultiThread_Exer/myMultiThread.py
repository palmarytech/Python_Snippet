import queue, time, threading, datetime  
  
class Job:    
     def __init__(self, name):    
             self.name = name    
     def do(self):    
             time.sleep(2)    
             print("\t[Info] Job({0}) is done!".format(self.name))  
  
que = queue.Queue()  
for i in range(20):  
        que.put(Job(str(i+1)))  
  
print("\t[Info] Queue size={0}...".format(que.qsize()))  
  
def doJob(*args):  
     queue = args[0]  
     while queue.qsize() > 0:  
          job = queue.get()  
          job.do()  
  
# Open three threads  
thd1 = threading.Thread(target=doJob, name='Thd1', args=(que,))  
thd2 = threading.Thread(target=doJob, name='Thd2', args=(que,))  
thd3 = threading.Thread(target=doJob, name='Thd3', args=(que,))  
  
# Start activity to digest queue.  
st = datetime.datetime.now()  
thd1.start()  
thd2.start()  
thd3.start()  
  
# Wait for all threads to terminate.  
while thd1.is_alive() or thd2.is_alive() or thd3.is_alive():  
     time.sleep(1)    
  
td = datetime.datetime.now() - st  
print("\t[Info] Spending time={0}!".format(td))

#===================================================================================

# 子執行緒類別
class MyThread(threading.Thread):
  def __init__(self, num):
    threading.Thread.__init__(self)
    self.num = num

  def run(self):
    while True:
        print("My Thread {0} Class is Running".format(self.num))
        time.sleep(1)

# 建立 5 個子執行緒
threads = []
for i in range(5):
  threads.append(MyThread(i))
  threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(5):
  threads[i].join()

print("Done.")