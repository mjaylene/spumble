from tkinter import *
import pygame
#import create_playlist
#from matchmaker import MatchMaker, User
import parse_saved_tracks
import spotipy
import spotipy.util as util
import time
import auth 
auth.init()

global index 
index = 0

def next_track(window):
    window.destroy()

def get_saved_tracks():
    offset = 0
    tracks = []
    results = auth.sp.current_user_saved_tracks(limit=50)
    while (results['items']):
        for item in results['items']:
            track = item['track']
            tracks.append(track['uri'])
        offset += 50
        results = auth.sp.current_user_saved_tracks(limit=50, offset=offset)
    return tracks

def populate_match_window(window, song_container, tracks):
    '''
    user = User('jayjaymobbles')

    for i in range(20):
        uri = user.tracks[i]
        track = user.sp.track(uri)
        song = track['artists'][0]['name'], " - ", track['name']
        song_container.insert(END, song) 
    '''
    #pygame.init()
    #user = User('jayjaymobbles')
    global index
    uri = tracks[index]
    track = auth.sp.track(uri)
    song = track['artists'][0]['name'], " - ", track['name']
    song_container.insert(0, song)
    index += 1


    '''
        for event in pygame.event.get():
            if event.type == pygame.K_RIGHT:
                likes.append(uri)
                song_container.insert(i, song)
            if event.type == pygame.K_SPACE:
                likes.append(uri)
                superliked = True
                super_like()
            if event.type == pygame.K_LEFT:
                song_container.insert(i, song)
    '''
  
    window.mainloop()

def super_like(i, song):
    song_container.insert(i, song)


def create_match_window(tracks):
    window = Tk()
    window.title('Spumble')
    window.geometry("500x520")
    window.configure(bg='gold2')

    #next_button = Button(window, text="Next Song", command=window.destroy)
    #next_button.pack(pady=20)
  
    # Song Display
    song_container = Listbox(window, bg="white", fg="black", width=50, height=20)
    song_container.pack(pady=20)

    # Create Spumble Buttons
    swipe_left_img = PhotoImage(file='images/swipe_left_yellow.png')
    swipe_right_img = PhotoImage(file='images/swipe_right_yellow.png')
    super_like_img = PhotoImage(file='images/super_like_yellow.png')

    # Create Button Frame 
    button_frame = Frame(window, bg='blue')
    button_frame.pack()

    swipe_left_btn = Button(button_frame, image=swipe_left_img, borderwidth=0, command= lambda: populate_match_window(window, song_container, tracks))
    swipe_right_btn = Button(button_frame, image=swipe_right_img, borderwidth=0, command= lambda: populate_match_window(window, song_container, tracks))
    super_like_btn = Button(button_frame, image=super_like_img, borderwidth=0, command= lambda: populate_match_window(window, song_container, tracks))

    swipe_left_btn.grid(row= 0, column=0)
    super_like_btn.grid(row= 0, column=1)
    swipe_right_btn.grid(row= 0, column=2)

    window.mainloop()

    return window, song_container


def main():
    tracks = get_saved_tracks() 
    window, song_container = create_match_window(tracks)

if __name__ == '__main__':
    main()
