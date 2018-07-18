# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from io import BytesIO
import qrcode
import qrcode.image.svg
from PIL import Image
from django.http import HttpResponse


class Image:
    @classmethod
    def image_buffer(cls,
                 str_data: str = None,
                 type: str = 'png',
                 version: int = 1,
                 box_size: int = 10,
                 border: int = 2,
                 fill_color: str = 'black',
                 back_color: str = 'white',
                 fit=True,
                 error_type: str = 'l',
                 method: str = 'basic'):

        switcher = {
            'l': qrcode.constants.ERROR_CORRECT_L,
            'm': qrcode.constants.ERROR_CORRECT_M,
            'q': qrcode.constants.ERROR_CORRECT_Q,
            'h': qrcode.constants.ERROR_CORRECT_H
        }

        content_type = {
            'png': 'image/png',
            'svg': 'image/svg+xml',
            'jpg': 'image/jpg',
        }

        qr = qrcode.QRCode(
            version=version,
            error_correction=switcher.get(error_type, lambda: qrcode.constants.ERROR_CORRECT_L),
            box_size=box_size,
            border=border,
        )

        qr.add_data(str_data)

        if type == 'svg' and method == 'basic':
            # Simple factory, just a set of rects.
            factory = qrcode.image.svg.SvgImage
        elif type == 'svg' and method == 'fragment':
            # Fragment factory (also just a set of rects)
            factory = qrcode.image.svg.SvgFragmentImage
        elif type == 'svg' and method == 'path':
            # Combined path factory, fixes white space that may occur when zooming
            factory = qrcode.image.svg.SvgPathImage

        if type == 'svg':
            qr.image_factory = factory

        qr.make(fit=fit)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()
        response = HttpResponse(image_stream, content_type=content_type.get(type, lambda: 'png'))

        return response
