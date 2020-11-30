from .hurz import i_dont_exist

def main():
    result = i_dont_exist()
    return map(lambda x: x.id, result)

def xxx(a):
    if a > 0:
        return 1
    return a * b


class Huey(object):
    def __init__(self, name='huey', results=True, store_none=False, utc=True,
                 immediate=False, serializer=None, compression=False,
                 use_zlib=False, immediate_use_memory=True, always_eager=None,
                 storage_class=None, **storage_kwargs):
        invalid = [p for p in self._deprecated_params
                   if storage_kwargs.pop(p, None) is not None]
        if invalid:
            warnings.warn('the following Huey initialization arguments are no '
                          'longer supported: %s' % ', '.join(invalid),
                          DeprecationWarning)

        self.name = name
        self.results = results
        self.store_none = store_none
        self.utc = utc
        self._immediate = immediate
        self.immediate_use_memory = immediate_use_memory
        if serializer is None:
            serializer = Serializer(compression, use_zlib=use_zlib)
        self.serializer = serializer

        # Initialize storage.
        self.storage_kwargs = storage_kwargs
        self.storage_class = storage_class
        self.storage = self.create_storage()

        self._locks = set()
        self._pre_execute = OrderedDict()
        self._post_execute = OrderedDict()
        self._startup = OrderedDict()
        self._registry = Registry()
        self._signal = S.Signal()

    def create_storage(self):
        # When using immediate mode, the default behavior is to use an
        # in-memory broker rather than a live one like Redis or Sqlite, however
        # this can be overridden by specifying "immediate_use_memory=False"
        # when initializing Huey.
        if self._immediate and self.immediate_use_memory:
            return self.get_immediate_storage()

        return self.get_storage(**self.storage_kwargs)

    def get_immediate_storage(self):
        return MemoryStorage(self.name)
