#if 0
#set -x
gcc -g -gstabs+ $0 -o $0.ell || exit -1
ls -l $0*
./$0.ell
objdump $0.ell -G -g
exit 0;
#//#Id$
#endif

//#include <stdio.h>
#if 0
----------------------------------------------struct/union-LenByte
-------------------------------------------type:TypeRef = sL(B)mem1{name:typeRef,start,len(b)};mem2{..};mem3;...;;
3      LSYM   0      0      00000000 45     int:t(0,1)=r(0,1);-2147483648;2147483647;
4      LSYM   0      0      00000000 87     char:t(0,2)=r(0,2);0;127;
20     LSYM   0      0      00000000 780    void:t(0,18)=(0,18)
21     LSYM   0      0      00000000 800    STa:T(0,19)=s8yc:(0,2),0,8;yi:(0,1),32,32;;
22     LSYM   0      0      00000000 844    STb:T(0,20)=s4yc:(0,2),0,8;ys:(0,8),16,16;;
23     LSYM   0      37     00000000 888    STb_:t(0,21)=(0,20)
24     LSYM   0      0      00000000 908    STc:T(0,22)=s12a:(0,19),0,64;b:(0,21),64,32;;
25     LSYM   0      0      00000000 954    SArr:T(0,23)=s36yc:(0,2),0,8;cc:(0,24)=ar(0,25)=r(0,25);0;037777777777;;0;1;(0,22),32,192;ccc:(0,26)=ar(0,25);0;4;(0,2),224,40;;
26     LSYM   0      0      00000000 1083   SBit:T(0,27)=s4x:(0,1),0,3;y:(0,1),3,2;;
27     LSYM   0      0      00000000 1124   SUa:T(0,28)=u4yc:(0,2),0,8;yi:(0,1),0,32;;
28     LSYM   0      0      00000000 1167   Ue:T(0,29)=u4yi:(0,1),0,32;;
29     LSYM   0      0      00000000 1196   STe:T(0,30)=s16cho:(0,2),0,8;u:(0,29),32,32;uu:(0,31)=u1yc:(0,2),0,8;;,64,8;:(0,32)=u2ys:(0,8),0,16;;,80,16;i:(0,1),96,32;;
30     LSYM   0      65     00000000 1320   bool:t(0,33)=(0,1)
31     LSYM   0      0      00000000 1339   EColor:T(0,34)=ered:-1,gre:0,blu:1,;
32     LSYM   0      0      00000000 1376   S_bool_enum:T(0,35)=s16ch:(0,2),0,8;c:(0,34),32,32;b:(0,33),64,32;i:(0,1),96,32;;
33     FUN    0      74     004011a0 1458   main:F(0,1)
34     PSYM   0      74     00000008 1470   ac:p(0,1)
35     PSYM   0      74     0000000c 1480   av:p(0,36)=*(0,37)=*(0,2)

struct STa { /* size 8 id 1 */
  char yc; /* bitsize 8, bitpos 0 */
  int yi; /* bitsize 32, bitpos 32 */
};

union SUa { /* size 4 id 6 */
  char yc; /* bitsize 8, bitpos 0 */
  int yi; /* bitsize 32, bitpos 0 */
};

typedef int bool;
enum EColor { red = -1, gre, blu };
struct S_bool_enum { /* size 16 id 11 */
  char ch; /* bitsize 8, bitpos 0 */
  enum EColor c; /* bitsize 32, bitpos 32 */
  bool b; /* bitsize 32, bitpos 64 */
  int i; /* bitsize 32, bitpos 96 */
};

#endif
//==
struct STa
{char yc;
int yi;
};
typedef struct STb
{char yc;
short ys;
}STb_;
struct STc
{struct STa a;
STb_ b;
};
struct SArr
{char yc;
struct STc cc[2];
char ccc[5];
};
//=
struct SBit
{int x:3;
int y:2;
};
union SUa
{char yc;
int yi;
};
//=
struct STe
{char cho;
union Ue{int yi;} u;
union {char yc;} uu;
union {short ys;};
int i;
};

typedef int bool; // c没有bool类型, c++中bool长度为4bytes,或1byte(最新g++4.x版本标准)
enum EColor{red=-1, gre, blu};
struct S_bool_enum{
char ch;
enum EColor c;
bool b;
int i;
};

int main(int ac, char* av[])
{
//int x=8;
//
//以前一直在写c++，所以想当然的认为c语言中也有bool类型，然而并没有，
//只是在C99标准引入的新的关键字_Bool 和c++中的bool类似，如果在c中也想直接使用bool，可以添加stdbool.h头文件
//bool b=false;
//sizeof(bool)==1;sizeof(EColor)==4; ///=1byte like char for this g++4.9. And enum is like "const int"
return 0;
}

