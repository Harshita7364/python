import sqlite3

con = sqlite3.connect('youtube_video.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,   
               time TEXT NOT NULL
    )
''')

def  list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?,?)",(name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos where id = ?",(id,))
    con.commit()

def main():
    while True:
        print("\n YOUTUBE MANAGER  | choose your option")
        print("1. list all video")
        print("2. add video")
        print("3. update video")
        print("4. delete video")
        print("5. exit")

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("enter the name: ")
                time = input("enter the time: ")
                add_video(name, time)
            case '3':
                video_id = input("enter update id: ")
                name = input("enter the name: ")
                time = input("enter the time: ")
                update_video(video_id, name, time)
            case '4':
                id = input("enter delete id: ")
                delete_video(id)
            case '5':
                break
            case _:
                print("invalid choice")

    con.close()



if __name__ == "__main__":
    main()