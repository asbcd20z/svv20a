#python3 -Bi
#import myfilePkg
#s1:create a generator obj(not-running); s2:next(g)/g.send(None) for 1st time; s3:next(g)/g.send(myArg)
#that's,it's like a foo_send(context_,inputArg_), but a generator can remember the last context_ by itself
#https://www.jianshu.com/p/839a91dd49e4
def grep(pattern):
    i=0
    print("-Searching for", pattern,i)
    while True:
        print("-bef",i)
        line = (yield i)
        print("-aft:",line)
        i+=1

search = grep("cornator")
'''
next(search)
next(search)
next(search)
search.send("xx")
'''

def app(begi_):
  s="0";
  print("-enter for", begi_,s)
  s=begi_+s
  while True:
    print("-bef",s)
    t=(yield s)
    print("-aft.rcv",t,"-")
    s+=str(t)
x=app("begi")
x=app("begi")
y=x.send(None);print("y=",y,"\n")
y=x.send("a");print("y=",y,"\n")
y=x.send("a");print("y=",y,"\n")

