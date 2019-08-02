
from abc import ABC, abstractmethod


class Command(ABC):
    """抽象命令基类
    Usage(demo):
        main = SomeCommand()
        main.config = config
        main.run()

    Design:
        构造 PITL，配置 property，控制

    Attributes:
        config: [description]
    """

    def set_config(self, config):
        self.__dict__.update(config.__dict__)

    config = property(fset=set_config)

    @abstractmethod
    def run(self):
        pass
