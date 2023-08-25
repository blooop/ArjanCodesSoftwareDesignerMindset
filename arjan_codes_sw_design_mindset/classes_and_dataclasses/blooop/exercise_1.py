from dataclasses import dataclass,field

@dataclass
class A:
    _length:int = field(init=False,default=0)

@dataclass
class B:
    x:int
    y:str="hello"
    lst:list = field(default_factory=list)


@dataclass
class C:
    a:int=3
    b:int = field(init=False)

    def __post_init__(self) -> None:
        self.b = self.a+3
