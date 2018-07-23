# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import qrcode
import qrcode.image.svg
from io import BytesIO
from PIL import Image
from django.http import HttpResponse
from django.utils.html import mark_safe


class Image:
    def __init__(self):
        self.image_content = None
        self.image_stream = None

    @staticmethod
    def error_correct(error_type: str='l'):
        error_types = {
            'l': qrcode.constants.ERROR_CORRECT_L,
            'm': qrcode.constants.ERROR_CORRECT_M,
            'q': qrcode.constants.ERROR_CORRECT_Q,
            'h': qrcode.constants.ERROR_CORRECT_H
        }

        return error_types.get(error_type, lambda: qrcode.constants.ERROR_CORRECT_L)

    @staticmethod
    def content_type(content_type: str='png'):
        content_types = {
            'png': 'image/png',
            'svg': 'image/svg+xml',
            'jpg': 'image/jpg',
        }

        return content_types.get(content_type, lambda: 'png')

    @classmethod
    def image_factory(cls, image_type: str='svg', method: str='basic'):
        if image_type == 'svg' and method == 'basic':
            # Simple factory, just a set of rects.
            factory = qrcode.image.svg.SvgImage
        elif image_type == 'svg' and method == 'fragment':
            # Fragment factory (also just a set of rects)
            factory = qrcode.image.svg.SvgFragmentImage
        elif image_type == 'svg' and method == 'path':
            # Combined path factory, fixes white space that may occur when zooming
            factory = qrcode.image.svg.SvgPathImage

        return factory

    @classmethod
    def image_create(cls,
                     str_data: str = None,
                     content_type: str = 'png',
                     version: int = 1,
                     box_size: int = 10,
                     border: int = 2,
                     fill_color: str = 'black',
                     back_color: str = 'white',
                     fit=True,
                     error_type: str = 'l',
                     method: str = 'basic',
                     *args,
                     **kwargs):

        qr = qrcode.QRCode(
            version=version,
            error_correction=cls.error_correct(error_type=error_type),
            box_size=box_size,
            border=border,
        )

        if 'cache_enabled' in kwargs:
            qr.pop('cache_enabled')

        qr.add_data(str_data)

        if content_type == 'svg':
            qr.image_factory = cls.image_factory(method=method)

        qr.make(fit=fit)

        return qr.make_image(fill_color=fill_color, back_color=back_color)

    @classmethod
    def image_buffered(cls, *args, **kwargs):
        if 'content_type' not in kwargs:
            kwargs['content_type'] = 'png'

        img = cls.image_create(**kwargs)
        img_buffer = BytesIO()
        img.save(img_buffer)

        image_stream = img_buffer.getvalue()
        content_type = cls.content_type(content_type=kwargs['content_type'])

        return image_stream, content_type

    @classmethod
    def get_image(cls, *args, **kwargs):
        stream, content = cls.image_buffered(**kwargs)
        return HttpResponse(stream, content)

    @classmethod
    def make_html(cls, *args, **kwargs):
        stream, content = cls.image_buffered(**kwargs)
        html_code = '<img src="data:{content};base64,{image}" alt="{alt}">'.format(content=content,image=str(base64.b64encode(stream), encoding='ascii'), alt='')
        #str(base64.b64encode(stream.getvalue()), encoding='ascii'), escape(text))
        return mark_safe(html_code)

