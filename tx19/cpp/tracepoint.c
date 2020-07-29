#if 0
//tracepoint.command
file tracepoint
target remote 127.0.0.1:1234
trace tracepoint.c:15
actions
collect indx
end
tstart
break tracepoint.c:14
continue
continue 10
tstop
tstatus
tfind start
while($trace_frame != -1)
printf "Frame %d : indx = %d\n", $trace_frame, indx
tfind
end

#[redhat@localhost src]$ gdbserver --attach 127.0.0.1:1234 `pidof tracepoint`
#[redhat@localhost test]$ gdb --command=command
#endif
//gdb tracepoint 使用demo https://blog.csdn.net/Morphad/article/details/17310167

#include <stdio.h>
#include <unistd.h>

int indx;

int main(int argc, char *argv[])
{
    int res;

    indx = 0;
    while ( indx < 10000 ) {
        res = indx * 2;
        printf("%d\n", res);
        sleep(1);
        indx++;
    }

    return 0;
}
//gcc -g tracepoint.c -o tracepoint
