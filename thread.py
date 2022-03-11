
import threading
import time
# def g():
#     print("thread is working ! ")

# t = threading.Thread(target=g)
# t.start()



# def f(i) :
#     print("the i is :" , i )


# for i in range(3):
#     threading.Thread(target=f , args=(i,)).start()


# def h(i , name = 'default'):
#     print('thread named {} with id {} is working'.format(name,i))


# for i in range(0,3):
#     threading.Thread(target=h ,args=(i,) , kwargs={'name': '{}{}{}'.format(i,i,i)}).start()


# How to find out which thread is working right now ? :

# def t():
#     print('current thread is: ' + threading.current_thread().name)

# print(threading.currentThread().getName())
# threading.Thread(name ='noTime'  , target=t)
# threading.Thread(name ='Hossein' , target=t).start()
# threading.Thread(name ='kkowsar' , target=t).start()
# threading.Thread(target=t).start()


# How to make deamon thread : 

#non- daemon : 

# def func():
#    # print('(' +threading.current_thread().name +') started ! ' )
#     time.sleep(1)
#     #print('(' +threading.current_thread().name +') finished ! ' )


# t = threading.Thread(name ='non-deamon' , target=func)
# t.start()


# daemon :

# def func2():
#     print('(' +threading.current_thread().name +') started ! ' )
#     time.sleep(1)
#     print('(' +threading.current_thread().name +') finished ! ' )


# t = threading.Thread(name = 'non-daemon', target=func2)

# t.setDaemon(True)

# t.start()

# # time.sleep(2)

# print("this is main thread")

# join() in threading : 


# def f():
#     print('(' +threading.current_thread().name + ') started !')
#     time.sleep(2)
#     print('(' +threading.current_thread().name + ') finished !')


# t = threading.Thread(name ='firstOne',target=f)
# t.start()
# t.join()
# print('salam')
# print(t.is_alive())
# print("______________________")

# t = threading.Thread(name ='secondOne', target=f)
# t.start()
# t.join(1.0)
# print('khoobi?')
# print(t.is_alive())
# print("---------------------")


# t = threading.Thread(name ='thirdOne',target=f)
# t.start()
# print('che khabar?')
# print(t.is_alive())
# print("---------------------")



# enumerate : 

def f(i) :
    print('(' +threading.current_thread().name + ') started')
    time.sleep(i)
    print('(' +threading.current_thread().name + ') finished')


ls = []
for i in range (1,5):
        ls.append(threading.Thread(name='t'+str(i), target=f, args=(i,)))

for t in ls : 
    t.start()

time.sleep(3)
print('')
for t in threading.enumerate():
    print(t.name + "is alive now ")
