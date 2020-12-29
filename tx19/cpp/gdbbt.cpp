#if 0
#set -x
g++ -g -gstabs+   -std=c++11 $0 -o $0.ell ||exit -1
#./$0.ell
#g++ -g -Wall  -std=c++11 -fno-elide-constructors  $0 -o $0.ell ||exit -1
ls -l $0*
./$0.ell
#exit 0;

gdb -q gdbbt.cpp.ell  <<eot
b mybk
r
bt full
eot
exit 0;

##

#endif
#include <stdio.h>
#include <iostream>

struct Data{
	char c;
	int i;
};

void mybk(int x_=0){}
void foo(Data d_)
{
	Data d2=d_;
	Data& d3=d_;
	std::cout<<d_.i<<std::endl;
	mybk(1);
}

void foor(Data& d_)
{
	Data d2=d_;
	Data& d3=d_;
	std::cout<<d_.i<<std::endl;
	mybk(2);
}


enum AA{aa1=-1,aa2}; enum AA aa=aa1;
int main(int ac, char* av[])
{
	Data d;
	foo(d);
	foor(d);
	//
	bool b=false; // c没有bool类型, c++中bool长度为4bytes,或1byte(最新g++4.x版本标准)
	sizeof(bool)==1;sizeof(AA)==4; ///=1byte like char for this g++4.9. And enum is like "const int"
	return 0;
}
