#!/usr/bin/python3

'''
File: main.py
File Created: Thursday, 7th November 2019 8:31:10 pm
Author: Jonathon Winter
-----
Last Modified: Sunday, 10th November 2019 2:14:54 am
Modified By: Jonathon Winter
-----
Purpose: 
'''


from stuff import *

import sys
import os
from glob import glob

# print(find_library('clang'))

import cParse as UCP
import jParse as OOPD

def getParent(tNode):
   interested = [Kind.TOP, Kind.FUNCTION, Kind.SWITCH, Kind.LOOP,Kind.IF]

   if tNode.parent.kind in interested:
      return tNode.parent
   else:
      return getParent(tNode.parent)

def getFunction(tNode):
   if tNode.kind == Kind.FUNCTION:
      return tNode.spelling
   if tNode.kind == Kind.TOP:
      return os.path.basename(tNode.spelling)
   else:
      return getFunction(tNode.parent)

def extractRec(tNode, cursed):

   cursed_statements = [Kind.BREAK, Kind.GOTO, Kind.CONTINUE, Kind.RETURN, Kind.VARIABLE]

   cursed_functions = ["exit","__assert_fail"]

   bad = False

   if tNode is not None:
      if tNode.kind == Kind.FUNC_CALL:
         if tNode.spelling in cursed_functions:
            bad = True
            message = "Illegal Function {}".format(tNode.spelling)
      elif tNode.kind in cursed_statements:
         parent = getParent(tNode)

         if tNode.kind == Kind.VARIABLE:
            if parent.kind == Kind.TOP:
               bad = True
               message = "Global Variable {}".format(tNode.spelling)
         elif tNode.kind == Kind.BREAK:
            if parent.kind != Kind.SWITCH:
               bad = True
               message = "Use of BREAK"
         elif tNode.kind == Kind.RETURN:
            if parent.kind != Kind.FUNCTION:
               bad = True
               message = "Multiple Returns"
            elif parent.children[-1] != tNode:
               bad = True
               message = "Code after Return"
         else:
            bad = True
            message = "Use of {}".format(tNode.kind.name)

      if bad:

         func = getFunction(tNode)
         curse = Curse(tNode, message, func)

         if not func in cursed:
            cursed[func] = []

         cursed[func].append(curse)

      else:
         pass
         # print(padding, color,tNode.kind.name, "{}:{}".format(tNode.raw.location.file,tNode.raw.location.line))

      
   for child in tNode.children:
      extractRec(child, cursed)

def extract(head):
   cursed = {}
   extractRec(head, cursed)


   if len(cursed) == 0:
      cursed = None

   return cursed

if __name__ == "__main__":

   files = glob(sys.argv[1]);

   for filename in files:
      tree = UCP.parse(filename)

      filename = os.path.basename(filename)

      if tree is not None:
         cursed = extract(tree)
         if cursed is not None:
            print("="*80)
            print("||",filename.center(74,' '),"||")
            print("||","-"*74,"||")
            for key,values in cursed.items():
               print("||","{:74}".format(key),"||")
               for v in values:
                  print("||","  {:3} : {:66}".format(v.node.raw.location.line, v.message),"||")
            print("="*80)
            print()
            

   

   
   