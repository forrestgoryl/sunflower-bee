from flask import Flask, request, render_template, redirect, session, url_for
from flask_session import Session
from PIL import Image
from secret_key import secret_key
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from io import BytesIO
from base64 import b64encode
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['DEBUG'] = False
Session(app)

@app.route('/')
def render_homepage():
    
    # Set up session to hold detected images
    if 'seen_images' not in session:
        session['seen_images'] = []
    
    # Render homepage
    return render_template('homepage.html', seen_images=session['seen_images'])

@app.route('/detect-sunflower', methods=['POST'])
def detect_sunflower():

    try:

        # Get image data from request
        img_data = request.files['drop-zone__input']

        # Load image into a PIL Image object
        img = Image.open(img_data)

        # Preprocess the image
        img = img.resize((300, 300))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Load neural network
        nn = load_model('sunflower_bee_mind.h5')

        # Use the neural network to classify the image
        prediction = nn.predict(img_array)[0][0]

        # Record prediction in string form
        if prediction >= 0.5:
            result = 'is_sunflower'
        else:
            result = 'not_sunflower'

        # Make temporary bytes file
        temp_img_file = BytesIO()

        # Save file to temporary file
        img.save(temp_img_file, format='JPEG')

        # Retrieve bytes
        img_bytes = temp_img_file.getvalue()

        # Encode img into base64 string
        encoded_data = b64encode(img_bytes)

        # Change encoded_data to string data type
        encoded_data = str(encoded_data, encoding='utf-8')

        # Save img_data and result to session
        img_data_and_result = {
            'img_data': encoded_data,
            'result': result
        }
        session['seen_images'].insert(0, img_data_and_result)

    except Exception:
        
        pass

    finally:

        return redirect('/')

@app.route('/delete-session', methods=['POST'])
def delete_session():
    session.pop('seen_images', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()