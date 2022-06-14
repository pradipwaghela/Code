#include<stdio.h>
int main(){
    int x;
    float y;
    scanf("%d %f",&x,&y);
    if(x%5==0){
        float z;
        z=y-(float)x-0.5;
        if (z<0)
        {
            printf("%0.2f",y);
        }
        else{
            printf("%0.2f",z);
        }
        
    }
    else{
        printf("%.2f",y);
    }
}