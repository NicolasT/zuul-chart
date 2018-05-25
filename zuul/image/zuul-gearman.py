#!/usr/bin/env python3

import os
import sys
import signal

import zuul.cmd.scheduler

# This is a bit messy, but implemented this way to be compatible with Zuul
# without requiring changes to its codebase.
class Gearman(zuul.cmd.scheduler.Scheduler):
    app_name = 'queue'
    app_description = 'Gearman work queue'

    def exit_handler(self, signum, frame):
        self.stop_gear_server()
        sys.exit(0)

    def run(self):
        self.start_gear_server()

        signal.signal(signal.SIGTERM, self.exit_handler)
        while True:
            try:
                signal.pause()
            except KeyboardInterrupt:
                self.exit_handler(signal.SIGINT, None)


def main():
    Gearman().main()

if __name__ == '__main__':
    main()
