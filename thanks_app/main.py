import webapp2
import handlers

config = {}
config['webapp2_extras.jinja2'] = {
                                    'template_path': 'templates',
                                    'compiled_path': None,
                                    'force_compiled': False,
                                    'environment_args': {
                                        'autoescape': True,
                                            'extensions': [
                                                'jinja2.ext.autoescape',
                                                'jinja2.ext.with_'
                                            ]
                                        },
                                    'globals': {
                                        'url_for' : webapp2.uri_for
                                        },
                                    'filters': None,
                                    }


routes = [
        webapp2.Route(r'/', handler=handlers.IndexHandler, name='name'),
        ]

app = webapp2.WSGIApplication(routes, debug=True, config=config)