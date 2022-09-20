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
