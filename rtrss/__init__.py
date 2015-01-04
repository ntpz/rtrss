__version__ = '0.3'


class OperationInterruptedException(Exception):
    '''Raised if unrecoverable error occured during any operation'''
    pass

class TException(Exception):
    '''Raised if error occured during topic processing'''
    pass
