#if 0
g++ -g -gstabs+ $0 -o $0.ell ||exit -1;
g++ -g -gstabs+ $0 -c
ls -l $0*
objdump -Gg $0.ell  # >& $0.ell.cpu64
exit 0;
#endif

//try for cpu64
struct mydef64{
char c1;
//int* pi; //8bytes for pointer
int i2;
char c3;
long l4;   //8bytes for cpu64
long long ll5; //8bytes
double d6;
};

struct myp64{
char c1;
int* pi; //8bytes for pointer
long l3;
};

#pragma pack(1)
struct mys1{
char c1;
double d2;
char c3;
};
#pragma pack()

int main(int ac, char* av[])
{
}


