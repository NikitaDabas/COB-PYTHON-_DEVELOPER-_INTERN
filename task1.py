#write a program to read a text file and find all unique words and how many times the word occurences.
from tabulate import tabulate

try:
    u_file=input('Enter the name of text file: ')
    file=open(f'{u_file}')
    
    
    #for reading file content
    content=file.read()
    f_content=content.lower()
    f_list=f_content.split()
    displayed=[]

    if f_list!=[]:
        print('The file content is :')
        print(content)
        print('$$$----------------------------------------------------------------------------------------------$$$')
        
        #table heading
        head=['WORD','OCCOURENCE']
        
        output=[]
        for i in f_list:
            if i not in displayed:
                a=[i,f_list.count(i)]
                output.append(a)
                displayed.append(i)
        print(tabulate(output,headers=head,tablefmt='grid'))
        print('$$$$-------------------------------THANK YOU-----------------------------------------------------------------------$$$')
        

    else:
        print('File is blank.')

except FileNotFoundError:
    print(f'{u_file} not found!!!\nPlease enter a valid file name.')
        
