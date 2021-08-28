import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print("执行此进程", self._args)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    p = MyProcess(args=("xxx",))
    p.start()
    print("继续执行")
