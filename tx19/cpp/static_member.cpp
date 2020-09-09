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

class B
{
public:
//protected:
static void foo1(){cout<<"B.foo1"<<endl;}
static void foo2(){cout<<"B.foo2"<<endl;}
static void  foo(){foo1();} // call B::foo1(), even by D::foo()
};

class D: public B
{
public:
//protected:
static void foo1(){cout<<"D.foo1"<<endl;}
//using B::foo;
};

int main()
{
D d;
//d.foo1(); //error: 'static void D::foo1()' is protected
//d.foo2();
//
cout<<__LINE__<<"class:"<<endl;
B::foo1();
D::foo1();
cout<<__LINE__<<"class-sub:"<<endl;
B::foo2();
D::foo2();
cout<<__LINE__<<"foo-foo1"<<endl;
D::foo();
return 0;
}
