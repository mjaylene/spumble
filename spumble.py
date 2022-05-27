from matchmaker import MatchMaker, User
import spotipy
import spotipy.util as util
import webbrowser


def main():
    username = input("Enter first person's username: ")
    user1 = User(username)
    username = input("Enter second person's username: ")
    user2 = User(username)
    matchmaker = MatchMaker(user1, user2)
    matchmaker.matchmake()



if __name__ == '__main__':
    main()