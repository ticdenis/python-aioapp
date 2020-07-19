from asyncio import AbstractEventLoop, get_event_loop
from types import TracebackType
from typing import Optional, TypeVar, Generic, Type

IContainer = TypeVar('IContainer')
IRunner = TypeVar('IRunner')


class Application(Generic[IContainer, IRunner]):
    _container: Optional[IContainer]
    _runner: Optional[IRunner]

    def __init__(
            self,
            container: Optional[IContainer] = None,
            runner: Optional[IRunner] = None,
    ) -> None:
        self._container = container
        self._runner = runner

    @property
    def container(self) -> Optional[IContainer]:
        return self._container

    @property
    def runner(self) -> Optional[IRunner]:
        return self._runner

    def __enter__(self) -> IRunner:
        pass

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        pass

    def __call__(self) -> None:
        pass


class AsyncApplication(Application[IContainer, IRunner]):
    _loop: AbstractEventLoop

    def __init__(
            self,
            loop: Optional[AbstractEventLoop] = None,
            container: Optional[IContainer] = None,
            runner: Optional[IRunner] = None,
    ) -> None:
        super().__init__(container, runner)
        self._loop = loop or get_event_loop()

    @property
    def loop(self) -> AbstractEventLoop:
        return self._loop

    async def __aenter__(self) -> IRunner:
        pass

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        pass
