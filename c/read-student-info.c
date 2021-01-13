/*       _\|/_
         (o o)
 +----oOO-{_}-OOo-------------------------------------------------------------+
 |Create a structure named college that has name roll-no, semester and grade  |
 |as memebers; assume appropriate type and size of members. Use this strucutre|
 |to read records of a 100 students. Write this array of structure to a file  |
 |and read its content to display on the screen whose grade is A.             |
 +---------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h> // for exit() function

struct college {
    char name[20];
    int roll;
    int sem;
    char grade;
};

int main() {
    struct college student_info[100]; // array of structures
    FILE *fptr;
    register int i;

    // writing to the structure

    for (i=0;i<3;i++) {
        printf("Enter Name ");
        scanf("%s",student_info[i].name);

        printf("Enter roll ");
        scanf("%d",&student_info[i].roll);

        printf("Enter sem ");
        scanf("%d",&student_info[i].sem);

        printf("Enter grade ");
        scanf(" %c",&student_info[i].grade);

        printf("\n");
    }

    // read the strucutre and print student_info if grade is A

    for (i=0;i<3;i++){
        if (student_info[i].grade == 'A')
            printf("Name %s\n Roll No. %d\n Semester %d \n Grade %c\n\n",
                    student_info[i].name,student_info[i].roll,student_info[i].sem,student_info[i].grade);
    }

    // writing the array of structures onto a file

    if ((fptr = fopen("student-info.txt","w")) == NULL) {
        printf("Error! File not opened");
        exit(1);
    }

    for (i=0;i<3;i++) {
    fprintf(fptr,"%s ",student_info[i].name);
    fprintf(fptr,"%d ",student_info[i].roll);
    fprintf(fptr,"%d ",student_info[i].sem);
    fprintf(fptr,"%c ",student_info[i].grade);
    fprintf(fptr,"\n");
   }

    fclose(fptr);

    return 0;
}
