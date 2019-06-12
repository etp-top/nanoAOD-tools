import shutil
import tempfile


class TemporaryDirectory(object):
    """
    Context manager for tempfile.mkdtemp().

    This class is available in python +v3.2.

    """
    def __init__(self):
        self.name = tempfile.mkdtemp()

    def __enter__(self):
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup()
        

    def __repr__(self):
         return "<{} {!r}>".format(self.__class__.__name__, self.name)

    def cleanup(self):
        try:
            shutil.rmtree(self.name)
        except:
            pass

    def __del__(self):
        self.cleanup()
