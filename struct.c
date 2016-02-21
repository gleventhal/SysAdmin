#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
/* An exercise in structs */

struct dad {
    bool meet;
    int  age;
    bool nice;
    char * name;
};
typedef struct dad Dad;

// Prototype
void get_dad(Dad *d);

int main()
{

    struct dad mitch;
    mitch.name = "mitch";
    mitch.age  = 42;
    mitch.nice = true;
    mitch.meet = false;

    Dad *mitchref = &mitch;
 
   get_dad(mitchref); 

}

   void get_dad(Dad *d) {
        char cmd[48];
        strcpy(cmd, "/usr/bin/say -v tarik Did I meet that dad?");
        system(cmd);
        printf("Did I meet that dad?\n");
        if(d->meet) { 
            printf("YES!\n");
         } else { 
            printf("NO!\n");
         }
        printf("How old is that Dad?\n%d!\n", d->age);
        printf("Is that dad nice?\n");
        if(d->nice) {
            printf("YES!\n");
        } else {
            printf("NO!\n");
        }
        printf("What's that dad's name?\n%s!\n", d->name);
}
