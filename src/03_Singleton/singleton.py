class Singleton:
    def __new__(cls):
        if not hasattr(cls, "single_cls"):
            cls.single_cls = super(Singleton, cls).__new__(cls)
        return cls.single_cls


a = Singleton()
