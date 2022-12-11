# voice-memo-transcription
 A quickly hacked up script to transcribe Apple Voice Memos using [OpenAI's Whisper](https://github.com/openai/whisper). I don't plan to support or substantially improve this.

Usage:
```shell
python transcribe.py
```

The script performs the following steps:
- Tries to detect the current username
- Looks at the default path for Apple Voice Memos
- Loads up Whisper's medium English model
- Transcribes all the voice memos in the Voice Memo folder
- Outputs each transcription to a separate file, along with a master transcription file containing all transcriptions

Prerequisites:
- [Whisper](https://github.com/openai/whisper)
- Python 3
- Apple Voice Memos synced to your Mac