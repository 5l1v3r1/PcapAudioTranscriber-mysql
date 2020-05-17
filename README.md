# PcapAudioTranscriber-mysql
A tool to check PCAP's for audio, transcribe the audio and upload the transcription to a mysql database

## PLEASE NOTE its not 100% Right now as I am still working on it

## Requirments
  - pip install speech_recognition
  - pip install pyshark
  - pip install pydub
  - pip install mysql
  
# Usage
Everything is controled from the menu, you will need to modify the Database informaiton before usage "Check the code". it will output a raw audio file in the same folder based on the name you give it and will then transcribe that audio to a mysql database
