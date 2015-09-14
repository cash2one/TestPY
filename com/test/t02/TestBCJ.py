#coding=utf-8

'''
Created on 2015年5月12日

@author: BFD474
'''

pre = pres[1050]
t= ts[1050]          # t 用于标记独立块的根结点

def Find(x):
     r=x;
     while(r!=pre[r]):
          r=pre[r]
     i=x,j;
     while(pre[i]!=r):
          j=pre[i];
          pre[i]=r;
          i=j;
     return r;

def mix(x,y)
     int fx=Find(x),fy=Find(y);
     if(fx!=fy):
          pre[fy]=fx;

if __name__ == '__main__':
     N,M,a,b,i,j,ans;
     while(scanf("%d%d",&N,&M)&&N):
          for(i=1;i<=N;i++):          #初始化
               pre[i]=i;
          for(i=1;i<=M;i++):          #吸收并整理数据
               scanf("%d%d",&a,&b);
               mix(a,b);
          memset(t,0,sizeof(t));
          for(i=1;i<=N;i++):          #标记根结点
               t[Find(i)]=1;
          for(ans=0,i=1;i<=N;i++)
               if(t[i])
                    ans++;
          printf("%d\n" % (ans-1));

     return 0;
# dellaserss
