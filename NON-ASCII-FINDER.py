import mysql.connector
import smtplib
from email.mime.text import MIMEText

# trying to connect to remote database using mysql connector (can be done locally also of course)
mariaconnect = mysql.connector.connect(host='localhost/ IP-Address',
                                       user='username',
                                       password='XXXXXXX')
# checking if connection is initiated successfully, if so print db version.
if mariaconnect.is_connected():
    db_Info = mariaconnect.get_server_info()
    print("Successfully connected to your database : ", db_Info)
    print("Searching for NON-ASCII Characters... \n")


def nonascii_select1():
    # Initiating cursor (cursor is the initiator that executes SQL commands for e.g ; fetching data (SELECT) against the
    # SQL server)

    cursor = mariaconnect.cursor()
    # execute cursor against SOME_TABLE
    cursor.execute(
        "SELECT * FROM SOMETHING.SOMETHING WHERE SOMETHING <> CONVERT(SOMETHING USING ASCII); ")
    select_query1 = cursor.fetchall()
    select_query1_results = cursor.rowcount

    print("Total number of rows with NON-ASCII Characters in SOMETHING.SOMETHING.SOMETHING: ",
          select_query1_results)

    # will only print relevant information and the lines that could be "filled" no need to print all the columns of the
    # table, (only fields that can be changed by a user accidentally or intentionally)
    for row in select_query1:
        print("SOME_ROW: ", row[0])
        print("SOME_ROW1: ", row[1])
        print("SOME_ROW2: ", row[2])
        print("SOME_ROW3: ", row[35])
        print("SOME_ROW4: ", row[36])
        print("SOME_ROW5: ", row[49])
        print("SOME_ROW6: ", row[50], '\n')

    return select_query1_results


def nonascii_select2():
    # Initiating cursor (cursor is the initiator that executes SQL commands for e.g ; fetching data (SELECT) against the
    # SQL server)
    cursor = mariaconnect.cursor()
    # execute cursor against SOME_TABLE
    cursor.execute(
        "SELECT * FROM SOMETHING WHERE SOMETHING <> CONVERT(SOMETHING USING ASCII);")
    select_query2 = cursor.fetchall()
    select_query2_results = cursor.rowcount
    print("Total number of rows with NON-ASCII Characters in SOME_TABLE: ",
          select_query2_results)

    # will only print relevant information and the lines that could be "filled" no need to print all the columns of the
    # table, (only fields that can be changed by a user accidentally or intentionally)
    for row in select_query2:
        print("SOME_ROW:", row[0])
        print("SOME_ROW1: ", row[1])
        print("SOME_ROW2: ", row[2])
        print("SOME_ROW3: ", row[3])
        print("SOME_ROW4: ", row[23])
        print("SOME_ROW5", row[24], '\n')

    return select_query2_results


def nonascii_select3():
    # Initiating cursor (cursor is the initiator that executes SQL commands for e.g ; fetching data (SELECT) against the
    # SQL server)
    cursor = mariaconnect.cursor()
    # execute cursor against SOME_TABLE
    cursor.execute(
        "SELECT * FROM SOMETHING WHERE SOMETHING_ELSE <> CONVERT(SOMETHING_ELSE USING ASCII);")
    select_query3 = cursor.fetchall()
    select_query3_results = cursor.rowcount
    print("Total number of rows with NON-ASCII Characters in SOMETHING.SOMETHING_ELSE: ",
          select_query3_results)

    # will only print relevant information and the lines that could be "filled" no need to print all the columns of the
    # table, (only fields that can be changed by a user accidentally or intentionally)
    for row in select_query3:
        print("SOME_ROW:", row[0])
        print("SOME_ROW1: ", row[1])
        print("SOME_ROW2: ", row[2])
        print("SOME_ROW3: ", row[3])
        print("SOME_ROW4: ", row[4])
        print("SOME_ROW5: ", row[5], '\n')

    return select_query3_results


def nonascii_select4():
    # Initiating cursor (cursor is the initiator that executes SQL commands for e.g ; fetching data (SELECT) against the
    # SQL server)
    cursor = mariaconnect.cursor()
    # execute cursor against SOME_TABLE
    cursor.execute(
        "SELECT * FROM SOMETHING WHERE SOMETHING_ELSE <> CONVERT(SOMETHING_ELSE USING ASCII);")
    select_query4 = cursor.fetchall()
    select_query4_results = cursor.rowcount
    print("Total number of rows with NON-ASCII Characters in SOMETHING.SOMETHING_ELSE: ",
          select_query4_results)

    # will only print relevant information and the lines that could be "filled" no need to print all the columns of the
    # table, (only fields that can be changed by a user accidentally or intentionally)
    for row in select_query4:
        print("SOME_ROW:", row[0])
        print("SOME_ROW1: ", row[3])
        print("SOME_ROW2: ", row[4])
        print("SOME_ROW3: ", row[5])
        print("SOME_ROW4: ", row[8])
        print("SOME_ROW5", row[9])
        print("SOME_ROW6: ", row[10])
        print("SOME_ROW7:", row[11], '\n')

    return select_query4_results


def nonascii_select5():
    # Initiating cursor (cursor is the initiator that executes SQL commands for e.g ; fetching data (SELECT) against the
    # SQL server)
    cursor = mariaconnect.cursor()
    # execute cursor against SOME_TABLE
    cursor.execute(
        "SELECT * FROM SOMETHING WHERE SOMETHING_ELSE <> CONVERT(SOMETHING_ELSE USING ASCII);")
    select_query5 = cursor.fetchall()
    select_query5_results = cursor.rowcount
    print("Total number of rows with NON-ASCII characters in SOMETHING.SOMETHING_ELSE: ",
          select_query5_results)

    # will only print relevant information and the lines that could be "filled" no need to print all the columns of the
    # table, (only fields that can be changed by a user accidentally or intentionally)
    for row in select_query5:
        print("SOME_ROW:", row[0])
        print("SOME_ROW1: ", row[1])
        print("SOME_ROW2: ", row[2])
        print("SOME_ROW3: ", row[3])
        print("SOME_ROW4: ", row[7])
        print("SOME_ROW5", row[26])
        print("SOME_ROW6: ", row[35], '\n')

    return select_query5_results


def send_email_if_non_ascii_found(msg):
    # connect with google smtp server
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465

    # Login credentials
    username = 'GMAIL ADDRESS'
    password = 'GMAIL PASSWORD'

    # From where to where
    from_addr = 'GMAIL ADDRESS'
    to_addr = ['tomerschwartz@candidate.com']

    # assign variables and create body for the message
    message = MIMEText(msg)
    message['subject'] = 'Demonstrating my python experience'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addr)

    # connecting using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()


# Call all functions

select1 = nonascii_select1()
select2 = nonascii_select2()
select3 = nonascii_select3()
select4 = nonascii_select4()
select5 = nonascii_select5()

if select1 >= 1:
    send_email_if_non_ascii_found(
        'NON ASCII characters have been found in the candidate application :)')
elif select1 == 0:
    exit()

if select2 >= 1:
    send_email_if_non_ascii_found(
        'NON ASCII characters have been found in the candidate application :)')
elif select2 == 0:
    exit()

if select3 >= 1:
    send_email_if_non_ascii_found(
        'NON ASCII characters have been found in the candidate application :)')

if select4 >= 1:
    send_email_if_non_ascii_found(
        'NON ASCII characters have been found in the candidate application :)')

elif select4 == 0:
    exit()

if select5 >= 1:
    send_email_if_non_ascii_found(
        'NON ASCII characters have been found in the candidate application :)')

elif select5 == 0:
    exit()
# Author - Tomer Schwartz
# tomerschwartz2411@gmail.com
