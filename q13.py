# Q13}Write a function RECOUNT( ) to read the contents of a binary file 
#    ‘NAMES.DAT’ and display number of records (each name occupies 20 
#     bytes in  file)  in it.
import os 
def RECCOUNT(): 
 size_of_rec = 20  #Each name will occupy 20 bytes 
 file_len = os.path.getsize('NAMES.dat') 
 num_record = file_len/size_of_rec 
 print("Total Records are :",num_record)