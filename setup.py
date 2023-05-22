import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="fun",
    options={"build_exe": {"packages": ["pygame","kivy"]}},
    executables=executables

)
