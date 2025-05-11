def validate_arguments(funct):
    def wrapper(**args, **kwargs):
        for arg in args:
            if arg < 0:
                print



        return wrapper
