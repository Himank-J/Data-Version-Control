import os
import random
import shutil

def balance_dataset(data_dir, target_count=500):
    # Define paths for cat and dog directories
    cat_dir = os.path.join(data_dir, 'Cat')
    dog_dir = os.path.join(data_dir, 'Dog')

    # Function to keep only target_count images in a directory
    def limit_images(directory, count):
        images = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if len(images) > count:
            to_remove = random.sample(images, len(images) - count)
            for img in to_remove:
                os.remove(os.path.join(directory, img))
            print(f"Removed {len(to_remove)} images from {directory}")
        else:
            print(f"No images removed from {directory}. Current count: {len(images)}")

    # Balance cat images
    limit_images(cat_dir, target_count)

    # Balance dog images
    limit_images(dog_dir, target_count)

    print("Dataset balancing complete.")

if __name__ == "__main__":
    data_directory = "data/catdog"  # Replace with your actual data directory path
    balance_dataset(data_directory)