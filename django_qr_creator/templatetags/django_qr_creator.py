from django import template
from ..render import Image

register = template.Library()


@register.simple_tag
def qr(**kwargs):
    if 'url' in kwargs:
        kwargs['str_data'] = kwargs['url']
        del kwargs['url']
    elif 'tel' in kwargs:
        kwargs['str_data'] = 'tel:{tel}'.format(tel=kwargs['tel'])
        del kwargs['tel']
    elif 'email' in kwargs:
        kwargs['str_data'] = 'mailto:{email}'.format(email=kwargs['email'])
        del kwargs['email']
    elif 'location' in kwargs:
        str_data = kwargs['location']
        str_data.replace(' ', '')
        latlon = [x.strip() for x in str_data.split(',')]
        if 'altitude' in kwargs:
            altitude = kwargs['altitude']
            del kwargs['altitude']
        else:
            altitude = 13

        kwargs['str_data'] = 'geo:{lat},{lon},{alt}'.format(lat=latlon[0], lon=latlon[1], alt=altitude)

        del kwargs['location']
    elif 'sms' in kwargs:
        str_data = kwargs['sms']
        str_data.replace(' ', '')
        str_data.strip()

        #num = [x.strip() for x in str_data.split(',')]
        if 'message' in kwargs:
            msg = kwargs['message']
            del kwargs['message']
        else:
            msg = None

        kwargs['str_data'] = 'SMS:{number}?body={message}'.format(number=str_data, message=msg) if msg else 'SMS:{number}'.format(number=str_data)

        del kwargs['sms']
    else:
        return 'Image not rendered'

    return Image.make_html(**kwargs)
