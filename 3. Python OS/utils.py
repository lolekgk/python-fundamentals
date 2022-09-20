import inspect


def check_path(func):
    def wrapper(self, *args, **kwargs):

        bound_args = inspect.signature(func).bind(self, *args, **kwargs)
        bound_args.apply_defaults()
        func_args = dict(bound_args.arguments)
        if func_args['path'] is None:
            func_args['path'] = self.path
            return func(*func_args.values())
        return func(*func_args.values())

    return wrapper


class PathError(Exception):
    def __init__(
        self,
        msg='You need to provide valid directory path to perform this action.',
        *args,
        **kwargs,
    ):
        super().__init__(msg, *args, **kwargs)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
