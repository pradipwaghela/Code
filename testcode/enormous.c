#include<stdio.h>
#include<stdlib.h>

int main(){
    int n,k,t,cnt=0;
    scanf("%d %d \n",&n,&k);
    for(int i=0;i<n;i++){
        scanf("%d",&t);
        if (t%k==0)
        {
            cnt++;
        }
    }

printf("\n%d\n",cnt);
return 0;
}