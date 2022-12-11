import whisper
import os
import pwd

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def processTranscript(text):
    return f"- {text}\n"

username = get_username()
print("detected username", username)

voiceMemoFolder = f"/Users/{username}/Library/Application Support/com.apple.voicememos/Recordings"
print("reading voice memos from", voiceMemoFolder)

outputFolder = "./transcriptions"
print("loading model")
model = whisper.load_model("medium.en")
print("model loaded")

files = list(filter(lambda x: x.endswith(('.m4a')), sorted(os.listdir(voiceMemoFolder))))
masterTranscription = ""

for index, file in enumerate(files):
    print("processing file", index + 1, "of", len(files))
    inputFile = os.path.join(voiceMemoFolder, file)
    print("next file ", inputFile)

    fileName = os.path.splitext(file)[0];
    outputFile = os.path.join(outputFolder, fileName + '.txt')
    if os.path.isfile(outputFile):
        print("transcription exists, grabbing text")
        textfile = open(outputFile, 'r')
        masterTranscription += processTranscript(textfile.read())
        textfile.close()
        continue

    print("transcribing")
    result = model.transcribe(inputFile, fp16=False, language='English')
    masterTranscription += processTranscript(result["text"])

    print("outputting to", outputFile)
    textfile = open(outputFile, 'w')
    textfile.write(result["text"])
    textfile.close()
    print("file complete")

print("all files complete, outputting master transcription")
masterFile = os.path.join(outputFolder, 'master_transcription.txt')
textfile = open(masterFile, 'w')
textfile.write(masterTranscription)
textfile.close()