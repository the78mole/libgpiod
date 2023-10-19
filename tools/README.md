gpiomon
=======

Help output of gpiomon

```
Usage: gpiomon [OPTIONS] <line>...

Wait for events on GPIO lines and print them to standard output.

Lines are specified by name, or optionally by offset if the chip option
is provided.

Options:
      --banner          display a banner on successful startup
  -b, --bias <bias>     specify the line bias
                        Possible values: 'pull-down', 'pull-up', 'disabled'.
                        (default is to leave bias unchanged)
      --by-name         treat lines as names even if they would parse as an offset
  -c, --chip <chip>     restrict scope to a particular chip
  -C, --consumer <name> consumer name applied to requested lines (default is 'gpiomon')
  -e, --edges <edges>   specify the edges to monitor
                        Possible values: 'falling', 'rising', 'both'.
                        (default is 'both')
  -E, --event-clock <clock>
                        specify the source clock for event timestamps
                        Possible values: 'monotonic', 'realtime', 'hte'.
                        (default is 'monotonic')
                        By default 'realtime' is formatted as UTC, others as raw u64.
  -h, --help            display this help and exit
  -F, --format <fmt>    specify a custom output format
      --idle-timeout <period>
                        exit gracefully if no events occur for the period specified
  -l, --active-low      treat the line as active low, flipping the sense of
                        rising and falling edges
      --localtime       format event timestamps as local time
        Only makes sense with `-E realtime`
  -n, --num-events <num>
                        exit after processing num events
  -p, --debounce-period <period>
                        debounce the line(s) with the specified period
  -q, --quiet           don't generate any output
  -s, --strict          abort if requested line names are not unique
      --unquoted        don't quote line or consumer names
      --utc             format event timestamps as UTC (default for 'realtime')
        Only makes sense with `-E realtime`
  -v, --version         output version information and exit

Chips:
    A GPIO chip may be identified by number, name, or path.
    e.g. '0', 'gpiochip0', and '/dev/gpiochip0' all refer to the same chip.

Periods:
    Periods are taken as milliseconds unless units are specified. e.g. 10us.
    Supported units are 's', 'ms', and 'us'.

Format specifiers:
  %o   GPIO line offset
  %l   GPIO line name
  %c   GPIO chip name
  %d   numeric edge event type ('0' - rising or '1' - falling)
  %e   numeric edge event type ('1' - rising or '2' - falling)
  %E   edge event type ('rising' or 'falling')
  %N   event timestamp as nanoseconds
  %S   event timestamp as seconds
  %U   event timestamp as UTC
  %L   event timestamp as local time

Example:
  gpiomon -e both -F "[%N] %l %d %E" -p 10 -b pull-up --banner GPIO17 GPIO27
```
