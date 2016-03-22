Cmustify
========

What is cmustify? This is a [cmus](https://cmus.github.io/) notifier that shows the current song into notifications using notify2.

### Why?
I would like to improve the current solutions. Also, it's always nice to do
things by ourselves.

### todo
* Finish the usage info
* Better support for internet radios stream
* Fetch albums image from google (useful for internet radios)

Requirements
------------
* [notify2](https://pypi.python.org/pypi/notify2/)

Install
-------
1. Clone the repository into the `.cmus` folder in your home directory.
  ```
  git clone https://github.com/kimond/cmustify.git ~/.cmus/
  ```
2. Make `cmustity.py` and `status_display_program.sh` executable.
  ```
  chmod +x cmustity.py status_display_program.sh
  ```
3. Set the `status_display_program` variable in `cmus`.
  ```
  :set status_display_program=/home/user/.cmus/cmustify/status_display_program.sh
  ```
4. Save configs in `cmus`. This is important to avoid having set the variable every times you start `cmus`.
  ```
  :save
  ```

Usage
-----
`cmus` will send notifications by itself.

Contributions
-------------
Contributions are welcome.

Credits
-------
* Travis Poppe for https://github.com/cmus/cmus/wiki/status_diplay_notify_send.py
  * A working script on which I based my code.
* Thomas Kluyver for [notify2](https://pypi.python.org/pypi/notify2/)
  * An API to ease the interaction with notification daemons
