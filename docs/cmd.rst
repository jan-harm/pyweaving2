Command Line Usage
==================

PyWeaving includes a command-line utility that can be used for basic tasks.
Here are some examples. You can also see the utility itself for more info::

    $ pyweaving -h


Draft Rendering
---------------

Render a draft from a WIF file::

    $ pyweaving2 render example.wif

Or from a JSON file::

    $ pyweaving2 render example.json

Render a draft to an image::

    $ pyweaving2 render example.wif out.png

Render a draft to an SVG (vector) file::

    $ pyweaving2 render example.wif out.svg

Instead of treadling, convert to a liftplan::

    $ pyweaving2 render example.wif out.png --liftplan


File Conversion
---------------

Convert between WIF and JSON::

    $ pyweaving2 convert example.wif example.json


Instructions
------------

These instructions are interactive, and intend to walk you step-by-step through
various processes, providing useful statistics and progress saving along the
way.

Show instructions for threading a draft::

    $ pyweaving2 thread example.wif

Show instructions for weaving::

    $ pyweaving2 weave example.wif --liftplan --repeats 50
