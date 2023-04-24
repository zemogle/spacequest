import glob
import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from PIL import Image, ImageFont, ImageDraw
from pdf2image import convert_from_path

from quest.models import Thing

class Command(BaseCommand):

    help = "Make a QR code image and add it to the poster image for a Thing"

    def add_arguments(self, parser):
        parser.add_argument('--thing', action="store", help='ID or slug of the Thing to process')


    def handle(self, *args, **options):
        usage = "Make a QR code image and add it to the poster image for a Thing"

        if thing := options['thing']:
            if type(thing) == int:
                things = Thing.objects.filter(id=options['thing'])
            elif type(thing) == str:
                things = Thing.objects.filter(slug=options['thing'])
        else:
            things = Thing.objects.all()

        for thing in things:
            url = settings.BASE_URL + thing.slug
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(url)

            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            img = img.resize((1000,1000), Image.Resampling.LANCZOS)

            poster_path = settings.POSTER_DIR + thing.slug + '*.pdf'
            files = glob.glob(poster_path)
            font1 = ImageFont.truetype("/Users/egomez/Library/Fonts/Inconsolata-VariableFont_wdth,wght.ttf", 300)
            font1.set_variation_by_name('Condensed Medium')
            font2 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Futura.ttc", 400)
            if not files:
                print(f"Could not find poster for {thing.slug}")
                continue
            for poster_file in files:
                images = convert_from_path(poster_file)
                path = Path(poster_file)
                poster = images[0]
                back_im = poster.copy()
                x, y = back_im.size
                back_im.paste(img, (50, y-1250))

                draw = ImageDraw.Draw(back_im)
                draw.text((x/2+250, y-600), f"spacequest.uk/{thing.slug}", (255, 255, 255), font=font1)
                if thing.id < 10:
                    draw.text((x-1250, 1250), str(thing.id), (37,36,67), font=font2)
                else:
                    draw.text((x-1350, 1250), str(thing.id), (37,36,67), font=font2)

                save_path = settings.BASE_DIR / "build" / "posters" / path.name
                back_im.save(save_path, quality=95)