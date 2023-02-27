import tempfile
import glob
import os

import click
from devpy import util


@click.command()
def build():
    """📖 Build astropy
    """
    with tempfile.TemporaryDirectory() as wheel_dir:
        p = util.run(['python', '-m', 'build', '--no-isolation', '-x', '-w',
                      '--outdir', wheel_dir],
                     output=False)

        if p.returncode != 0:
            print(p.stdout.decode('utf-8'))
            print()
            print("Error building wheel.")
            sys.exit(-1)

        wheel = glob.glob(os.path.join(wheel_dir, '*'))[0]
        util.run(['pip', 'install', wheel])
