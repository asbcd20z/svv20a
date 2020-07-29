#if 0
#g++ -fno-elide-constructors -Werror -Wall  -g -std=c++11 $0 -o $0.ell ||exit -1;
g++ -Wall  -g -std=c++11 $0 -o $0.ell ||exit -1;
ls -l $0*
./$0.ell
exit 0;
#endif
#include <iostream>
#include <vector>

using namespace std;

vector<int> foo1()
{
vector<int> v(3,7);
int *p=&v[2];
cout<<__LINE__<<": "<< sizeof(v)<<p<<endl;
cout<<__LINE__<<": "<< v.size()<<","<<v[0]<<v[1]<<v[2] <<endl;
return v;//std::move(v);
}
void foo1m()
{
vector<int> v;
v=foo1();
int *p=&v[2];
cout<<__LINE__<<": "<< sizeof(v)<<p<<endl;
cout<<__LINE__<<": "<< v.size()<<","<<v[0]<<v[1]<<v[2] <<endl;
//
vector<int> v2;v2=v;int *p2=&v2[2];cout<<__LINE__<<": "<< sizeof(v2)<<p2<<endl; 
vector<int> v3;v3=std::move(v);int *p3=&v3[2];cout<<__LINE__<<": "<< sizeof(v3)<<p3<<"/"<<*p3<<endl; //
auto *q=&v;cout<<q<<endl;
}

//==
vector<vector<char>> foo(){
vector<char> t(4,'A');
vector<vector<char>> v(3,vector<char>(4,'A')); //r3c4
cout<<__LINE__<<": "<< sizeof(v)<<endl;
cout<<__LINE__<<": "<< v.size()<<","<<v[0].size()<<endl;
cout<<"/"<<v[0][0]<<v[0][1]<<v[0][3]<<endl;
return std::move(v);//v;
}

void foom()
{
vector<vector<char>> v;//v(3,{4,8}); //r3c4
v=foo();
cout<<__LINE__<<": "<< v.size()<<","<<v[0].size()<<endl;
cout<<"/"<<v[0][0]<<v[0][1]<<v[0][3]<<endl;
}


int main(int ac, char* av[])
{
//vector<vector<char>> v;
//v=foo();
foo1m();
cout<<"=="<<endl;
foom();
cout<<__LINE__<<": "<< "end."<<endl;

return 0;
}
