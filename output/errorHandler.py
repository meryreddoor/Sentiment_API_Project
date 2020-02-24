import traceback


def jsonErrorHandler(fn):
    def wrapper(*args, **kwargs):
        try:
            print("Calling fn")
            return fn(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            return {
                "error": str(e)
            }, 404
    return wrapper