import sqlite3

from datetime import datetime



DATABASE="chat_history.db"




def create_table():


    conn=sqlite3.connect(
        DATABASE
    )


    cursor=conn.cursor()


    cursor.execute(

    """

    CREATE TABLE IF NOT EXISTS messages(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_message TEXT,

    bot_response TEXT,

    timestamp TEXT

    )

    """

    )


    conn.commit()

    conn.close()





def save_message(user,bot):


    conn=sqlite3.connect(
        DATABASE
    )


    cursor=conn.cursor()



    cursor.execute(

    """

    INSERT INTO messages

    (user_message,bot_response,timestamp)

    VALUES(?,?,?)

    """,

    (

        user,

        bot,

        datetime.now()

    )

    )


    conn.commit()

    conn.close()





def get_messages():


    conn=sqlite3.connect(
        DATABASE
    )


    cursor=conn.cursor()


    cursor.execute(

    """

    SELECT user_message,bot_response

    FROM messages

    ORDER BY id

    """

    )


    data=cursor.fetchall()


    conn.close()


    return data