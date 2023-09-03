import os

# Specify the directory containing the image files
directory_path = r'your/file/path'

# Specify the new extension (in lowercase) you want to use
new_extension = 'jpg'

# Initialize a counter for naming the files
counter = 1

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file has one of the specified extensions
    if filename.lower().endswith(('.jpeg', '.png', '.jpg', '.gif')):
        # Build the new file name
        new_filename = f'pic {counter}.{new_extension}'

        # Build the old and new file paths
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)

        # Rename the file to the new name and extension
        os.rename(old_file_path, new_file_path)

        # Increment the counter
        counter += 1

print("File names and extensions changed successfully.")