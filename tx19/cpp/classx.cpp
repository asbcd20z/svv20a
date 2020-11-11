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

void foodef(int x=0){cout<<"define-with-def:"<<x<<endl;}

//static char emptyStr[]; //static char emptyStr[];  ///error: storage size of 'emptyStr' isn't known
struct Xstring
{
static const int id=22;
static const int idx; //static const int Xstring::idx=22; //error: 'static' may not be used when defining (as opposed to declaring) a static data member [-fpermissive]
int id2=22;
 const int id3=22;
//static  int id4=22; //error: ISO C++ forbids in-class initialization of non-const static member 'Xstring::id4'

//Xstring(){}
Xstring(const char* s=NULL){}
Xstring(const Xstring& rts_){}
Xstring& operator=(const Xstring& rts_){return(*this);}
char* _str=nullptr;
//
friend ostream& operator<<(ostream& os, Xstring x){os<<x._str; return os;}
};

//ostream& operator<<(ostream& os, char* p_){if(!p_){os<<"NUL";}else{os<<p_;} return os;} //error recursion if not NULL


struct CInit
{
CInit():x{2}{}  //it's higher than inline-initializer(x=1)
int x=1;
friend ostream& operator<<(ostream& os, const CInit ob){return os<<ob.x<<std::endl;}
};


struct B{
int mb;
void f1(){}
virtual void vf1(){}
virtual void vf2(){}
};
struct D1: public B{
int md;
void f2(){}
virtual void vf2(){}
virtual void vf3(){}
};


int main()
{
	void foodef(int x=999);
	foodef();
	Xstring();
	cout<<"hi...\n";
	char* p=Xstring()._str; cout<<(!p?"NUL":p);
	//cout<<Xstring()._str<<endl;
	//const char* q="hello"; //cout <<q<<endl;
	cout<<(int*)0<<string("tt")<<"end.\n";
	string t;
printf("=%p\n", t.c_str());
CInit i; cout<<i;
B b;
D1 d;
	return 0;
}

