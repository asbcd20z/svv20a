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
