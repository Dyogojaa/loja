from PIL import Image
import os
from django.conf import settings
 
 
 # Metodo Estático que efetua o redimensionamento de Imagem para o máximo de largura de 800 Pixels        
@staticmethod
def resize_image(img, new_width=800):
    img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
    img_pil = Image.open(img_full_path)
    original_width, original_height =  img_pil.size
    
    new_height = round((new_width * original_height) / original_width )
    
    if original_width <= new_width:            
        img_pil.close()
        return
    
    
    new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
    new_img.save(
        img_full_path,
        optimize=True,
        quality=50
    )        