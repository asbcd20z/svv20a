#if 0
#set -x
gcc -m32 -g -gstabs+ $0 -o $0.ell || exit -1
ls -l $0*
./$0.ell
objdump $0.ell -G -g
exit 0;
#endif

//#include <stdio.h>
struct Test{
unsigned long KE: 18;
unsigned long KI: 18;
unsigned long KC: 18;
unsigned long KS: 18;
unsigned long KB: 24;
} test;

int
main(int argc, const char *argv[])
{
printf("sizeof(Test) = %d\n", sizeof(test));
return 0;
}

