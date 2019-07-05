# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def separate_name(name):
    ln=name.split() #separate name by spaces in a list
    first_name=ln[0]
    #middle_name='' #It seems i dont need this
    last_name=ln[-1]
    #if (len(ln)==3): #this is not need but already there
    #    middle_name=ln[1] #this is not need it, can be probably delete
    return (first_name,last_name)

def get_email_tail(C):
    email_tail=('@%s.com'%(C.lower()))
    return(email_tail)

def make_unique_name(first_name,last_name,dic_emails):
    email_name=('%s%s'% (first_name.lower(),
                last_name.replace('-','').lower()))
    if email_name in dic_emails:
        dic_emails[email_name]+=1
        email_name=('%s%s'%(email_name,dic_emails[email_name]))
    else:
        dic_emails[email_name]=1
    return(email_name)

def solution(S, C):
    # write your code in Python 3.6
    list_names=S.split("; ") #list of names
    email_tail=get_email_tail(C)
    output_list=[]
    dic_emails={}
    output_string=''
    for name in list_names:
        first_name,last_name=separate_name(name)
        unique_name=make_unique_name(first_name,last_name,dic_emails)
        email=('%s%s'%(unique_name,email_tail))
        output_name=('%s <%s>; '% (name,email))
        print(output_name)
        output_string=('%s%s'%(output_string,output_name))
    output_string=output_string[0:len(output_string)-2]
    print('done')
    return output_string


solution('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example')
