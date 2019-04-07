### Autochess MMR Simulator
A python script to simulate the MMR change in Auto Chess for different lobbies. 

### Setup
* Install `python3`, `pip` and `virtualenv`
* `virtualenv -p python3 venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

### Running the script
* Make changes to `input.txt`
  * Each line represents a different lobby
  * Each line should have eight (8) values for MMR
  * Example `input.txt` provided
* Run `python main.py`

The graphs corresponding to each lobby should be opened in the browser and saved to `graphs/`
