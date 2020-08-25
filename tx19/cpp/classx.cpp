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
using namespace std;

void foodef(int x=0){cout<<"define-with-def:"<<x<<endl;}

struct Xstring
{
//Xstring(){}
Xstring(const char* s=NULL){}
Xstring(const Xstring& rts_){}
Xstring& operator=(const Xstring& rts_){return(*this);}
char* _str=nullptr;
};

//ostream& operator<<(ostream& os, char* p_){if(!p_){os<<"NUL";}else{os<<p_;} return os;} //error recursion if not NULL

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
	return 0;
}

