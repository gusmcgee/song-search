# song-search

A system that identifies which song is playing from a short recorded audio snippet captured from a speaker. It uses an audio fingerprinting technique similar to Shazam, generating robust frequency–time hashes to match noisy real-world recordings against a set of known songs.

### Project Setup
In the project root, run the following commands:
```bash
mkdir song-files live-song-snippets
python -m pip install -r requirements.txt
```
```song-files``` stores pre-recorded reference songs and ```live-song-snippets``` stores short recorded clips to be matched to songs in ```song-files```. These audio files should use the .wav file type.


### Usage
In the project root, run the following command:
```bash
python src/main.py
```

For each audio snippet in ```live-song-snippets```, the program outputs the snippet’s name and its five closest matches in ```song-files```, ranked in descending order. Each match is accompanied by the number of matching hashes between the snippet and the corresponding audio file.