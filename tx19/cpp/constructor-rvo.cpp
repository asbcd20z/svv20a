#if 0
#set -x
g++ -g   -std=c++11 $0 -o $0.ell ||exit -1
./$0.ell
g++ -g -Wall  -std=c++11 -fno-elide-constructors  $0 -o $0.ell ||exit -1
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
https://blog.csdn.net/guangcheng0312q/article/details/103740410/  //现代C++之如何返回一个对象 //rvo/nrvo
https://blog.csdn.net/choumin/article/details/106986913 // 如f()的优化时,对象的创建的地址在f()外,优化s掉了return的对象. 即,Return-Value-Optimization能把对象直接构造到调用者的栈上
https://www.runoob.com/w3cnote/cpp-constructor-method-of-the-parent-class.html //在 C++ 中子类继承和调用父类的构造函数方法
https://www.cnblogs.com/huhuuu/p/3460406.html //继承中赋值函数的注意点 Base::operator =(other);
eg,C++中的对象初始化 https://www.cnblogs.com/arxive/p/8418187.html
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
A& operator=(const A& a){ if (this!=&a){str=a.str;} cout << "assig=copy" <<endl; return(*this);}
~A(){cout << "~des" << endl;}
A(A&& a): str(std::move(a.str)){ cout << "cons-move&&" << endl; }
A& operator=(A&& a){ if (this!=&a){str=std::move(a.str);} cout << "assig=move&&" <<endl; return(*this);}
void foo() const;
string str;
};
void A::foo() const{}

//===
void func(A a)
{
cout << a.str << endl;
}
int main0()
{
func(string("hello world"));
return 0;
}
//==
void main0a(){A a=string("to-construct");} //2 const[1.temp(string(...)),2.a(temp)].but will be optimizated as main0b() below
void main0b(){A a{string("to-construct")};}

//===
A f()
{
return A();
}
int main1(void)  
{
A o = f();
//A o2("ha"); o2=f();
///o2=o;
return 0;
}

//===
int main2()
{
A o("hi");
A o2(o);
A o2a(std::move(o));
A o3;
o3=o;
o3=std::move(o);
return 0;
}

int main()
{
	int x=0x1234567890;
	int y1=0x12345678; int y2=0x10; int y=y1*y2;
	cout<<x<<","<<y<<endl;
	main0a();
	cout<<"---\n";
	main0b();
	cout<<"---\n";
	main0();
	cout<<"------\n";
	main1();
	cout<<"------\n";
	main2();
	return 0;
}

