import datetime
def attachment_path(instance, filename):
    """
    Provide a file path that will help prevent files being overwritten, by
    putting attachments in a folder off attachments for id.
    """
    import os
    from django.conf import settings
    os.umask(0)
    path = 'rdoc/attachments/%s_%s' % (datetime.date.today().month, datetime.date.today().year,)
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(att_path):
        os.makedirs(att_path, 0777)
    return os.path.join(path, filename)