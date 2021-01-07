#if 0
#set -x
g++ -g   -std=c++11 $0 -o $0.ell ||exit -1
#./$0.ell
#g++ -g -Wall  -std=c++11 -fno-elide-constructors  $0 -o $0.ell ||exit -1
ls -l $0*
./$0.ell
exit 0;
##
$ find /usr -name string
/usr/lib/gcc/i686-pc-cygwin/4.9.3/include/c++/debug/string
/usr/lib/gcc/i686-pc-cygwin/4.9.3/include/c++/string
#include <bits/basic_string.h>
#include <bits/basic_string.tcc>
字符指针指向NULL，cout输出时出现的非法操作的困惑 https://bbs.csdn.net/topics/60196783
#
c++String实现## https://blog.csdn.net/qq_40386321/article/details/101298064
C++ string类详解 https://blog.csdn.net/huangjw_806/article/details/79700964
strings(字符串)详解(一) https://blog.csdn.net/axe8/article/details/50363
#endif

#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;


struct CA{
static int _x;  /// declare for static member
//int _x; //error: 'int CA::_x' conflicts with a previous declaration
int _y;
};

struct CB: CA{
int _y;  //CA::_y is hided?
int _z;
};


int CA::_x=99; /// define for static member, but must not with 'static' here

int main()
{
CA a;
a._x=1;
a._y=2;

cout<<a._x<<a._y<<endl;
return 0;
}

