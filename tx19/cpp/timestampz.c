#if 0
#//$Id$
#set -x
gcc -g $0 -o $0.ell ||exit 1
ls -l $0*
./$0.ell
#exit 0
echo
date --date='@1588848145.585363600'  +%FT%T.%NZ
date --date=2020-05-07T18:42:25.585363600Z  +%s.%N
date --date='@1588848145.585363600' +%FT%T.%NZ |xargs -ti date --date={} +%s.%Nzz
date --date=2020-05-07T18:42:25.585363600Z  +%s.%N |awk -e'{printf("%023.9f\n",$0+0.002)}'
date --date=2020-05-07T18:42:25.585363600Z -u
date --date=2020-05-07T18:42:25.585363600+0000
@echo
date --date=2020-05-07T18:42:25.585363600
date --date=2020-05-07T18:42:25.585363600 -u
date --date=2020-05-07T18:42:25.585363600+0000
date --date=2020-05-07T18:42:25.585363600+0000 -u
date --date=2020-05-07T18:42:25.585363600+0000 +%FT%T.%N%z
exit 0
#endif

//http://www.man7.org/linux/man-pages/man7/time.7.html
//Variadic functions https://en.cppreference.com/w/c/variadic
#include <stdio.h>
#include <sys/time.h> //gettimeofday
#include <time.h> //clock_gettime
#include <unistd.h>

extern unsigned getLine(){static unsigned l=-3u;return ++l;}
//#define LOG(...)
#define LOG(...) do{unsigned l=getLine(); struct timespec ts;int rval=clock_gettime(CLOCK_REALTIME,&ts); \
    if(!(l&0xFF)){unsigned pl=l;l=getLine(); struct tm tmX;gmtime_r(&ts.tv_sec,&tmX); char tbuf[32]={0};strftime(tbuf,32, "%FT%Tz", &tmX/*gmtime(&ts.tv_sec)*/);\
    /*printf("%04x: %d.%09d #UTC-timestamp %s.%09d\n", pl,ts.tv_sec,ts.tv_nsec, tbuf,ts.tv_nsec);}*/ \
    printf("%04X: %d.%09d %s+%d@%s: #UTC-timestamp %s\n", pl,ts.tv_sec,ts.tv_nsec, __FILE__,__LINE__,__func__, tbuf);} \
    printf("%04X: %d.%09d %s+%d@%s: \n", l,ts.tv_sec,ts.tv_nsec, __FILE__,__LINE__,__func__); fflush(stdout);\
        }while(0)

int main(int ac,char* av[])
{
struct timeval tv;
int rval=0;
rval=gettimeofday(&tv, NULL);
printf("%d, %d.%06d\n", __LINE__, tv.tv_sec,tv.tv_usec);
rval=gettimeofday(&tv, NULL);
printf("%d, %d.%06dZ\n", __LINE__, tv.tv_sec,tv.tv_usec);

//usleep(300);
struct timespec ts;
rval=clock_gettime(CLOCK_REALTIME,&ts);
printf("%d, %d.%09d\n", __LINE__, ts.tv_sec,ts.tv_nsec);
rval=clock_gettime(CLOCK_REALTIME,&ts);
printf("%d, %d.%09dz\n", __LINE__, ts.tv_sec,ts.tv_nsec);

printf("==\n");
//The call ctime(t) is equivalent to asctime(localtime(t))
//asctime(gmtime(t))
char tbuf[32]={0};
strftime(tbuf,32, "%FT%Tz", gmtime(&ts.tv_sec)); //UTC ie.timezone+0000
printf("%d, %010d.%9d UTC-timestamp %s.%09d\n", __LINE__, ts.tv_sec,ts.tv_nsec, tbuf,ts.tv_nsec);

#if 1
printf("==\n");
printf("%d, %04x\n", __LINE__, getLine());
printf("%d, %04x\n", __LINE__, getLine());
LOG();//sleep(1);
LOG();
printf("%d, %04x\n", __LINE__, getLine());
printf("%d, %04x\n", __LINE__, getLine());
#endif

return 0;
}

