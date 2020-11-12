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
using namespace std;

#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
 
int main()
{
    int n1 = 3;
    int n2 = 5;
 
    std::vector<int> v{0, 1, 2, 3, 4};
 
    auto result1 = std::find(std::begin(v), std::end(v), n1);
    auto result2 = std::find(std::begin(v), std::end(v), n2);
 
    if (result1 != std::end(v)) {
        *result1 =33;
        auto p=&(*result1);
        *p=44;
        std::cout<<*result1 << "v contains: " << n1 << '\n';
    } else {
        std::cout << "v does not contain: " << n1 << '\n';
    }
 
    if (result2 != std::end(v)) {
        std::cout << "v contains: " << n2 << '\n';
    } else {
        std::cout << "v does not contain: " << n2 << '\n';
    }
}

int main0()
{

return 0;
}
