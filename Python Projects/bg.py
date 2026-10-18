
from rembg import remove, new_session

input_path = "IMG_0925.jpeg"
output_path = "IMG_0925_no_bg.png"

# Use a smaller AI model
session = new_session("u2netp")

with open(input_path, "rb") as input_file:
    input_bytes = input_file.read()

output_bytes = remove(input_bytes, session=session)

with open(output_path, "wb") as output_file:
    output_file.write(output_bytes)

print("Background removed successfully!")
print("Saved as:", output_path)
