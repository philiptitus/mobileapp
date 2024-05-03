from django.db import models
import qrcode
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    qr_code = models.ImageField(blank=True, upload_to='qrcodes/')
    date = models.DateField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.qr_code:
            # Create QR code
            qr_img = qrcode.make(self.name)
            
            # Create canvas for QR code image
            canvas = Image.new('RGB', qr_img.size, 'white')
            canvas.paste(qr_img)
            
            # Save QR code image
            fname = f'qr_code-{self.name}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, ContentFile(buffer.getvalue()), save=False)
        
        super().save(*args, **kwargs)
