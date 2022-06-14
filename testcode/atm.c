#include<stdio.h>
int main(){
    float y;
    int x;
    scanf("%d %f",&x,&y);
    if(x%5==0&&x<y){
        y=y-x-0.50;
        printf("%.2f",y);
    }
    else{
        printf("%.2f",y);
    }
    return 0;
}