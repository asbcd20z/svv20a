//$ gcc -fPIC -shared func.c -o libfunc.so
/* func.c */
#include <stdio.h>
struct mycc{
char c1;
int i2;
short s3[20];//20,22
int i4;
};
int fcc(struct mycc c)
{
printf("--sizeof: %d--arg:%c,%d,%d,%x,%p\n", sizeof(c),c.c1,c.i2,c.s3[1],c.i4,&c);
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
