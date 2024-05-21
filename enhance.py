import os
from PIL import Image, ImageEnhance

def enhance_image(image_path, output_path):

    with Image.open(image_path) as img:
      
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.2)  

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.3)  

   
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)  


        img.save(output_path)

def enhance_images_in_folder(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            enhance_image(input_path, output_path)
            print(f"Enhanced {filename} and saved to {output_folder}")
        except Exception as e:
            print(f"Failed to enhance {filename}: {e}")

if __name__ == "__main__":
    input_folder = '/input/folder'  # Replace with the path to your input folder
    output_folder = '/output/folder'  # Replace with the path to your output folder
    
    enhance_images_in_folder(input_folder, output_folder)
