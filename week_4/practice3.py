from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi().list('UERhvV9AGnI')
caption_list = list()
for i in transcript_list:
    caption_list.append(i.fetch())
print(caption_list[0][0:10])

text_list = list()
for i in caption_list[0]:
    text_list.append(i.text)
print(text_list)

with open('video_text.txt', 'w') as f:
    f.writelines(text_list)