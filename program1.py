
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("#" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.Name: {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("#" * 70)

    
def add_video(videos):
    name = input("enter name:")
    time = input("enter time:")
    videos.append({'name': name, 'time': time})
    load_data()

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter update number:"))
    if 1 <= index <= len(videos):
        name = input("enter new name:")
        time = input("enter time:")
        videos[index-1] = {'name':name,'time':time}
        save_data(videos)
    else:
        print("invalid")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter number :"))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("invalid")

def main():
    videos = load_data()
    while True:
        print("\n YOUTUBE MANAGER  | choose your option")
        print("1. list all video")
        print("2. add video")
        print("3. update video")
        print("4. delete video")
        print("5. exit")

        choice = input("Enter your choice:")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()

