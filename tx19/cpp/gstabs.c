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
21     LSYM   0      0      00000000 775    STa:T(0,19)=s8yc:(0,2),0,8;yi:(0,1),32,32;;
22     LSYM   0      0      00000000 819    STb:T(0,20)=s4yc:(0,2),0,8;ys:(0,8),16,16;;
23     LSYM   0      26     00000000 863    STb_:t(0,21)=(0,20)
24     LSYM   0      0      00000000 883    STc:T(0,22)=s12a:(0,19),0,64;b:(0,21),64,32;;
25     LSYM   0      0      00000000 929    SArr:T(0,23)=s36yc:(0,2),0,8;cc:(0,24)=ar(0,25)=r(0,25);0;037777777777;;0;1;(0,22),32,192;ccc:(0,26)=ar(0,25);0;4;(0,2),224,40;;
26     LSYM   0      0      00000000 1058   SBit:T(0,27)=s4x:(0,1),0,3;y:(0,1),3,2;;
27     LSYM   0      0      00000000 1099   SUa:T(0,28)=u4yc:(0,2),0,8;yi:(0,1),0,32;;
28     LSYM   0      0      00000000 1142   Ue:T(0,29)=u4yi:(0,1),0,32;;
struct STa { /* size 8 id 1 */
  char yc; /* bitsize 8, bitpos 0 */
  int yi; /* bitsize 32, bitpos 32 */
};
#endif
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

int main(int ac, char* av[])
{
//int x=8;
return 0;
}

