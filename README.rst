Python Project Bootstrap (PPB)
==============================

Bootstrap your Python project, let PPB adds its install scripts and plugin in your project.

This is *not* a build system such as ``scons``. The intend of PPB is to solve the bootstrapping of
your project:

- your user may have different systems, different settings, but they want your software
- you do not want to mess with pip or easy_egg files.
- you already have created several project with several installation script (some bash, some
  python,...). Now they are heterogenous and hardly maintainable.
- each time you create a Python project you keep copying the same setup.py file, until you find
  better one.

Python Project Bootstrap will do the following:

- create a single entry point for the installation, compilation, deployment of your Python project.
- allow you to jump directly what really matters: code
- ease your life with deployment, test. A default behavior is provided.

Instensively Plugin
-------------------

PPB is easily extendable with new plugins. So you can easilly customize the folder organization you
want, naming convention,...

Your bootstrapped project will no new dependencies
--------------------------------------------------

Once a project is bootstrapped with PPB, there will be *NO* new dependency on any non standard
libraries, except what are really needed. Said otherwize, the installation script is self contained
within your project.

Easily updatable
----------------

You have bootstrapped a project long time ago. Since then, PPB has evolved. Just execute the
following command to update your installation script::

    ppb update


Multiple OS support
-------------------

Of course, Linux is supported. Mac OS X as well. But your application will also have an installer
on Windows. The only dependencies that are needed on Windows are Python and Virtual env. Just
have a version of Python installed on your system and build script can run.


Command line tool
=================

You can install the command line tool directly through pip:

    pip install ppb

This will install the ppb command line tool that can help you installing, configuring and
modifying the bootstrap files of your project.
