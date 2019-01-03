from coinop import app

config_file = ('COINOP_CONFIG_FILE'
               if not app.testing
               else 'COINOP_TEST_CONFIG_FILE')


if __name__ == '__main__':
    app.config.from_envvar(config_file)

    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        # For HTML responses only!
        DebugToolbarExtension(app)
    app.run()
