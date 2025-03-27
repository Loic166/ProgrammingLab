# include <stdio.h>
# include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}node;

node *Creat_node(int x){
    node * new_node =(node*)malloc(sizeof(node));
    new_node ->data = x;
    new_node ->next = NULL;
    return new_node;
}

void stamp_list(node *testa){
    if(testa == NULL){
        printf("la lista è vueìota");
        return;
    }
    printf("{");
    while(testa != NULL){
        printf("%d ",testa->data);
        testa = testa->next;
    }
    printf("}");
}

int main(){
   node *a = Creat_node(23);
    stamp_list(a);
}