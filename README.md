# Wordpot

Wordpot is a Wordpress honeypot which detects probes for plugins, themes, timthumb and other common files useful to fingerprint a wordpress installation.

   $ python wordpot.py --help
   Usage: wordpot.py [options]
   
   Options:
     -h, --help     show this help message and exit
     --host=HOST    Host address
     --port=PORT    Port address
     --title=TITLE  Blog Title
     --ver=VERSION  Wordpress version

You can customize the main template by editing `templates/dummy.html` and the associated images and style sheets in the same directory.

## License

ISC License.
 
    Copyright (c) 2012, Gianluca Brindisi <g@brindi.si>

    Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
