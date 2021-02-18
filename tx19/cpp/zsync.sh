#
#sh -x ../zsync
##lz,v20210218a-git
#function: sync checkout-source-code from one trunk on local windows-pc to another trunk on linux(but shared by samba)
#attention: 1.trunk with same release version; 2.the file should be newer on local windows-pc if it needs updated by this script
#precondition: 'pwd(./)' is the checkout-trunk on local windows-pc(by tortoiseSVN), and $rpath is checkout-trunk with same release version on linux(linsee,so it can be compiled on linux),and $rpath is shared mapping by samba(linux's smbd service). so we can cp files from 'pwd' to $rpath easilly
#work-steps: 1.edit files on trunk of local windows-pc with source-insight quickly. 2.sync svn-diff files(only newer) to $rpath trunk. 3.then compile on linux
#attention: if files in local 'pwd' is reverted, do it on remote manual. (svn diff can find the files without changes)
rpath="z:/tw/trunk/"
#f=Makefile.local

fcp()
{
v=$1
echo -e "\n====  $v"
#rpath=lzhao019@hzling525.china.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; rsync -a $v $rpath/$v
#rpath=lzhao019@hzling525.china.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; scp -p $v $rpath/$v
rpath=cplanesh09.eecloud.dynamic.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/;  rsync -a $v $rpath/$v
#if [ "$v" -nt "$rpath/$v" ] ;then bash -x -c "  cp  $v $rpath/$v"; fi
#ls -l $v $rpath/$v
}
#fcp Makefile.local; exit 0;

#C_Test/cplane_k3/src/TestTargets/RROM/testcases/LBT5458_DynamicShaperControl.ttcn3
catzz()
{
cat<<eot
C_Application/SC_RROM/CP_LomManagement/Source/RromLomMgmtSessionFsm.cpp-
C_Application/SC_Common/Scripts/gencode/gencode_settings.py-
C_Application/SC_RROM/MsgBuilders/Source/RromBuildEnbsonCbrsConfigReq.cpp
C_Application/SC_RROM/MsgBuilders/Test_modules/RromBuildEnbsonCbrsConfigReqTestSuite.cpp
C_Application/SC_RROM/CP_LomManagement/CP_TraceConnections/Test_modules/Mocks/RromLomMgmtTraceConnectionsConnectionFSMMock.hpp
C_Application/SC_RROM/CP_LomManagement/CP_TraceConnections/Test_modules/RromLomMgmtTraceConnectionsConnectionsHolderTest.cpp-
C_Test/cplane_k3/src/TestTargets/RROM/templates/LTE1997_ENBSon_tmpl.ttcn3
C_Test/cplane_k3/src/TestTargets/RROM/templates/npf/CDNL_BTS_XCells.ttcn3
C_Test/cplane_k3/src/TestTargets/RROM/templates/NpfConfigValues.ttcn3
C_Test/cplane_k3/src/TestTargets/RROM/testcases/LTE4738_GSMLTEDynamicSpectrumSharing.ttcn3-

eot
}

main()
{
#C_Application/SC_UEC/CP_Utilities/CP_RrcMsgBuilder/Test_modules/UecOtherConfigR9ExtensionAdditionFillerTestSuite.cpp
for f in `svn diff|grep 'Index:'|cut -d' ' -f2`  `catzz`;  #it's better to save the differrence filename into a file,then can edit the file.such as add '#' to remove filename from the list in the file
#for f in `cat ../zz`;
do
  fcp $f
 #sleep 1
done
}

main2()
{
echo >ylist.txt
#svn diff|grep 'Index:'|cut -d' ' -f2 >ylist.txt
catzz >>ylist.txt
sed -i -e'/cplaneLogger/s|$|-|'  ylist.txt
bash -xc 'cat ylist.txt'
echo

#rpath=cplanesh09.eecloud.dynamic.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; 
rpath=cplanesh02.eecloud.dynamic.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; 
#echo rsync -a --include-from= $v $rpath/$v
#echo rsync -nrvCtaz --stats `cat ylist.txt` $rpath/$v
 rsync -rvCtaz --stats --files-from=ylist.txt . $rpath/
}

#alias svn='/cygdrive/c/Program\\x20Files/TortoiseSVN/bin/svn'
#svn h



catzz3()
{
cat<<eot |egrep -v '\-$'
cplane/CP-RT/CP-RT/SCT/Ttcn3/messages/F1APControlMessages.ttcn3--

eot
}

main3()
{
local x=`dirname $0`; local y=$x/ylist.txt
echo >$y
#svn diff|grep 'Index:'|cut -d' ' -f2 >$y
git diff --name-only HEAD >$y
#git diff --name-only origin/master >$y
#
catzz3 >>$y
sed -i -e'/cplaneLogger/s|$|-|'  $y
sed -i -e'/CPRT_Design_Document_20B.adoc/s|$|-|'  $y
#bash -xc "cat $y"
bash -xc "nl $y"
echo

#rpath=cplanesh09.eecloud.dynamic.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; 
#rpath=cplanesh02.eecloud.dynamic.nsn-net.net:/var/fpwork/lzhao019/tw/trunk/; 
#rpath=hzlinb47.china.nsn-net.net:/var/fpwork/lzhao019/t/nr/gnb/
#rpath=10.183.68.25:/var/fpwork/lzhao019/nr4/gnb/
rpath=10.183.68.25:/var/fpwork/lzhao019/t/nr/gnb/
rpath=10.183.68.25:/ephemeral/workspace/lzhao019/nr5/gnb/
rpath=10.183.67.66:/ephemeral/workspace/lzhao019/nr6/gnb
#rpath=10.182.67.77:/ephemeral/workspace/lzhao019/nr7/gnb
#rpath=10.182.68.88:/ephemeral/workspace/lzhao019/nr7/gnb

#pwd
echo ==$PWD ==$rpath
#echo rsync -a --include-from= $v $rpath/$v
##echo rsync -nrvCtaz --stats `cat ylist.txt` $rpath/$v
echo
  rsync -rvCtaz --stats --files-from=$y . $rpath/
}


main3
echo
exit 0;

#scp /c/temp/20190412.diff 10.183.68.25:tmp/

##https://www.cnblogs.com/konrad/p/6901273.html
##for-cygwin:install rsync+ssh; ssh-setup-rlogin-without-pw[1.ssh-keygen(create id_rsa+id_rsa.pub), 2.ssh-copy-id remote-ip(local"known_hosts" yes simultaneously)(or:cat id_rsa.pub, then ssh remote-ip, and append id_rsa.pub text to remote"authorized_keys" manually.)]
#
