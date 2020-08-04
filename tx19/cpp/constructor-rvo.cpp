#if 0
#set -x
g++ -g   -std=c++11 $0 -o $0.ell ||exit -1
./$0.ell
g++ -g -Wall  -std=c++11 -fno-elide-constructors $0 -o $0.ell ||exit -1
ls -l $0*
./$0.ell
exit 0;
##
https://www.geek-share.com/detail/2725637758.html
https://blog.csdn.net/zhangqi_gsts/article/details/89076465
https://segmentfault.com/a/1190000018096043
https://segmentfault.com/a/1190000022062016?utm_source=sf-related
https://www.geek-share.com/detail/2539234761.html
https://blog.csdn.net/luotuo44/article/details/46779063 //&& 移动构造
https://www.cnblogs.com/xiongjiaji/p/3351383.html // C++标准规定，delete (void*)0;是安全的. delete NULL
//-malign-double
#endif

#include <iostream>
#include <string>
using namespace std;

class A{
public:
//A() = default;
A(): str("none"){ cout<< "cons-def" <<endl; }
A(const string &d): str(d){ cout << "cons-str" << endl; }
A(const A &a): str(a.str){ cout << "cons-copy" << endl; }
A& operator=(const A& a){ if (this!=&a){str=a.str;} cout << "assig=" <<endl; return(*this);}
~A(){cout << "~des" << endl;}
void foo() const;
string str;
};
void A::foo() const{}

void func(A a)
{
cout << a.str << endl;
}
int main0()
{
func(string("hello world"));
return 0;
}

//===
A f()  
{  
return A();  
}  
int main1(void)  
{  
A o = f();
//A o2("ha");
//o2=o;
return 0;
}  

int main2()
{
A o("hi");
A o2;
o2=o;
return 0;
}

int main()
{
	main0();
	cout<<"------\n";
	main1();
	cout<<"------\n";
	main2();
	return 0;
}

