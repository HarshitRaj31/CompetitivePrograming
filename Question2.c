/*Singly linklist*/

#include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node*next;
};
int main(){
 struct Node*head=NULL,*temp = NULL,*newNode = NULL,*prev=NULL,*nextNode=NULL, *current=head;
 int n,value;
 printf("Enter number of nodes: ");
 scanf("%d",&n);
 for (int i = 0; i < n; i++)
 {
 newNode = (struct Node *)malloc(sizeof(struct Node));
 printf("Enter value: ");
 scanf("%d",&value);
 newNode->data=value;
 newNode->next=NULL;
 if (head==NULL)
 {
    head=newNode;
    temp=head;
 }
 else{
    temp->next=newNode;
    temp=newNode;
 }
}
temp=head;
while(temp!=NULL){
    printf("%d ",temp->data);
    temp=temp->next;
}
printf(" NULL");
current = head;
while (current != NULL) {
    nextNode=current->next;  // Save next node
    current->next=prev;      // Reverse the link
    prev=current;            // Move prev forward
    current=nextNode;        // Move current forward
}

head = prev; 
temp=head;
while(temp!=NULL){
    printf("%d ",temp->data);
    temp=temp->next;
}
printf(" NULL");
return 0;

}
