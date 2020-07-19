# Async Python application

pyaioapp is a Python library for simple and lightweight application wrapper.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyaioapp.

```bash
pip install pyaioapp
```

## Usage

```python
from asyncio import get_event_loop, AbstractEventLoop
from pyaioapp import AsyncApplication
from aiohttp.web import Application, run_app
from typing import Dict as Container, Any

SETTINGS = {
    'DEBUG': '0', 'DEBUG_HOST': '0.0.0.0', 'DEBUG_PORT': '5678',
    'HTTP_HOST': '0.0.0.0', 'HTTP_PORT': '80'
}


async def get_container(settings: dict, **kwargs) -> Container:
    container = {}
    # ...
    return container


async def get_runner(container: Container) -> Application:
    runner = Application()
    # ...
    return runner


class HttpApp(AsyncApplication[Container, Application]):
    async def __aenter__(self) -> Application:
        self._container = await get_container(SETTINGS, loop=self.loop)
        self._runner = await get_runner(self._container)
        return self._runner

    def __call__(self) -> None:
        run_app(
            app=self.__aenter__(),
            host=str(SETTINGS['HTTP_HOST']),
            port=int(SETTINGS['HTTP_PORT'])
        )


def main(loop: AbstractEventLoop) -> Any:
    if SETTINGS['DEBUG'] == '1':
        from ptvsd import enable_attach  # type: ignore
        enable_attach(
            address=(SETTINGS['DEBUG_HOST'], int(SETTINGS['DEBUG_PORT']))
        )
    return HttpApp(loop).__call__()


if __name__ == '__main__':
    main(get_event_loop())
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/ticdenis/python-aioapp/blob/master/LICENSE)
