# optparse-modular-example

I tried to find a nice way for modular optparse that would provide opportunity to create meta-utils easily.

This repo is just a proof of concept.

## How it works

Every top has common and specific options:

``` shell
$ top1 --help
Usage: top1 [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  file to monitor
  -i INTERVAL, --interval=INTERVAL
                        interval between file readings in seconds
  -t TOP1_SPECIFIC1, --top1-specific1=TOP1_SPECIFIC1
                        Top1 specific option #1
  -s TOP1_SPECIFIC2, --top1-specific2=TOP1_SPECIFIC2
                        Top1 specific option #2
```

Here are top2 specific options:

``` shell
$ top2 --help
Usage: top2 [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  file to monitor
  -i INTERVAL, --interval=INTERVAL
                        interval between file readings in seconds
  -u TOP2_SPECIFIC1, --top2-specific1=TOP2_SPECIFIC1
                        Top2 specific option #1
  -w TOP2_SPECIFIC2, --top2-specific2=TOP2_SPECIFIC2
                        Top2 specific option #2
```

And metatop has both all other tops' specific and common options:

``` shell
$ metatop --help
Usage: metatop [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  file to monitor
  -i INTERVAL, --interval=INTERVAL
                        interval between file readings in seconds
  -t TOP1_SPECIFIC1, --top1-specific1=TOP1_SPECIFIC1
                        Top1 specific option #1
  -s TOP1_SPECIFIC2, --top1-specific2=TOP1_SPECIFIC2
                        Top1 specific option #2
  -u TOP2_SPECIFIC1, --top2-specific1=TOP2_SPECIFIC1
                        Top2 specific option #1
  -w TOP2_SPECIFIC2, --top2-specific2=TOP2_SPECIFIC2
                        Top2 specific option #2
```

## There are still few problems:

### Duplicity in utils' `__main__` part:

Top1 and Top2 have simillar `__main__`

``` python
if __name__ == '__main__':
    top = Top1()
    top.parse_options()
    print top.options
```

```
if __name__ == '__main__':
    top = Top2()
    top.parse_options()
    print top.options
```

Partly it's because of difference between `MetaTop` and `Top1`/`Top2`:

``` python
if __name__ == '__main__':
    print MetaTop().options
```

`BaseTop.__init__()` seems to be a perfect place for `parse_options()` call if not this difference.
