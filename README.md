<!-- Title -->
# Sunflower Bee!
## A web application housing an image detection engine.

<!-- Intro -->
### Have you ever wondered if your picture had a sunflower in it? Well, look no further! This web application can tell you!

### Sunflower Bee is a flask-based web application that accepts pictures and then detects whether that picture had a sunflower in it or not. It then shows the picture and the result of the detection to the user.

<!-- Video -->
Video walkthrough of the project coming soon!

<!-- Installation Instructions -->
0. Make sure to have `pip` (and optionally, `git`) correctly downloaded and up-to-date.
1. Download the zip file from the user interface at https://github.com/forrestgoryl/sunflower-bee, 
or run `git clone 'https://github.com/forrestgoryl/sunflower-bee.git'` to clone into this repository.

2. Run `cd sunflower-bee` to move to the project folder and then create a virtual environment using the command `python -m venv myenv`
You may replace `myenv` with an appropriate name, such as sunflower_bee_env-py3.9.

3. Start virtual environment using `source myenv/Scripts/activate` if in [Git Bash](https://www.geeksforgeeks.org/working-on-git-bash/). Otherwise, search online how to start virtual environment using your command terminal.

4. Download dependencies to your new virtualenv using the command `pip install -r requirements.txt`.

5. Download the neural network from this link:
https://www.dropbox.com/s/9edx6bjnqaz0x4p/sunflower_bee_mind.h5?dl=0

6. Move the neural network file to the sunflower-bee project folder. Make sure it is on the same file-level as `app.py`.

7. Run the command `python app.py` to start a locally hosted web server.

<!-- Contributor Expectations -->
Please email me with any ideas for contribution at forrestgoryl@outlook.com, or questions of any sort.

<!-- Known Issues -->
The network evaluates correctly around 90% of the time. It will return false positives on most yellow flowers, for example. This project was meant to be a practice project of mine to learn about the basics of neural networks, and as such isn't a commercially-viable product.

<!-- Contact Me -->
Please contact me at forrestgoryl@outlook.com. I would love to hear from you!

# Thank you for your time and interest in my project!
