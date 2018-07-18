from django_qr_code.core import Image


def image_with_vars(request, param_data=1, extension='png'):
    return Image.get_image(
        str_data='http://my-site.com/{param_data}'.format(param_data=param_data),
        box_size=40,
        content_type=extension)

