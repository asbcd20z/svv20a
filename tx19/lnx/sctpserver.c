

/*************************************************************************
    > File Name: client.c
    > Author: Chen
    > Mail: 971859774@qq.com 
    > Created Time: 2018年11月14日 星期三 14时56分38秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <string.h>
#include <strings.h>
#include <netinet/sctp.h>
#include "my_err.h"

#define SERV_PORT 9877
#define LISTENQ 1024

sctp_assoc_t sctp_get_no_strms(int sock_fd,struct sockaddr *to,socklen_t tolen,struct sctp_sndrcvinfo sri)
{
    int retsz;
    struct sctp_status status;
    retsz=sizeof(status);
    bzero(&status,sizeof(status));

    status.sstat_assoc_id=sri.sinfo_assoc_id;
    getsockopt(sock_fd,IPPROTO_SCTP,SCTP_STATUS,&status,&retsz);
    return status.sstat_outstrms;
}

int main(int argc,char **argv)
{
    //socket
    int sockfd=socket(AF_INET,SOCK_SEQPACKET,IPPROTO_SCTP);

    struct sockaddr_in servaddr,cliaddr;
    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(SERV_PORT);
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY);

    //bind
    bind(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr));

    struct sctp_event_subscribe events;
    bzero(&events,sizeof(events));
    events.sctp_data_io_event=1;//预定，每次recvmsg返回sctp_sndrcvifo
    setsockopt(sockfd,IPPROTO_SCTP,SCTP_EVENTS,&events,sizeof(events));

    //listen
    listen(sockfd,LISTENQ);
    
    char rdbuf[MAXLINE];
    struct sctp_sndrcvinfo sri;
    int flag,index=1;
    while(1)
    {
        socklen_t len=sizeof(struct sockaddr_in);
        size_t rd_sz=sctp_recvmsg(sockfd,rdbuf,sizeof(rdbuf),(struct sockaddr *)&cliaddr,&len,&sri,&flag);
        
        if(index)
        {
            ++sri.sinfo_stream;
            if(sri.sinfo_stream>=
             sctp_get_no_strms(sockfd,(struct sockaddr *)&cliaddr,len,sri))//如果流号增长到大于等于最大流号，重新置为0
                sri.sinfo_stream=0;
        }
        /*
         * 服务器在发送完消息后终止关联，设置MSG_EOF标志。该标志迫使发送消
         * 被客户确认后，相应的关联终止
         */
        sctp_sendmsg(sockfd,rdbuf,rd_sz,(struct sockaddr *)&cliaddr,len,sri.sinfo_ppid,(sri.sinfo_flags),sri.sinfo_stream,0,0);
    }
    return 0;

}

