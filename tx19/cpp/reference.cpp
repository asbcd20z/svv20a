#if 0
#g++ -fno-elide-constructors -g -c $0 ||exit -1
g++  -std=c++1y -g -c $0 ||exit -1
#g++ -S $0 ||exit -1
ls -l  ${0%.cpp}*
#ls -l $0* ${0%.c}*
#cat ${0%.c}.s
objdump -S ${0%.cpp}.o
exit 0
#gdb reference.o -q -ex 'disassemble/m main0' -ex q
#endif

#include <utility>

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
//int val(const int a_){return 0;} ///not ok,it's same to below
int val(/*const */ int a_) ///ret by 寄存器eax
{
	a_=8;
int x=7;
x=a_+1;
a_=8;
return a_;
}
//引用作 arg或return 都是作为address
const int& ref(const int& a_){return a_;} ///ok,is mangled diferrent to below
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


//rval
void rval()
{
int x=7;
int* px=&x;
int& rx=x;
rx=6;
//
int&& rval=8; ///value 8 is stored-hide in frame-stack, then rval point to it
rval=9;
return;
}

//about argument by value, reference, right-reference
void foo1(/*const */ int a_) ///__Z4foo1i
{
int x=9;
x=a_;
}
void foo1_ref(const int& a_) ///__Z8foo1_refRKi， 可可用于const,或left/right
{
int x=0;
x=a_;
}
void foo1_ref( int& a_) ///__Z8foo1_refRi， only for left
{
int x=0;
x=a_;
}
void foo1_ref( int&& a_) ///__Z8foo1_refOi, only for right/const-temp
{
int x=0;
x=a_;
}
void call_foo1()
{
//foo1(1);
foo1_ref(1);
int x=8;
//int&&z=std::move(x);foo1_ref(z);
foo1_ref(std::move(x));
foo1_ref(x);
const int y=9; foo1_ref(y);
}
