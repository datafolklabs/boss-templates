"""@project@ base controller."""

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
        print("Inside @class_prefix@BaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``@module@.cli.templates``, or ``/var/lib/@module@/templates/``.
        #
