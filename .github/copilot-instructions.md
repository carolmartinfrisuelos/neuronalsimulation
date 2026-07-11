

# Copilot Instructions for Lessons

-   The package `Lessons` is a Python Project located in the folder `Lessons-folder`.
-   You need to call the `Get Python Environment Information` tool on the `Lessons` path to get the Python executable details.
-   Substitute the Python executable you get from the `Get Python Environment Information` tool anywhere you see `<python>` in these instructions.
    -   Run command for `Lessons`: `<python> -m Lessons`
    -   Command to run tests for `Lessons`: `<python> -m pytest Lessons/tests`
-   To run an editable install for the package `Lessons`, use the `Install Python Package` tool with the `Lessons-folder` path and arguments `['-e', '.']`.
-   In the workspace `launch.json` file, configurations related to this package have the prefix `Lessons`.
-   The package `Lessons` has a defined `pyproject.toml` file that you should use and keep up to date.
