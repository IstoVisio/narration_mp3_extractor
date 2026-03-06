Python script which reads a directory of narrations, extracts the audio files contained within, and generates subtitle json files for each narration.

To use:
1. Clone the repo
2. Run `python -m venv venv`
3. Run `.\venv\Scripts\activate.ps1`
4. Run `pip install -r requirements.txt`
5. Place the narrations in the narrations folder.
6. Run `python narration_mp3_extractor.py`

Note: This json is similar, but not the same as the json used in syGlass Pro
