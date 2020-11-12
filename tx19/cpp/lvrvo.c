#if 0
gcc -g -c $0 ||exit -1
gcc -S $0 ||exit -1
ls -l  ${0%.c}*
#ls -l $0* ${0%.c}*
#cat ${0%.c}.s
objdump -S ${0%.c}.o
exit 0
//gdb a.out #disassable foo
#endif

void foo()
{
char buf[6]="1234";
char c='a';
char* p=buf;
c=*buf;
*buf='A';
return;
}


#if 0
https://www.cnblogs.com/xkfz007/archive/2004/01/13/2336311.html
gcc中常用的选项
开始学习在Linux下写程序，利用gcc进行编译的时候经常需要添加一些选项，为了便于查找，将这写常用的选项整理出来。
GCC常用选项
    -c 通知GCC取消链接步骤，即编译源码并在最后生成目标文件；
    -Dmacro 定义指定的宏，使它能够通过源码中的#ifdef进行检验；
    -E 不经过编译预处理程序的输出而输送至标准输出；
    -g3 获得有关调试程序的详细信息，它不能与-o选项联合使用；
    -Idirectory 在包含文件搜索路径的起点处添加指定目录；
    -llibrary 提示链接程序在创建最终可执行文件时包含指定的库；
    -O、-O2、-O3 将优化状态打开，该选项不能与-g选项联合使用；
    -S 要求编译程序生成来自源代码的汇编程序输出；
    -v 启动所有警报；
    -Wall 在发生警报时取消编译操作，即将警报看作是错误；
    -Werror 在发生警报时取消编译操作，即把报警当作是错误；
    -w 禁止所有的报警。
加速：
    使用管道代替编译中临时文件，
    -pipe 加速编译
    gcc -pipe foo.c -o foo
#endif
