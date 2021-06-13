from django.urls import path, include, reverse

this_urlpatterns = []


def to_path(url_path, name, model_abs_url=False):
    def decor_to_path(cls):
        p = path(url_path, cls.as_view(), name=name)
        this_urlpatterns.append(p)

        if model_abs_url:
            def get_absolute_url(self):
                return reverse(name, args=[str(self.id)])

            cls.model.get_absolute_url = get_absolute_url

        return cls

    return decor_to_path


class Pathing:
    """docstring for Pathing"""
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        prams = cls.to_path
        p = path(prams[0], cls.as_view(), name=prams[1])
        this_urlpatterns.append(p)


def as_path(p=''):
    return path(p, include(this_urlpatterns))