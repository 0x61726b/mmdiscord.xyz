import os
from flask import Flask, redirect
import click

app = Flask(__name__, static_url_path='')
app.url_map.strict_slashes = False


@click.group(invoke_without_command=True, options_metavar='[options]')
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        while True:
            app.run(host='0.0.0.0', port=3332)
            print("Restarting...")



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def all_routes(path):
    return redirect("https://discord.gg/xC7Jvju")




if __name__ == '__main__':
    main()