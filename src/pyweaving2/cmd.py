from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
import argparse

from pyweaving2 import Draft
from pyweaving2 import instructions
from pyweaving2.wif import WIFReader, WIFWriter
from pyweaving2.render import ImageRenderer, SVGRenderer


def load_draft(infile):
    if infile.endswith('.wif'):
        return WIFReader(infile).read()
    elif infile.endswith('.json'):
        with open(infile) as f:
            return Draft.from_json(f.read())
    else:
        raise ValueError(
            "filename %r unrecognized: .wif and .json are supported" %
            infile)


def render(opts):
    draft = load_draft(opts.infile)
    if opts.outfile:
        if opts.outfile.endswith('.svg'):
            SVGRenderer(draft).save(opts.outfile)
        else:
            ImageRenderer(draft).save(opts.outfile)
    else:
        ImageRenderer(draft).show()


def convert(opts):
    draft = load_draft(opts.infile)
    if opts.outfile.endswith('.wif'):
        WIFWriter(draft).write(opts.outfile)
    elif opts.outfile.endswith('.json'):
        with open(opts.outfile, 'w') as f:
            f.write(draft.to_json())


def thread(opts):
    draft = load_draft(opts.infile)
    instructions.threading(draft, opts.repeats)


def weave(opts):
    draft = load_draft(opts.infile)
    assert opts.liftplan, "only liftplan supported for now"
    # todo: update storage of status (overule when file exists?)
    save_filename = '.' + opts.infile + '.save'
    print("SAVE FILENAME is %r" % save_filename)
    instructions.weaving(draft,
                         repeats=opts.repeats,
                         start_repeat=opts.start_repeat,
                         start_pick=opts.start_pick,
                         save_filename=save_filename)


def tieup(opts):
    draft = load_draft(opts.infile)
    instructions.tieup(draft)


def stats(opts):
    draft = load_draft(opts.infile)
    warp_longest, weft_longest = draft.compute_longest_floats()
    print("Title:", draft.title)
    print("Author:", draft.author)
    print("Address:", draft.address)
    print("Email:", draft.email)
    print("Telephone:", draft.telephone)
    print("Fax:", draft.fax)
    print("Notes:", draft.notes)
    print("Date:", draft.date)
    print("***")
    print("Warp Threads:", len(draft.warp))
    print("Weft Threads:", len(draft.weft))
    print("Shafts:", len(draft.shafts))
    print("Treadles:", len(draft.treadles))
    print("Longest Float (Warp):", warp_longest)
    print("Longest Float (Weft):", weft_longest)


def main(argv=sys.argv):
    p = argparse.ArgumentParser(description='Weaving utilities.',
                                epilog='use %(prog)s command -h for more help on the specific command')

    # p.add_argument('infile', nargs=1)
    subparsers = p.add_subparsers(help='command help')


    p_render = subparsers.add_parser('render', help='Render a draft to screen or an image file')
    p_render.add_argument('infile', help=' valid json or wif file')
    p_render.add_argument('outfile', nargs='?', help=' when present image will be saved')
    p_render.add_argument('--liftplan', action='store_true')
    p_render.set_defaults(function=render)

    p_convert = subparsers.add_parser('convert', help='Convert between draft file types.')
    p_convert.add_argument('infile', help='a valid wif or json file')
    p_convert.add_argument('outfile', nargs='?', help='output file with extension wif or json')
    p_convert.add_argument('--liftplan', action='store_true')
    p_convert.set_defaults(function=convert)

    p_thread = subparsers.add_parser('thread',help='Show step by step threading instructions for a draft.')
    p_thread.add_argument('infile', help='a valid wif or json file')
    p_thread.add_argument('--repeats', type=int, default=1,
                          help='repeat number of pattern')
    p_thread.add_argument('--threads', type=bool,
                          help='ruse --repeats for number of threads rather than number of patterns')
    p_thread.set_defaults(function=thread)

    p_weave = subparsers.add_parser(
        'weave',
        help='Show step by step weaving instructions for a draft. Use Cntrl-Z for suspending.' +
             ' After restart the program will continue where it left off unless --restart is given.')
    p_weave.add_argument('infile', help='a valid wif or json file')
    p_weave.add_argument('--liftplan', action='store_true',
                         help='use liftplan rather then treadling with tie-up')
    p_weave.add_argument('--repeats', type=int, default=1, help=' the number of patterns to repeat')
    p_weave.add_argument('--threads', action='store_true',
                          help='use --repeats for number of threads rather than number of patterns')
    p_weave.add_argument('--start-repeat', type=int, default=1)
    p_weave.add_argument('--start-pick', type=int, default=1)
    p_weave.add_argument('--restart', action='store_true',
                         help='do not resume but start from given start numbers.')

    p_weave.set_defaults(function=weave)

    p_tieup = subparsers.add_parser(
        'tieup',
        help='Show tie-up instructions for a draft.')
    # p_tieup.add_argument('infile')

    p_stats = subparsers.add_parser(
        'stats',
        help='Print stats for a draft.')
    p_stats.add_argument('infile', help='a valid wif or json file')
    p_stats.set_defaults(function=stats)
    # p.add_argument('infile', nargs=1)

    # p.print_help()
    # print(__name__)
    # opts, args = p.parse_known_args(argv[1:])
    opts, args = p.parse_args(argv[1:])
    return opts.function(opts)
