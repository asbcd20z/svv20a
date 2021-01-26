#if 0
gcc -gstabs+ -fPIC -shared func.c -o libfunc.so ||exit -1;
#nm libfunc.so -D
#gcc -fPIC  $0 -o $0.ell0 ||exit -1
 gcc -fPIC  $0 -o $0.ell -rdynamic ||exit -1
#gcc -fPIC  $0 -o libfunc.so  -rdynamic ||exit -1  #cygfault, and linux fails with 'cannot dynamically load executable'
#ls
nm *func* -A|grep main
#nm -D //objdump  -T libfunc.so |grep text
#objdump -Gg
exit 0;
#endif

//$ gcc -fPIC -shared func.c -o libfunc.so
/* func.c */
#include <stdio.h>
struct mycc{
char c1;
int i2;
short s3[20];//20,22
int i4;
};
//
int fcc(struct mycc c)
{
printf("--fcc, sizeof: %d--arg:%c,%d,%d,%X,%p\n", sizeof(c),c.c1,c.i2,c.s3[1],c.i4,&c);
return c.i2*c.i2;
}
//=
int func(int a)
{
        return a*a;
}


//==how to return struct for ctypes in python?
struct mycc func2(int a)
{
	struct mycc c={};
	c.i2=a+1;
	c.i4=a;
	return c;
}


__attribute__((weak)) 
int mainw(int x_){printf("mainw\n");}
//int mainw2(int x) __attribute__((weakref("mainw")))

//__attribute__((weak))  //linux ok, but cywin fails when ld
int main(int ac, char* av[]){printf("hi..\n"); mainw(1);}
