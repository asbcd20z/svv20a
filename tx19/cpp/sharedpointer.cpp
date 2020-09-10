#if 0
#set -x
g++ -g   -std=c++11 $0 -o $0.ell ||exit -1
#./$0.ell
#g++ -g -Wall  -std=c++11 -fno-elide-constructors  $0 -o $0.ell ||exit -1
ls -l $0*
./$0.ell
exit 0;
##

#endif

#include <iostream>
#include <string>
#include <stdio.h>
#include <memory>
using namespace std;

struct B{
B(){cout<<__LINE__<<":" <<"B():"<<endl;}
~B(){cout<<__LINE__<<":" <<"~B():"<<endl;}
friend ostream& operator<<(ostream& os, B&){return os<<"hi";}
};

int main0()
{
cout<<__LINE__<<":" <<"start:"<<endl;
shared_ptr<B> po=make_shared<B>();
shared_ptr<B> po2(po);
cout<<__LINE__<<":" <<po.use_count() <<*po <<po.get()<<sizeof(po)<<endl;
po2.reset();
cout<<__LINE__<<":" <<po.use_count() <<*po <<po.get()<<endl;
po.reset();

return 0;
}

void del(B* b) {cout<<__LINE__<<": del-" <<b <<endl;/*del b;*/} //shared_ptr<B> po(b, del);

int main1()
{
cout<<__LINE__<<":" <<"start:"<<endl;
B* b=new B();
//shared_ptr<B> po=make_shared<B>();
//shared_ptr<B> po(b, [](B* b){cout<<__LINE__<<": lambda-del" <<b <<endl;} );
shared_ptr<B> po(b, del);
shared_ptr<B> po2(po);
cout<<__LINE__<<":" <<po.use_count() <<*po <<po.get() <<","<<sizeof(po)<<endl;
po.reset();
cout<<__LINE__<<":" <<po2.use_count() <<*po2 <<po2.get()<<endl;
//po2.reset();

return 0;
}


int main()
{
//main0();
main1();
return 0;
}
