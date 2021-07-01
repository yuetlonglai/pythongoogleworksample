"""A video player class."""
import random
from .video_library import VideoLibrary
from .video import Video
#import numpy as np


#currentvid='N/A'

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isplaying=False
        self.paused=False
        self.vidplaying='N/A'

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        sorted_videos=sorted(all_videos, key=lambda x:x.video_id)
        print("Here's a list of all available videos:")
        for i in sorted_videos:
            print(str(i.title) + " (" + str(i.video_id)+ ") " + " [" + " ".join(i.tags) + "] ")
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_videos = self._video_library.get_all_videos()
        sorted_videos=sorted(all_videos, key=lambda x:x.video_id)
        failscore=0


        for j in sorted_videos:
            if video_id == j.video_id:
                print("Stopping Video: " +str(self.vidplaying))
                print("Playing Video: " +str(j.title))
                self.vidplaying=str(j.title)
                self.isplaying=True
                self.pause=False
            else:  
                continue
        

        for k in sorted_videos:
            if video_id!= k.video_id:
                failscore+=1
            else:
                continue
        if failscore==len(all_videos):
                print("Cannot play video: Video doesn't exist")
        



    def stop_video(self):
        """Stops the current video."""
        all_videos = self._video_library.get_all_videos()
        sorted_videos=sorted(all_videos, key=lambda x:x.video_id)
        if self.isplaying==True:
            print("Stopping Video: "+str(self.vidplaying))
        else:
            print("Cannot stop playing: no video is currently playing")


        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        sorted_videos=sorted(all_videos, key=lambda x:x.video_id)
        dice=random.randint(0,len(sorted_videos))
        if self.isplaying==True:
            print("Stopping Video: " +str(self.vidplaying))
            print("Playing video: " +str(sorted_videos[dice][0]))
            self.vidplaying=str(sorted_videos[dice][0])
            self.isplaying=True
        else:
            print("Playing video: " +str(sorted_videos[dice][0]))
            self.vidplaying=str(sorted_videos[dice][0])
            self.isplaying=True

        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.paused==False:
            print("Pausing video: "+str(self.vidplaying))
            self.pasued=True
        elif self.isplaying==False:
            print("Cannot pause video: No video is currently playing")
        elif self.paused==True:
            print("Video already paused: "+str(self.vidplaying))

        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        


        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
