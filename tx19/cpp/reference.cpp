#if 0
#g++ -fno-elide-constructors -g -c $0 ||exit -1
g++ -g -c $0 ||exit -1
g++ -S $0 ||exit -1
ls -l  ${0%.cpp}*
#ls -l $0* ${0%.c}*
#cat ${0%.c}.s
objdump -S ${0%.cpp}.o
exit 0
#gdb reference.o -q -ex 'disassemble/m main0' -ex q
#endif

int gx=1;
int main0(int ac,char* av[])
{
return 0;
}

void foo1(int a_, int b_){
b_=0xc;	
a_=8;
int x=-4;
int y=-8;
}

void foo2r(){
int x=0;
int y=7; y=x;
int *px=0; px=&x;
*px=1;
y=*px;
//int& r;
int& rx=x;
rx=2;
y=rx;
const int& crx=x;
(void)crx;
y=crx;
}

#if 0
void foo2loop(){
int x=0;
//for(int i=0; i<3; i++);
for(int i=0; i<3; i++)
{int& rx=gx; rx=i;
}
}
#endif

int val(int a_) ///ret by 寄存器eax
{
	a_=8;
int x=7;
x=a_+1;
a_=8;
return a_;
}
//引用作 arg或return 都是作为address
int& ref(int& a_) ///引用传递的是address，类似指针。实参编译时隐式取自己的地址
{
	a_=8;
int x=7;
x=a_+1;
return a_;
}
int* ptr(int* a_)
{
	*a_=8;
return a_;
}
void foo_call()
{
gx=7;
int x=0;
x=val(gx);
x=ref(gx);       ///引用传递的是address，类似指针。实参编译时隐式取自己的地址
x=*ptr(&gx);
}


///===通常return：小数据通过寄存器(eax,edx), 太大的数据隐含作为arg0
struct Data{char x[9];};
Data gd;
Data foo_data(int a_, int b_) ///ret作为arg0,即: bp-ip--[ret-tmp]--a_--b_--->high
{a_=6; b_=7;
Data d={};
int x=1;
return d;
}
void foo_data_call()
{
Data d={};
d=foo_data(8,9);  ///参数隐含的为: (&ret-tmp_Data, 8, 9)
}

