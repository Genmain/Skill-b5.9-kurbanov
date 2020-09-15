from timeit import default_timer


class Timer(object):
    # инициализируем класс. по умолчанию количество запусков = 5
    def __init__(self, verbose=False, num_runs = 5):
        self.num_runs = num_runs
        self.verbose = verbose
        self.timer = default_timer
        
    # Создание метода вызова. Передается название функции в обертку
    def __call__(self, func):            
        # Передача параметров функции в обертку
        def wrap(param):
            # среднее время выполнения функции. в начале вычислений обнуляем
            avg_time = 0
            # выполняем заданное количество итераций
            for i in range(self.num_runs):
                # засекли время старта
                self.start = self.timer()
                # выполняем переданную функцию
                func(param)
                # засекаем время окончания
                self.end = self.timer()
                # вычисляем вычисляем время выполнения
                avg_time += (self.end - self.start)
            # вычисляем среднее вермя выполнения
            avg_time /= self.num_runs
            print('Elapsed time %f ms' % (avg_time * 1000))
        return wrap
        


    def __enter__(self):
        self.start = self.timer()
        return self
        
    def __exit__(self, *args):
        end = self.timer()
        elapsed_secs = end - self.start
        elapsed = elapsed_secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % elapsed)        

timer_5 = Timer(num_runs=1)

@timer_5
def fibo(max):
    el = [1,2]
    i = 1
    while el[i]< max:
        el.append(el[i]+el[i-1])
        i += 1
    print (el[-2])

if __name__ == '__main__':    
    fibo(4000000)

    with Timer(verbose=True):
        print("123")