# from faster_whisper import WhisperModel

# model_size = "small"
# model = WhisperModel(model_size, device="cpu", compute_type="int8")
# segments, info = model.transcribe("audio.mp3", beam_size=5)

# print(
#     "Detected language '%s' with probability %f"
#     % (info.language, info.language_probability)
# )

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

from youtube_transcript_api import YouTubeTranscriptApi

transcript_dict = YouTubeTranscriptApi.get_transcript("gIBEnSIM7W4")
transcript_stringified = ""

for t in transcript_dict:
    transcript_stringified += t["text"] + " "

f = open("test_input.txt", "a")
f.write(transcript_stringified)
f.close()
