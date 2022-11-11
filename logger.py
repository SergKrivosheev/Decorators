from datetime import datetime
from pathlib import Path
import os

def logger(path='/', log_name='logger.log'):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            log = ''
            log += f'{datetime.now()}\n'
            log += f'Function {old_function.__name__} was called\n'
            log += f'With args: {args} \n     kwargs: {kwargs}\n'
            res = old_function(*args, **kwargs)
            log += f'Was returned: {res}\n'
            log += '\n'
            Path(path).mkdir(parents=True, exist_ok=True)
            with open(os.path.join(path, log_name), 'a+', encoding="utf8") as f:
                f.write(log)
            return res

        return new_function

    return decorator


if __name__ == '__main__':
    @logger(path='logs', log_name='test.txt')
    def test_func(x1, x2=0, x3=2):
        return x1 + x2 * x3


    test_func(x1=2, x2=5)