

//socket sctp
//socket编程---SCTP
//https://www.cnblogs.com/tianzeng/p/9960077.html
/*************************************************************************
    > File Name: client.c
    > Author: Chen
    > Mail: 971859774@qq.com 
    > Created Time: 2018年11月14日 星期三 17时06分56秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <netinet/sctp.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include "my_err.h"

#define SERV_PORT 9877
#define SCTP_MAXLINE 800
#define SERV_MAX_SCTP_STRM 10

void sctp_cli(int sockfd,struct sockaddr * to,socklen_t tolen)
{
    struct sctp_sndrcvinfo sri;
    bzero(&sri,sizeof(sri));

    char rdbuf[MAXLINE],rvbuf[MAXLINE];
    struct sockaddr_in peeraddr;
    int flag;
    while(fgets(rdbuf,MAXLINE,stdin)!=NULL)
    {
        if(rdbuf[0]!='[')
        {
            fprintf(stderr,"Error,line must be of the form '[strnum]text'\n");
            continue;
        }

        if(isdigit(rdbuf[1]))
        {
            sri.sinfo_stream=strtol(&rdbuf[1],NULL,10);
            int out_sz=strlen(rdbuf);
            sctp_sendmsg(sockfd,rdbuf,out_sz,to,tolen,0,0,sri.sinfo_stream,0,0);
            socklen_t len=sizeof(peeraddr);
            int rd_sz=sctp_recvmsg(sockfd,rvbuf,sizeof(rvbuf),(struct sockaddr *)&peeraddr,&len,&sri,&flag);

            printf("From str:%d seq:%d (assoc:0x%x):",sri.sinfo_stream,sri.sinfo_ssn,(u_int)sri.sinfo_assoc_id);
            printf("%.*s",rd_sz,rvbuf);
        }
    }
    return;
}

//是否有头端阻塞
void sctp_cli_all(int sockfd,struct sockaddr *to,socklen_t tolen)
{
    struct sctp_sndrcvinfo sri;
    bzero(&sri,sizeof(sri));

    char rdbuf[MAXLINE],rvbuf[MAXLINE];
    bzero(&rdbuf,sizeof(rdbuf));
    bzero(&rvbuf,sizeof(rvbuf));

    while(fgets(rdbuf,SCTP_MAXLINE-9,stdin)!=NULL)
    {
        int rd_sz=strlen(rdbuf);
        if(rdbuf[rd_sz-1]=='\n')
        {
            rdbuf[rd_sz-1]='\0';
            --rd_sz;
        }

        int i=0;
        for(;i<SERV_MAX_SCTP_STRM;++i)
        {
            snprintf(rdbuf+rd_sz,sizeof(rdbuf)-rd_sz,".msg.%d",i);
            sctp_sendmsg(sockfd,rdbuf,sizeof(rdbuf),to,tolen,0,0,i,0,0);
        }

        struct sockaddr_in peeraddr;
        int flag;
        for(i=0;i<SERV_MAX_SCTP_STRM;++i)
        {
            socklen_t len=sizeof(peeraddr);
            rd_sz=sctp_recvmsg(sockfd,rvbuf,sizeof(rdbuf),(struct sockaddr *)&peeraddr,&len,&sri,&flag);

            printf("From str:%d seq:%d (assoc:0x%x):",sri.sinfo_stream,sri.sinfo_ssn,(u_int)sri.sinfo_assoc_id);
            printf("%.*s\n",rd_sz,rvbuf);
        }
    }
    return;
}

int main(int argc,char **argv)
{
    int flag=0;
    if(argc<2)
        err_quit("please input server ip");
    else if(argc>2)
        flag=1;
    //sock
    int sockfd=socket(AF_INET,SOCK_SEQPACKET,IPPROTO_SCTP);
    
    struct sockaddr_in servaddr;
    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(SERV_PORT);
    inet_pton(AF_INET,argv[1],&servaddr.sin_addr);

    struct sctp_event_subscribe events;
    bzero(&events,sizeof(events));
    events.sctp_data_io_event=1;
    setsockopt(sockfd,IPPROTO_SCTP,SCTP_EVENTS,&events,sizeof(events));

    if(flag==0)
        sctp_cli(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr));
    else
        sctp_cli_all(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr));

    /*
     * ABORT类似于tcp的rst分节，无延迟的终止任何关联，尚未发送的任何数据都
     * 丢弃，也没有TCP的TIME_WAIT的不良影响，
     */
    /*
    char beymsg[20];
    strcpy(beymsg,"goodbey");
    sctp_sendmsg(sockfd,beymsg,strlen(beymsg),(struct sockaddr *)&servaddr,sizeof(servaddr),0,MSG_ABORT,0,0,0);*/
    close(sockfd);
    return 0;
}

