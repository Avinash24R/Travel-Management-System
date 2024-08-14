
import mysql.connector as con
import time
p=input('enter your mysql password : ')
mycon=con.connect(host='localhost',user='root',passwd=p)
mycur=mycon.cursor()
que='create database if not exists trip3;'
mycur.execute(que)
q1='use trip3;'
mycur.execute(q1)
q='create table if not exists personal_info(s_no int(4) primary key, name varchar(25) not null, age varchar(3) not null, gender varchar(9) not null, phone_no varchar(12) not null, email varchar(40), city varchar(20) not null);'
mycur.execute(q)
qu='create table if not exists traval_info(s_no int(4), departure_area varchar(25), destination varchar(25), traval_mode varchar(12), departure_timing varchar(8), arrival_timing varchar(8));'
mycur.execute(qu)

def personal_info():
          try:
               print('\n')
               print('='*235)

               print('!!!you are using personal_info table!!!'.center(160))
               print('you can press\n1 --> To insert values in the table\n2 --> To display the table\n3 --> To search in the table\n4 --> To delete some data from table\n5 --> Exit')
               p_ch=int(input('Enter your choice(press 1 to 5) : '))
               if p_ch==1:
                    insert_p()
               if p_ch==2:
                    dis_p()
               if p_ch==3:
                    serch_p()
               if p_ch==4:
                    delete_p()
               if p_ch==5:
                    menu()
               else:
                   print('you can press 1 to 5')
                   n=input('you wants to try again(press y or n) :')
                   if n=='y':
                        personal_info()
                   else:
                       menu()
                   
          except:
               print('you can press 1 to 5')
               n=input('you wants to try again(press y or n) :')
               if n=='y':
                    personal_info()
               else:
                   menu()
               

def traval_info():
     try:
               print('\n')
               print('='*235)

               print('!!!you are using traval_info table!!!'.center(160))
               print('you can press\n1 --> To insert values in the table\n2 --> To display the table\n3 --> To search in the table\n4 --> To delete some data from table\n5 --> Exit')
               p_cht=int(input('Enter your choice(press 1 to 5) : '))
               if p_cht==1:
                    insert_t()
               if p_cht==2:
                    dis_t()
               if p_cht==3:
                    serch_t()
               if p_cht==4:
                    delete_t()
               if p_cht==5:
                    menu()
               else:
                   print('you can press 1 to 5')
                   n=input('you wants to try again(press y or n) :')
                   if n=='y':
                        traval_info()
                   else:
                       menu()
                   
               
     except:
               print('you can press 1 to 5')
               n=input('you wants to try again(press y or n) :')
               if n=='y':
                    traval_info()
               else:
                   menu()
def both():
     try:
               print('\n')
               print('='*235)

               print('!!!you are using both the table!!!'.center(160))
               print('you can press\n1 --> To insert values in the tables\n2 --> To display the tables\n3 --> To search in the tables\n4 --> To delete some data from tables\n5 --> Exit')
               p_chb=int(input('Enter your choice(press 1 or 2 or 3 or 4 or 5) : '))
               if p_chb==1:
                    print('In which table you want to insert value\n1 --> In personal_info table\n2 --> In traval_info table')
                    t_c=int(input('Enter your choice (press 1 to 3) :'))
                    if t_c==1:
                         insert_p()
                    if t_c==2:
                         insert_t()
               if p_chb==2:
                    print(' which table you want to display\n1 --> for personal_info table\n2 --> for traval_info table\n3 --> for both the tables')
                    t_c2=int(input('Enter your choice (press 1 to 3) :'))
                    if t_c2==1:
                         dis_p()
                    if t_c2==2:
                         dis_t()
                    if t_c2==3:
                         qu='select * from personal_info p,traval_info t where p.s_no=t.s_no;'
                         mycur.execute(qu)
                         a=mycur.fetchall()
                         l=list(map(list,a))
                         #print(a)
                         gap=' '*2
                         h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
                         print(l)
                         print("="*160)
                         print(h)
                         print("_"*160) 
                         for i in l:
                                   rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:16s}{gap}{i[12]:15s}"
                                   print(rec)
                         print("_"*160)
                         both()
                    
               if p_chb==3:
                    print('In which table you want to search\n1 --> for personal_info table\n2 --> for traval_info table\n3 --> for both the tables')
                    t_c3=int(input('Enter your choice (press 1 or 2 :'))
                    if t_c3==1:
                         serch_p()
                    if t_c3==2:
                         serch_t()
                    if t_c3==3:
                         serch_b()
                         
               if p_chb==4:
                    print('In which table you want to delete\n1 --> for personal_info table\n2 --> for traval_info table')
                    t_c4=int(input('Enter your choice (press 1 or 2 :'))
                    if t_c4==1:
                         delete_p()
                    if t_c4==2:
                         delete_t()
                    
               if p_chb==5:
                    menu()
     except:
               print('wrong choice ')
               n=input('you wants to try again(press y or n) :')
               if n=='y':
                    both()
               else:
                   menu()
def insert_p():
     try:
          n=int(input('Enter how many recode you wants to insert :'))
          o='_'*40
          for i in range(n):
               s=int(input('Enter the s_no :'))
               n=input('Enter the name :')
               age=int(input('Enter the age :'))
               g=input('Enter the gender :')
               p=int(input('Enter the phnoe_no :'))
               e=input('Enter the email :')
               c=input('Enter the city :')
               q="insert into personal_info values(%s,%s,%s,%s,%s,%s,%s)"
               mycur.execute(q,(s,n,age,g,p,e,c))
               print('data entered successuflly')
               print(o,end='\n')
               mycur.execute('commit')
          personal_info()
     except:
          print('insert values correctly')
def dis_p():                              
     query='select * from personal_info;'
     mycur.execute(query)
     a=mycur.fetchall()
     l=list(map(list,a))
     #print(a)
     gap=' '*3
     h=f"{'s_no':^4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':^12s}{gap}{'Email':^40s}{gap}{'city':^20s}"
     print("="*140)
     print(h)
     print("_"*140) 
     for i in l:
          rec=f"{i[0]:^4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:^12s}{gap}{i[5]:^40s}{gap}{i[6]:^20s}"
          print(rec)
     print("_"*140)

     personal_info()
     
     
def serch_p():
     try:
          print('you can serch by \n1 -->s_no\n2 -->Name\n3 -->Age\n4 -->Gender\n5 -->Phone_no\n6 -->Email\n7 -->City\n8 -->Manually\n9 -->EXIT')
          b=int(input('Enter your choice(press 1 to 8) : '))
          if b==1:
               s=int(input('Enter the s_no :'))
               query='select * from personal_info where s_no=%s'
               d=(s,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':^4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':^12s}{gap}{'Email':^40s}{gap}{'city':^20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:^4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:^12s}{gap}{i[5]:^40s}{gap}{i[6]:^20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==2:
               s2=input('Enter the name :')
               query='select * from personal_info where name like %s'
               d=(s2,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':^4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':^12s}{gap}{'Email':^40s}{gap}{'city':^20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:^4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:^12s}{gap}{i[5]:^40s}{gap}{i[6]:^20s}"
                    print(rec)
               print("_"*140)

               personal_info()
               
          if b==3:
               s3=input('Enter the age :')
               query='select * from personal_info where age like %s'
               d=(s3,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':^4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':^12s}{gap}{'Email':^40s}{gap}{'city':^20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:^4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:^12s}{gap}{i[5]:^40s}{gap}{i[6]:^20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==4:
               s4=input('Enter the gender :')
               query='select * from personal_info where gender like %s'
               d=(s4,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==5:
               s5=int(input('Enter the phone_no :'))
               query='select * from personal_info where phone_no=%s'
               d=(s5,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==6:
               s6=input('Enter the email :')
               query='select * from personal_info where email like %s'
               d=(s6,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==7:
               s7=input('Enter the  city :')
               query='select * from personal_info where city like %s'
               d=(s7,)
               mycur.execute(query,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==8:
               q8=input('Enter your mysql query :')
               
               mycur.execute(q8)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}"
               print("="*140)
               print(h)
               print("_"*140) 
               for i in l:
                    rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}"
                    print(rec)
               print("_"*140)

               personal_info()
          if b==9:
               personal_info()
     except:
          print('insert values correctly')
def delete_p():
     try:
          print('you can delete by \n1 --> s_no\n2 --> Name\n3 --> Age\n4 --> Gender\n5 --> Phone_no\n6 --> Email\n7 --> City\n8 --> Manually\n9 --> EXIT')
          b=int(input('Enter your choice(press 1 to 8) : '))
          if b==1:
               s=int(input('Enter the s_no :'))
               c=input('Are you sure you want to delete the data (press y or n) :')
               if c=='y':
                    qurey='delete from personal_info where s_no=%s'
                    d=(s,)
               
                    mycur.execute(qurey,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==2:
               s2=input('Enter the name :')
               c2=input('Are you sure you want to delete the data (press y or n) :')
               if c2=='y':
                    qurey='delete from personal_info where name=%s'
                    d=(s2,)
                    mycur.execute(qurey,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
                    
          if b==3:
               s3=input('Enter the age :')
               c3=input('Are you sure you want to delete the data (press y or n) :')
               if c3=='y':
                    q='delete from personal_info where age=%s'
                    d=(s3,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
                    
          if b==4:
               s4=input('Enter the gender :')
               c4=input('Are you sure you want to delete the data (press y or n) :')
               if c4=='y':
                    q='delete from personal_info where gender=%s'
                    d=(s4,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==5:
               s5=input('Enter the phone_no :')
               c5=input('Are you sure you want to delete the data (press y or n) :')
               if c5=='y':
                    q='delete from personal_info where phone_no=%s'
                    d=(s5,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==6:
               s6=input('Enter the email :')
               c6=input('Are you sure you want to delete the data (press y or n) :')
               if c6=='y': 
                    q='delete from personal_info where email=%s'
                    d=(s6,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==7:
               s7=input('Enter the  city :')
               c7=input('Are you sure you want to delete the data (press y or n) :')
               if c7=='y':
                    q='delete from personal_info where city=%s'
                    d=(s7,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==8:
               q8=input('Enter your mysql query :')
               c8=input('Are you sure you want to delete the data (press y or n) :')
               if c8=='y':
                    mycur.execute(q8)
                    print("data deleted")
                    mycon.commit()
                    personal_info()
               else:
                    personal_info()
          if b==9:
               personal_info()
     except:
          print('insert values correctly')
               
def insert_t():
     try:
          n=int(input('Enter how many recode you wants to insert :'))
          for i in range(n):
               s=int(input('Enter the s_no :'))
               d_a=input('Enter the departure_area :')
               d=input('Enter the destination :')
               t_m=input('Enter the traval mode :')
               d_t=input('Enter the departure timing :')
               dt=input('Enter arrvial_timing :')
               q="insert into traval_info values(%s,%s,%s,%s,%s,%s);"
               d1=(s,d_a,d,t_m,d_t,dt)
               mycur.execute(q,d1)
               mycur.execute('commit')
               print('data entered successuflly')
               print('------------------------------')
               
          traval_info()
     except:
          print('insert values correctly')
def dis_t():
     query='select * from traval_info;'
     mycur.execute(query)
     a=mycur.fetchall()
     l=list(map(list,a))
     #print(a)
     gap=' '*3
     h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':15s}{gap}{'arrvial_timing':15s}"
     print("="*116)
     print(h)
     print("_"*116) 
     for i in l:
          rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
          print(rec)
     print("_"*116)
     traval_info()
def serch_t():
     try:
          print('you can serch by \n1 -->s_no\n2 -->Departure_area\n3 -->Destination\n4 -->Traval_mode\n5 -->Departure_timing\n6 -->Arrival_timing\n7-->Manually\n8 -->EXIT')
          b=int(input('Enter your choice(press 1 to 8) : '))
          if b==1:
               s=int(input('Enter the s_no :'))
               q='select * from traval_info where s_no=%s'
               d=(s,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==2:
               s2=input('Enter the departure_area :')
               q='select * from traval_info where departure_area like %s'
               d=(s2,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==3:
               s3=input('Enter the departure_area :')
               q='select * from traval_info where destination like %s'
               d=(s3,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==4:
               s4=input('Enter the traval_mode :')
               q='select * from traval_info where traval_mode like %s'
               d=(s4,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          
          if b==5:
               s6=input('Enter the departure_timing :')
               
               q='select * from traval_info where departure_timing like %s'
               d=(s6,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:45s}{gap}{i[2]:45s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==6:
               s7=input('Enter the arrival_timing :')
               
               q='select * from personal_info where arrival_timing like %s'
               d=(s7,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==7:
               q8=input('Enter your mysql query :')
               mycur.execute(q8)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*3
               h=f"{'s_no':4s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':12s}{gap}{'departure timing':18s}{gap}{'arrvial_timing':8s}"
               print(l)
               print("="*120)
               print(h)
               print("_"*120) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:25s}{gap}{i[3]:12s}{gap}{i[4]:18s}{gap}{i[5]:8s}"
                         print(rec)
               print("_"*120)
               traval_info()
          if b==8:
               traval_info()
     except:
          print('insert values correctly')
def delete_t():
     try:
          print('you can delete by \n1 -->s_no\n2 -->Departure_area\n3 -->Destination\n4 -->Traval_mode\n\n5 -->Departure_timing\n6 -->Arrival_timing\n7-->Manually\n8 -->EXIT')
          b=int(input('Enter your choice(press 1 to 8) : '))
          if b==1:
               s=int(input('Enter the s_no :'))
               ct=input('Are you sure you want to delete the data (press y or n) :')
               if ct=='y':
                    q='delete from traval_info where s_no=%s'
                    d=(s,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==2:
               s2=input('Enter the departure_area :')
               c2t=input('Are you sure you want to delete the data (press y or n) :')
               if c2t=='y':
                    q='select * from traval_info where departure_area=%s'
                    d=(s2,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==3:
               s3=input('Enter the destination :')
               c3t=input('Are you sure you want to delete the data (press y or n) :')
               if c3t=='y':
                    q='select * from traval_info where destination=%s'
                    d=(s3,)
               
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==4:
               s4=input('Enter the traval_mode :')
               c4t=input('Are you sure you want to delete the data (press y or n) :')
               if c4t=='y':
                    q='select * from traval_info where traval_mode=%s'
                    d=(s4,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          
          if b==5:
               s6=input('Enter the departure_timing :')
               c5t=input('Are you sure you want to delete the data (press y or n) :')
               if c5t=='y':
               
                    q='select * from traval_info where departure_timing=%s'
                    d=(s6,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==6:
               s7=input('Enter the arrival_timing :')
               c6t=input('Are you sure you want to delete the data (press y or n) :')
               if c6t=='y':
               
                    q='select * from traval_info where arrival_timing=%s'
                    d=(s7,)
                    mycur.execute(q,d)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==7:
               q8=input('Enter your mysql query :')
               c7t=input('Are you sure you want to delete the data (press y or n) :')
               if c7t=='y':
                    mycur.execute(q8)
                    print("data deleted")
                    mycon.commit()
                    traval_info()
               else:
                    traval_info()
          if b==8:
               traval_info()
     except:
          print('insert values correctly')               

def serch_b():
     try:
          print('you can serch by \n1 -->s_no\n2 -->Name\n3 -->Age\n4 -->Gender\n5 -->Phone_no\n6 -->eEmail\n7 -->City\n8 -->s_no\n9 -->Departure_area\n10 -->Destination\n11 -->Traval_mode\n12 -->Departure_timing\n13 -->Arrival_timing\n14-->Manually\n15 -->EXIT ')
          b3=int(input('Enter your choice(you can press from 1 to 14) : '))
          if b3==1:
               s=int(input('Enter the s_no :'))
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and p.s_no=%s'
               d=(s,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:17s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==2:
               s2=input('Enter the name :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and name like %s'
               d=(s2,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:16s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==3:
               s3=input('Enter the age :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and age like %s'
               d=(s3,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:16s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==4:
               s4=input('Enter the gender :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and gender like %s'
               d=(s4,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:16s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==5:
               s5=int(input('Enter the phone_no :'))
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and phone_no =%s'
               d=(s5,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:16s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==6:
               s6=input('Enter the email :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and email like %s'
               d=(s6,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==7:
               s7=input('Enter the  city :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and city like %s'
               d=(s7,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==8:
               print('you can serched by choice 1 ')
               '''s=int(input('Enter the s_no :'))
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and s_no=%s'
               d=(s,)
               mycur.execute(q,d)
               r=mycur.fetchall()
               for i in r:
               print(i,end=" ")'''
               
          if b3==9:
               s2=input('Enter the departure_area :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and departure_area like %s'
               d=(s2,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==10:
               s3=input('Enter the destination :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and destination like %s'
               d=(s3,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==11:
               s4=input('Enter the traval_mode :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no  and traval_mode like %s'
               d=(s4,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          
          if b3==12:
               s6=input('Enter the departure_timing :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and departure_timing like %s'
               d=(s6,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==13:
               s7=input('Enter the arrival_timing :')
               q='select * from personal_info p,traval_info t where p.s_no=t.s_no and arrival_timing like %s'
               d=(s7,)
               mycur.execute(q,d)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               both()
          if b3==14:
               q8=input('Enter your mysql query :')
               mycur.execute(q8)
               a=mycur.fetchall()
               l=list(map(list,a))
               #print(a)
               gap=' '*2
               h=f"{'s_no':4s}{gap}{'name':25s}{gap}{'age':3s}{gap}{'gender':9s}{gap}{'phone_no':12s}{gap}{'Email':40s}{gap}{'city':20s}{gap}{'departure_area':25s}{gap}{'destination':25s}{gap}{'traval mode':11s}{gap}{'departure timing':16s}{gap}{'arrvial_timing':15s}"
               print(l)
               print("="*160)
               print(h)
               print("_"*160) 
               for i in l:
                    if l==[]:
                         print('No Data entered')
                    else:
                         rec=f"{i[0]:4d}{gap}{i[1]:25s}{gap}{i[2]:3s}{gap}{i[3]:9s}{gap}{i[4]:12s}{gap}{i[5]:40s}{gap}{i[6]:20s}{gap}{i[8]:25s}{gap}{i[9]:25s}{gap}{i[10]:11s}{gap}{i[11]:18s}{gap}{i[12]:8s}"
                         print(rec)
               print("_"*160)
               mycon.commit()
               both()
          if b3==15:
               both()
     except:
          print('insert values correctly')
def menu():
     try:
          print('****************************** MENU**********************************'.center(160))
          p='='*306
          print(p)
          print('!!!welcome to traval form!!! '.center(160))
          print('There are two tables')
          print('  1 --> personal_info')
          print('  2 --> traval_info')
          print('you can choice your table\npress 1  if you wants to use personal_info table\npress 2  if you wants to ue traval_info table\npress 3  if you wants to use both tables\npress 4 if you want to EXIT \n')
          ch=int(input('Enter your choice(press 1 to 4) : '))
          if ch==1:
               personal_info()             
          if ch==2:
               traval_info()
          if ch==3:
               both()
          if ch==4:
               print('!!!Thank you for using my code!!!'.center(160))
          else:
              print('you can only choice from  1 to 4')
              n=input('you wants to try again(press y or n) :')
              if n=='y':
                   menu()
              if n=='n':
                   print('!!!Thank you for using my code!!!'.center(160))
                   
              
     except:
          print('you can choice from  1 to 4')
          n=input('you wants to try again(press y or n) :')
          if n=='y':
               menu()
          if n=='n':
               print('!!!Thank you for using my code!!!'.center(1600))
menu()
time.sleep(8)
