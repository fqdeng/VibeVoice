# import warnings
# try:
#     import urllib3.exceptions
#     warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)
# except (ImportError, AttributeError):
#     pass

from gradio_client import Client

client = Client("https://vibe-voice.jonwinters.pw/")
result = client.predict(
    api_name="/clear_audio_outputs"
)
print(result)
client = Client("https://vibe-voice.jonwinters.pw/")
result = client.predict(
    num_speakers=2,
    script="Hello!!",
    param_2="zh-Bowen_man",
    param_3="zh-Xinran_woman",
    param_4="en-Frank_man",
    param_5="en-Maya_woman",
    param_6=1.3,
    api_name="/generate_podcast_wrapper"
)
print(result)