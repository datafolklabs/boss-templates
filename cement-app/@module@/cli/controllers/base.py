""" @project.title@ base controller."""

from cement.core.controller import CementBaseController, expose

class @class_prefix@BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = '@description@'
        arguments = [
            (['-f', '--foo'], 
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        raise NotImplementedError
