# Don't Use This Code!

## Resources

- [Objectionable Content (Python Object Model) || James Powell](https://www.youtube.com/watch?v=AmHE0kZhLIQ)

## Use This Code!

- Typing
  - [dataclass](https://docs.python.org/3.7/library/dataclasses.html)
  - [pydatinc](https://pydantic-docs.helpmanual.io/)
- Printing
  - [Wasabi](https://github.com/ines/wasabi)
- CLIs
  - [Typer](https://github.com/tiangolo/typer)
- APIs
  - [FastAPI](https://fastapi.tiangolo.com/)
- Labeled Arrays
  - [xarray](https://github.com/pydata/xarray)
- Builtins
  - [walrus](https://www.python.org/dev/peps/pep-0572/)

## Services

- Backend
  - [Deta](https://www.deta.sh/)
  - [Firebase](https://firebase.google.com/)

## Extra

### Inputs and Outputs on IPython/Jupyter

IPython kernels will keep all inputs and outputs on memory

- Inputs are kept as a list of strings
- Outputs are kept as a dictionary

If you have printed a variable it will be saved on the `Out` dictionary, deleting the variable will not delete the output entry.
To do so you need to delete using `%xdel variable` or `%reset out` to reset the dictionary.
