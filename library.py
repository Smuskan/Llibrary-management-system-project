#   project name    : Library management system
#   made by         : Muskan S.

import mysql.connector
from datetime import date

fine_per_day =5.0  #global variable

def clear():
  for _ in range(1):
     print


def add_book():
  conn = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
  cursor = conn.cursor()

  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Book Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  copies  = int(input('Enter copies : '))
  sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
   #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  for _ in range(0,copies):
    cursor.execute(sql)
  conn.close()
  print('\n\nNew Book added successfully')
  wait = input('\n\n\n Press any key to continue....')


def add_member():
  conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='')
  cursor = conn.cursor()

  name = input('Enter Member Name :')
  clas = input('Enter Member Class & Section : ')
  address = input('Enter Member Address : ')
  phone = input('Enter Member Phone  : ')
  email = input('Enter Member Email  : ')
  
 
  sql = 'insert into member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
  #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  
  cursor.execute(sql)
  conn.close()
  print('\n\nNew Member added successfully')
  wait = input('\n\n\n Press any key to continue....')


def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    clear()
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n6. Book Edition')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title'
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    if field =='pages' or field == 'price':
        sql = 'update book set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
        sql = 'update book set ' + field + ' = "'+value+'" where id = '+book_id+';'
    #print(sql)
    cursor.execute(sql)
    print('\n\n\nBook details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def modify_member():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    clear()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    mem_id =input('Enter member ID :')
    value = input('Enter new value :')
    sql = 'update member set '+ field +' = "'+value+'" where id = '+mem_id+';'
    #print(sql)
    cursor.execute(sql)
    print('Member details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def mem_issue_status(mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    sql ='select * from transaction where m_id ='+mem_id +' and dor is NULL;'
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def book_status(book_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    sql = 'select * from book where id ='+book_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[5]

def book_issue_status(book_id,mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    sql = 'select * from transaction where b_id ='+book_id + ' and m_id ='+ mem_id +' and dor is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def issue_book():
    conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id  = input('Enter Member ID :')
   
    
    result = book_status(book_id)
    result1 = mem_issue_status(mem_id)
    #print(result1)
    today = date.today()
    if len(result1) == 0:
      if result == 'available':
          sql = 'insert into transaction(b_id, m_id, doi) values('+book_id+','+mem_id+',"'+str(today)+'");'
          sql_book = 'update book set status="issue" where id ='+book_id + ';'
          cursor.execute(sql)
          cursor.execute(sql_book)
          print('\n\n\n Book issued successfully')
      else:
          print('\n\nBook is not available for ISSUE... Current status :',result1)
    else:
      if len(result1)<1:
        sql = 'insert into transaction(b_id, m_id, doi) values(' + \
             book_id+','+mem_id+',"'+str(today)+'");'
        sql_book = 'update book set status="issue" where id ='+book_id + ';'
        #print(len(result))
        cursor.execute(sql)
        cursor.execute(sql_book)
        print('\n\n\n Book issued successfully')
      else:
        print('\n\nMember already have book from the Library')
      #print(result)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def return_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    global fine_per_day
    clear()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id = input('Enter Member ID :')
    today =date.today()
    result = book_issue_status(book_id,mem_id)
    if result==None:
       print('Book was not issued...Check Book Id and Member ID again..')
    else:
       sql='update book set status ="available" where id ='+book_id +';'
       din = (today - result[3]).days
       fine = din * fine_per_day    #  fine per data
       sql1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+mem_id+' and dor is NULL;' 
       
       cursor.execute(sql)
       cursor.execute(sql1)
       print('\n\nBook returned successfully')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_book(field):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from book where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_menu():
    while True:
      clear()
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_book(field)


def reprot_book_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES ')
    print('-'*120)
    sql ='select * from book'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_issued_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Issued')
    print('-'*120)
    sql = 'select * from book where status = "issue";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_available_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Available')
    print('-'*120)
    sql = 'select * from book where status = "available";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_weed_out_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Weed Out')
    print('-'*120)
    sql = 'select * from book where status = "weed-out";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_stolen_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Stolen')
    print('-'*120)
    sql = 'select * from book where status = "stolen";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_lost_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - lost')
    print('-'*120)
    sql = 'select * from book where status = "lost";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_member_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - Members List ')
    print('-'*120)
    sql = 'select * from member'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_fine_collection():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    sql ='select sum(fine) from transaction where dor ="'+str(date.today())+'";'
    cursor.execute(sql)
    result = cursor.fetchone() #always return values in the form of tuple
    clear()
    print('Fine collection')
    print('-'*120)
    print('Total fine collected Today :',result[0])
    print('\n\n\n')
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_menu():
    while True:
      clear()
      print(' R E P O R T    M E N U ')
      print("\n1.  Book List")
      print('\n2.  Member List')
      print('\n3.  Issued Books')
      print('\n4.  Available Books')
      print('\n5.  Weed out Book')
      print('\n6.  Stolen Book')
      print('\n7.  Lost Book')
      print('\n8.  Fine Collection')
      print('\n9.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        reprot_book_list()
      if choice == 2:
        report_member_list()
      if choice == 3:
        report_issued_books()
      if choice == 4:
        report_available_books()
      if choice == 5:
        report_weed_out_books()
      if choice == 6:
        report_stolen_books()
      if choice == 7:
        report_lost_books()
      if choice == 8:
        report_fine_collection()
      if choice == 9:
        break


def change_book_status(status,book_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = conn.cursor()
    sql = 'update book set status = "'+status +'" where id ='+book_id + ' and status ="available"'
    cursor.execute(sql)
    print('Book status changed to ',status)
    print('\n\n\n')
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')

def special_menu():

    while True:
      clear()
      print(' S P E C I A L     M E N U')
      print("\n1.  Book Stolen")
      print('\n2.  Book Lost')
      print('\n3.  Book Weed out')
      print('\n4.  Return Book')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      status=''
      if choice == 1:
         status ='stolen'
      if choice == 2:
         status = 'lost'
      if choice == 3:
         status = 'weed-out'
      if choice == 4:
         break
      book_id = input('Enter book id :')
      change_book_status(status,book_id)


def main_menu():
    while True:
      clear()
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Book Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue Book')
      print('\n6.  Return Book')
      print('\n7.  Search Menu')
      print('\n8.  Report Menu')
      print('\n9.  Special Menu')
      print('\n0.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()
      if choice == 9:
        special_menu()
      if choice == 0:
        break


if __name__ == "__main__":
    main_menu()
