#if 0
g++ -g -gstabs+ $0 -o $0.ell ||exit -1;
ls -l $0*
objdump -Gg $0.ell
exit 0;
#endif

//#pragma pack(4)
//#pragma pack(1)
struct mys1{
char c1;
//long long l2;
double d2;
char c3;
};
#pragma pack()

int main(int ac, char* av[])
{
}


