from flask import Flask, request, render_template, redirect, session, url_for
from flask_session import Session
from PIL import Image
from secret_key import secret_key
from werkzeug.utils import secure_filename
from keras.saving import load_model
from io import BytesIO
from base64 import b64encode
import numpy as np
import os

# Prepare application
APP = Flask(__name__)
APP.config['SECRET_KEY'] = secret_key
APP.config['SESSION_TYPE'] = 'filesystem'
APP.config['SESSION_PERMANENT'] = False
APP.config['DEBUG'] = False
Session(APP)

# Load neural network
NEURAL_NETWORK = load_model('sunflower_bee_mind.h5')

# Define PORT as environment variable given by server, or PORT = 5000
PORT = int(os.environ.get('PORT', 5000))


@APP.route('/')
def render_homepage():
    
    # Set up session to hold detected images
    if 'seen_images' not in session:
        session['seen_images'] = []
    
    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)
    
    # Render homepage
    return render_template('homepage.html', seen_images=session['seen_images'])


@APP.route('/detect-sunflower', methods=['POST'])
def detect_sunflower():

    # Limit session data to 3 images to save memory
    if session.get('seen_images') != None:
        if len(session['seen_images']) >= 3:
            session['seen_images'].pop()

    # Get image data from request
    img_data = request.files['drop-zone__input']

    # Load image into a PIL Image object
    img = Image.open(img_data)

    # Preprocess the image
    img = img.resize((300, 300))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Use the neural network to classify the image
    prediction = NEURAL_NETWORK.predict(img_array)[0][0]

    # Record prediction in string form
    if prediction >= 0.8:
        result = 'is_sunflower'
    else:
        result = 'not_sunflower'

    # Make temporary bytes file
    temp_img_file = BytesIO()

    # Save file to temporary file
    img.save(temp_img_file, format='JPEG')

    # Retrieve bytes
    img_bytes = temp_img_file.getvalue()

    # Close temporary bytes file to prevent memory leak
    temp_img_file.close()

    # Encode img into base64 string
    encoded_data = b64encode(img_bytes)

    # Change encoded_data to string data type
    encoded_data = str(encoded_data, encoding='utf-8')

    # Save img_data and result
    img_data_and_result = {
        'img_data': encoded_data,
        'result': result
    }

    # Send img_data_and_result to session at index 0
    session['seen_images'].insert(0, img_data_and_result)

    # Reload homepage
    return redirect('/')

@APP.route('/delete-session', methods=['POST'])
def delete_session():
    session.pop('seen_images', None)
    return redirect('/')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=PORT)
