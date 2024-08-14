l1=['_','_','_','_','_','_','_','_','_']
turn=1
while turn<10:

   if turn%2==0:
      pos=int(input("joy enter the pos. "))
      l1[pos-1]='x'
      if pos==pos:
         print("you can not enter same position repeatatly " ) 
   

   else:
      pos=int(input("jay enter the pos. "))
      l1[pos-1]='0'
      if pos==pos:
         print("you can not enter same position repeatatly " ) 

   print("after",turn)  
   print(l1[0],'|',l1[1],'|',l1[2])
   print(l1[3],'|',l1[4],'|',l1[5])
   print(l1[6],'|',l1[7],'|',l1[8])

   if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='0':
      print("jay is winner")
      turn=15
   elif l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='x':
      print("joy is winner")
      turn=15
   elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='0':
      print("jay is winner")
      turn=15
   elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='x':
      print("joy is winner")
      turn=15
   elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='0':
      print("jay is winner")
      turn=15
   elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='x':
      print("joy is winner")
      turn=15
   elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='0':
      print("jay is winner")
      turn=15
   elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='x':
      print("joy is winner")
      turn=15
   elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='0':
      print("jay is winner")
      turn=15
   elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='x':
      print("joy is winner")
      turn=15
   elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='0':
      print("jay is winner")
      turn=15
   elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='x':
      print("joy is winner")
      turn=15
   elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='0':
      print("jay is winner")
      turn=15
   elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='x':
      print("joy is winner")
      turn=15
   elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='0':
      print("jay is winner")
      turn=15
   elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='x':
      print("joy is winner")
      turn=15
   


   turn=turn+1

print(turn)
if turn==10:
   print("the game is tie")


