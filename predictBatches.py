import os
import csv
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas as pd

# Define the image dimensions expected by the model
image_width, image_height = 224, 224

# Define the labels
labels = ['Architecture', 'Art and Culture', 'Food and Drinks', 'Travel and Adventure']

# Load the trained model
model = tf.keras.models.load_model('image_classifier.h5')  

# Define the image directory path
image_dir = 'test-case-1-dataset/test/test/classify'  

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Create a list to store the results
results = []

# Process each image file
for image_file in image_files:
    # Open and preprocess the image
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path).convert("RGB")
    image = image.resize((image_width, image_height))
    image = np.expand_dims(image, axis=0)  # Add a batch dimension

    # Perform the prediction
    prediction = model.predict(image)[0]
    predicted_class = np.argmax(prediction)
    predicted_label = labels[predicted_class]

    # Store the result
    results.append((image_file, predicted_label))

# Create a pandas DataFrame from the results
df = pd.DataFrame(results, columns=['Image File', 'Predicted Category'])

# Save the DataFrame to a CSV file
output_csv = 'BatchPredictResult.csv'  # Specify the path and filename for the output CSV file
df.to_csv(output_csv, index=False)

print(f"Classification results saved to {output_csv}")
print(df)