/*
 * File: main.c
 * File Created: Thursday, 7th November 2019 8:36:59 pm
 * Author: Jonathon Winter
 * -----
 * Last Modified: Saturday, 9th November 2019 5:39:54 pm
 * Modified By: Jonathon Winter
 * -----
 * Purpose: 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <assert.h>

#define TEST(x) if(x){return;}

void func(char* name);

int hello = 1;

void idk5()
{
   int x = 5;

   if(x > 1)
   {
      return;
   }
}

void func(char* name)
{
   int x;
   char buff[100];
   if(name == NULL){
      return;
   }

   

   while(1==1){}

   do{
   }while(0);

   switch(x){
      case 1:
         break;
      case 2:
         goto idk;
      default:
         for(;;){
            break;
         }
   }

   idk:

   x=7;
   for(int ii = 0; ii < 1;ii++){
      if( ii < 1)
         break;
      else
         continue;
   }

   if(0)
      exit(0);

   TEST(0)

   strcpy(buff,name);
   
}

void perfect()
{
   int x = 1;
   return x;
}

int idk2()
{
   #ifdef HEHE
      return 1;
   #endif
   printf("idk");
   return 5;
   int x = 4;
}

int main(int argc, char *argv[])
{
   assert(1);
   func(argv[1]);
   return 0;
}
