import shutil
import tempfile


class TemporaryDirectory(object):
    """
    Context manager for tempfile.mkdtemp().

    This class is available in python +v3.2.

    """
    def __enter__(self):
        self.dir_name = tempfile.mkdtemp()
        return self.dir_name

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            shutil.rmtree(self.dir_name)
        except:
            pass
