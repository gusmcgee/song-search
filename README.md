# song-search

A system that identifies which song is playing from a short recorded audio snippet captured from a speaker. It uses an audio fingerprinting technique similar to Shazam, generating robust frequency–time hashes to match noisy real-world recordings against a set of known songs.

### Project Setup
In the project root, run the following commands:
```bash
mkdir song-files          # stores pre-recorded reference songs of type .wav
mkdir live-song-snippets  # stores short recorded clips to be matched of type .wav

python -m pip install -r requirements.txt # Install requirements
```

### Usage
In the project root, run the following command:
```bash
python src/main.py
```