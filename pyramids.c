#include <stdio.h>

int main(void)
{
    int len;

    do
    {
        printf("Enter the pyramid length value:");
        scanf("%d", &len);
    }
    while (len < 1 || len > 257);
    
    
    int blanks = len - 1;

    for (int i = 0; i <= len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if ( j <= blanks )
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");

        for (int y = len; y > 0; y--)
        {
            if ( y <= blanks + 1 )
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
        blanks--;
    }
}
