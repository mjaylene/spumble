from tkinter import *
import parse_saved_tracks
import spotipy
import spotipy.util as util
import time
from tkinter import font

global index 
index = 1

def pad_box(song_container):
    for i in range(4):
        song_container.insert(i, "")


def superlike_func(window, song_container, tracks, sp, superlike, button):
    global index
    if index == 20:
        index = 1
        window.destroy()
        return
    song_container.delete(0, 'end')
    superlike.append(tracks[index-1])
    uri = tracks[index]
    track = sp.track(uri)
    song = f"{track['artists'][0]['name']} - {track['name']}"
    pad_box(song_container)
    song_container.insert(4, song)
    index += 1
    button.grid_forget()
  
    window.mainloop()


def swipe_right_func(window, song_container, tracks, sp, likes):
    global index
    if index == 20:
        index = 1
        window.destroy()
        return
    song_container.delete(0, 'end')
    likes.append(tracks[index-1])
    uri = tracks[index]
    track = sp.track(uri)
    song = f"{track['artists'][0]['name']} - {track['name']}"
    pad_box(song_container)
    song_container.insert(4, song)
    font_size = font.Font(size=25)
    song_container.config(font=font_size)
    index += 1
  
    window.mainloop()


def swipe_left_func(window, song_container, tracks, sp):
    global index
    if index == 20:
        index = 1
        window.destroy()
        return
    song_container.delete(0, 'end')
    uri = tracks[index]
    track = sp.track(uri)
    song = f"{track['artists'][0]['name']} - {track['name']}"
    pad_box(song_container)
    song_container.insert(4, song)
    font_size = font.Font(size=25)
    song_container.config(font=font_size)
    index += 1
  
    window.mainloop()


def create_match_window(username, sp, tracks):
    global index
    window = Tk()
    window.title('Spumble')
    window.geometry("1000x500")
    window.configure(bg='gold2')

    #next_button = Button(window, text="Next Song", command=window.destroy)
    #next_button.pack(pady=20)
  
    # Song Display
    song_container = Listbox(window, bg="white", fg="black", width=50, height=10, justify='center')
    song_container.pack(pady=10)

    # Create Spumble Buttons
    swipe_left_img = PhotoImage(file='images/swipe_left_yellow.png')
    swipe_right_img = PhotoImage(file='images/swipe_right_yellow.png')
    super_like_img = PhotoImage(file='images/super_like_yellow.png')

    # Create Button Frame 
    button_frame = Frame(window, bg='blue')
    button_frame.pack()

    likes = []
    superlike = []

    swipe_left_btn = Button(button_frame, image=swipe_left_img, borderwidth=0, command= lambda: swipe_left_func(window, song_container, tracks, sp))
    swipe_right_btn = Button(button_frame, image=swipe_right_img, borderwidth=0, command= lambda: swipe_right_func(window, song_container, tracks, sp, likes))
    super_like_btn = Button(button_frame, image=super_like_img, borderwidth=0, command= lambda: superlike_func(window, song_container, tracks, sp, superlike, super_like_btn))

    swipe_left_btn.grid(row= 0, column=0)
    super_like_btn.grid(row= 0, column=1)
    swipe_right_btn.grid(row= 0, column=2)

    uri = tracks[0]
    track = sp.track(uri)
    song = f"{track['artists'][0]['name']} - {track['name']}"
    pad_box(song_container)
    song_container.insert(4, username + " now picking tracks!")
    song_container.insert(5, song)
    font_size = font.Font(size=25)
    song_container.config(font=font_size)
    

    window.mainloop()

    return likes, superlike 

def create_close_window(common_liked):
    window = Tk()
    window.title('Spumble')
    window.geometry("1000x500")
    window.configure(bg='gold2')

    song_container = Listbox(window, bg="white", fg="black", width=50, height=10, justify='center')
    song_container.pack(pady=20)

    pad_box(song_container)
    song_container.insert(4, "You have " + str(len(common_liked)) + " matches!")
    song_container.insert(5, "Playlists generated! Check your Spotify accounts.")
    song_container.insert(6, "Thank you for using Spumble <3")
    bolded = font.Font(weight='bold') # will use the default font
    font_size = font.Font(size=25)
    song_container.config(font=font_size)

    window.mainloop()


def main():
    tracks = get_saved_tracks() 
    window, song_container = create_match_window(sp, tracks)

if __name__ == '__main__':
    main()
