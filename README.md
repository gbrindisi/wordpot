# Wordpot

Wordpot is a Wordpress honeypot which detects probes for plugins, themes, timthumb and other common files used to fingerprint a wordpress installation.
   
    $ python wordpot.py --help
    Usage: wordpot.py [options]
    
    Options:
      -h, --help        show this help message and exit
      --host=HOST       Host address
      --port=PORT       Port address
      --title=TITLE     Blog Title
      --theme=THEME     Default theme name
      --plugins=PLUGINS Fake installed plugins
      --themes=THEMES   Fake installed plugins
      --ver=VERSION     Wordpress version

To configure the honeypot you can edit the config file `wordpot.conf` or provide arguments trough the command line interface as shown above.

## Theme support

You can use a wordpress theme as you would in a normal Wordpress installation by putting the theme folder in the `static/wp-content/themes/` directory. You might also need to edit the html skeleton which is stored in the `templates/` folder and should be named as your theme (e.g. `themename.html`) - take a look at `twentyeleven.html` to see how it works. 

To use the theme start wordpot with the theme option (default value is `twentyeleven`):
    
    $ python wordpot --theme=THEMENAME

Templates are built with the [Jinja2](http://jinja.pocoo.org) template engine.

## Expandable with plugins (*beta*)

Wordpot can be expanded with plugins to improve its behaviour or just expand some functionalities.

For example you can write a plugin to mimick a particular vulnerability in a Wordpress plugin or theme.

Learn more in the dedicated [wiki page](https://github.com/gbrindisi/wordpot/wiki/Plugins).

## Links

* Project Homepage: http://brindi.si/g/projects/wordpot.html

## License

ISC License.
 
> Copyright (c) 2012, Gianluca Brindisi < g@brindi.si >
>
> Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.
>
> THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
