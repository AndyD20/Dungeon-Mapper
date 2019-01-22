import time


def timer(step_name, function_to_evaluate, function_arguments=None):

    start = time.time()

    if function_arguments is not None:
        return_val = function_to_evaluate(*function_arguments)
    else:
        return_val = function_to_evaluate()

    print('{} took: {:.3f} seconds.'.format(step_name, time.time() - start))

    return return_val
