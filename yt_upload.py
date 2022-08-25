import reddit_scraper
import video_creator
import upload_video


topic = 'confessions'

print('Getting top reddit post data ............. \n')

p_title , p_body = reddit_scraper.get_text(topic)

print("Done...... \n")
print('############################################## \n')
print(p_title)
print('############################################## \n')

print(p_body)

print('############################################## \n')

print("Converting text to speech............ \n")

video_creator.text_to_speech(p_body)

print("Done...........\n")

    # Taking the input for the paths of the variables mentioned below.
    #folder_path = input("Enter the Path of the Folder containing Images: ")
folder_path = "/Users/neerajsingh/Documents/projects/youtube_automation/image"
    #audio_path = input("Enter the Path of the MP3 file: ")
audio_path = "/Users/neerajsingh/Documents/projects/youtube_automation/audio/test.mp3"
   # video_path_name = input("Enter the Path followed by name of the Video to be created: ")

video_path_name = "/Users/neerajsingh/Documents/projects/youtube_automation/created_video/test.mp4"

video_creator.text_to_video(folder_path, audio_path, video_path_name)


video_data = {
        "file":"/Users/neerajsingh/Documents/projects/youtube_automation/created_video/test.mp4",
        "title":"Dankest memes and comments!",
        "description": "#shorts \n Giving you the hottest memes of the day with funny comments!",
        "keywords":"meme,reddit",
        "category":"28",
        "privacyStatus":"private"
    }

upload_video.upload_video(video_data)
