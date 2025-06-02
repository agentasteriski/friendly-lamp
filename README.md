# friendly-lamp
random script collection. lamps probably not related. unless i need something for my smart outlets idk


## merge_cleaner.py
- for diffsinger setup wrangling. removes unwanted languages from merged.yaml(an unofficial subconfig with only merged_phoneme_groups for loading into difftrainer and stuff)
- requirements: pyyaml
- to use: edit the file to have the right input name/filepath(default: merged.yaml in the same folder as the script), desired output name/filepath(default: merge_updated.yaml), and the language prefixes you want to remove, then run script

## dict_grabber.py
- for diffsinger setup wrangling. reads all phonemes in transcriptions.csv and writes them in unique_phonemes.txt. does NOT make correctly formatted dictionaries. it's just for checking what phonemes are in a given speaker.
- requirements: pandas
- to use: put it next to transcriptions.csv and run
